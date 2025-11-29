"""
Vector database and embeddings handler using ChromaDB and FAISS
"""
import os
import json
import warnings
import numpy as np
from typing import List, Dict, Tuple
from sentence_transformers import SentenceTransformer

# Suppress deprecation and runtime warnings that break Streamlit output
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', message='.*distutils.*')
warnings.filterwarnings('ignore', message='.*sqlite3.*')
warnings.filterwarnings('ignore', message='.*telemetry.*')

try:
    import chromadb
    from chromadb.config import Settings
    CHROMADB_AVAILABLE = True
except (ImportError, Exception) as e:
    CHROMADB_AVAILABLE = False
    print(f"Warning: ChromaDB not available: {e}")

try:
    import faiss
    FAISS_AVAILABLE = True
except (ImportError, Exception) as e:
    FAISS_AVAILABLE = False
    print(f"Warning: FAISS not available: {e}")

class VectorDatabase:
    """Handles product embeddings and similarity search"""
    
    def __init__(self, db_type="chroma", embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
        self.db_type = db_type
        self.embedding_model_name = embedding_model
        self.embedding_model = SentenceTransformer(embedding_model)
        self.products = []
        
        if db_type == "chroma":
            self._init_chroma_db()
        elif db_type == "faiss":
            self._init_faiss_db()
            
    def _init_chroma_db(self):
        """Initialize ChromaDB vector store"""
        if not CHROMADB_AVAILABLE:
            self._init_faiss_db()
            self.db_type = "faiss"
            return
            
        try:
            self.client = chromadb.Client()
            self.collection = self.client.get_or_create_collection(
                name="products",
                metadata={"hnsw:space": "cosine"}
            )
        except Exception as e:
            print(f"Warning: ChromaDB failed, using FAISS: {e}")
            self._init_faiss_db()
            self.db_type = "faiss"
        
    def _init_faiss_db(self):
        """Initialize FAISS vector store"""
        if not FAISS_AVAILABLE:
            raise ImportError("FAISS is not installed. Install with: pip install faiss-cpu")
        self.index = None
        self.id_to_product = {}
        
    def add_products(self, products: List[Dict]):
        """Add products to vector database with embeddings"""
        self.products = products
        
        for product in products:
            # Create searchable text from product fields
            text = f"{product['name']} {product.get('description', '')} {' '.join(product.get('tags', []))}"
            
            if self.db_type == "chroma":
                self._add_to_chroma(product, text)
            elif self.db_type == "faiss":
                self._add_to_faiss(product, text)
                
    def _add_to_chroma(self, product: Dict, text: str):
        """Add product to Chroma collection"""
        embedding = self.embedding_model.encode(text).tolist()
        
        self.collection.add(
            ids=[str(product['id'])],
            embeddings=[embedding],
            documents=[text],
            metadatas=[{
                "name": product['name'],
                "price": str(product['price']),
                "category": product['category'],
                "rating": str(product.get('rating', 0)),
                "full_data": json.dumps(product)
            }]
        )
        
    def _add_to_faiss(self, product: Dict, text: str):
        """Add product to FAISS index"""
        if not FAISS_AVAILABLE:
            return
        embedding = self.embedding_model.encode(text)
        
        if self.index is None:
            self.index = faiss.IndexFlatL2(len(embedding))
            
        self.index.add(np.array([embedding]))
        self.id_to_product[len(self.id_to_product)] = product
        
    def search(self, query: str, top_k: int = 5, threshold: float = 0.3) -> List[Tuple[Dict, float]]:
        """
        Search for similar products
        Returns list of (product, similarity_score) tuples
        """
        query_embedding = self.embedding_model.encode(query)
        
        if self.db_type == "chroma":
            return self._search_chroma(query_embedding, top_k, threshold)
        elif self.db_type == "faiss":
            return self._search_faiss(query_embedding, top_k, threshold)
            
    def _search_chroma(self, query_embedding, top_k: int, threshold: float) -> List[Tuple[Dict, float]]:
        """Search using Chroma"""
        if not CHROMADB_AVAILABLE or self.collection is None:
            return []
            
        try:
            results = self.collection.query(
                query_embeddings=[query_embedding.tolist()],
                n_results=top_k
            )
            
            products_with_scores = []
            if results and results['ids'] and len(results['ids']) > 0:
                for i, product_id in enumerate(results['ids'][0]):
                    metadata = results['metadatas'][0][i]
                    distance = results['distances'][0][i]
                    
                    # Convert distance to similarity (cosine distance: 0=similar, 2=dissimilar)
                    similarity = 1 - (distance / 2)
                    
                    if similarity >= threshold:
                        product = json.loads(metadata['full_data'])
                        products_with_scores.append((product, similarity))
                        
            return sorted(products_with_scores, key=lambda x: x[1], reverse=True)
        except Exception as e:
            print(f"ChromaDB search error: {e}")
            return []
        
    def _search_faiss(self, query_embedding, top_k: int, threshold: float) -> List[Tuple[Dict, float]]:
        """Search using FAISS"""
        if self.index is None or self.index.ntotal == 0:
            return []
            
        distances, indices = self.index.search(np.array([query_embedding]), min(top_k, self.index.ntotal))
        
        products_with_scores = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx == -1:
                continue
            # Convert L2 distance to similarity score (0-1)
            similarity = 1 / (1 + distance)
            
            if similarity >= threshold:
                product = self.id_to_product[int(idx)]
                products_with_scores.append((product, similarity))
                
        return products_with_scores[:top_k]
        
    def get_all_products(self) -> List[Dict]:
        """Get all products in database"""
        return self.products
