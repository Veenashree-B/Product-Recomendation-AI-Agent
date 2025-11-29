"""
LLM-based Product Recommendation Agent
Uses OpenAI GPT for intelligent product recommendations
"""
import os
import json
from typing import List, Dict, Tuple
from datetime import datetime

class ProductRecommendationAgent:
    """Intelligent product recommendation agent using LLM"""
    
    def __init__(self, api_key: str = None, model: str = "gpt-4o-mini"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self.conversation_history = []
        self.user_preferences = {}
        
        if self.api_key:
            try:
                import openai
                openai.api_key = self.api_key
                self.client = openai
                self.openai_available = True
            except:
                self.openai_available = False
        else:
            self.openai_available = False
            
    def extract_preferences(self, user_query: str) -> Dict:
        """Extract user preferences from natural language query with improved accuracy"""
        preferences = {
            "budget_min": None,
            "budget_max": None,
            "categories": [],
            "features": [],
            "rating_min": 0,
            "keywords": []
        }
        
        query_lower = user_query.lower()
        
        # Extract numeric prices with improved pattern
        import re
        
        # Check for "under X" pattern
        under_match = re.search(r'under\s+\$?(\d+(?:\.\d{2})?)', query_lower)
        if under_match:
            preferences["budget_max"] = float(under_match.group(1))
        
        # Check for "between X and Y" pattern
        between_match = re.search(r'between\s+\$?(\d+(?:\.\d{2})?)\s+and\s+\$?(\d+(?:\.\d{2})?)', query_lower)
        if between_match:
            min_price = float(between_match.group(1))
            max_price = float(between_match.group(2))
            preferences["budget_min"] = min(min_price, max_price)
            preferences["budget_max"] = max(min_price, max_price)
        
        # Check for "X - Y" or "X to Y" pattern
        range_match = re.search(r'\$(\d+(?:\.\d{2})?)\s*(?:to|-|and)\s*\$(\d+(?:\.\d{2})?)', query_lower)
        if range_match and not between_match:
            min_price = float(range_match.group(1))
            max_price = float(range_match.group(2))
            preferences["budget_min"] = min(min_price, max_price)
            preferences["budget_max"] = max(min_price, max_price)
        
        # Extract all numbers as potential prices
        if not preferences["budget_max"]:
            numbers = re.findall(r'\d+(?:\.\d{2})?', user_query)
            if numbers:
                nums = [float(n) for n in numbers]
                # If single number > 20, assume it's a price limit
                if len(nums) == 1 and nums[0] > 20:
                    # Check if it follows "under" or similar
                    if 'under' in query_lower or 'below' in query_lower or 'less' in query_lower:
                        preferences["budget_max"] = nums[0]
                # If multiple numbers, use as range
                elif len(nums) >= 2:
                    preferences["budget_min"] = min(nums)
                    preferences["budget_max"] = max(nums)
                
        # Extract features - expanded list
        feature_keywords = {
            "wireless": "wireless",
            "wired": "wired",
            "ergonomic": "ergonomic",
            "gaming": "gaming",
            "mechanical": "mechanical",
            "portable": "portable",
            "lightweight": "lightweight",
            "noise-cancelling": "noise-cancelling",
            "noise cancelling": "noise-cancelling",
            "smart": "smart",
            "waterproof": "waterproof",
            "rgb": "rgb",
            "professional": "professional",
            "budget": "budget",
            "premium": "premium"
        }
        for keyword, feature in feature_keywords.items():
            if keyword in query_lower:
                preferences["features"].append(feature)
        
        # Extract categories
        category_keywords = {
            "electronics": "Electronics",
            "furniture": "Furniture",
            "home": "Home",
            "shoes": "Shoes",
            "chair": "Furniture",
            "desk": "Furniture",
            "monitor": "Electronics",
            "keyboard": "Electronics",
            "mouse": "Electronics",
            "headphones": "Electronics",
            "laptop": "Electronics",
            "tablet": "Electronics",
            "lamp": "Home",
            "light": "Home",
            "speaker": "Electronics"
        }
        for keyword, category in category_keywords.items():
            if keyword in query_lower and category not in preferences["categories"]:
                preferences["categories"].append(category)
        
        # Extract main keywords for ranking
        words = query_lower.split()
        preferences["keywords"] = [w for w in words if len(w) > 3 and w not in ['under', 'over', 'with', 'that', 'this', 'from', 'between', 'and', 'the']]
                
        return preferences
        
    def filter_products(self, products: List[Dict], preferences: Dict) -> List[Dict]:
        """Filter products based on user preferences with strict criteria"""
        filtered = products
        
        # STRICT: Filter by price if specified
        if preferences["budget_min"] is not None:
            filtered = [p for p in filtered if p.get("price", float('inf')) >= preferences["budget_min"]]
        if preferences["budget_max"] is not None:
            filtered = [p for p in filtered if p.get("price", 0) <= preferences["budget_max"]]
            
        # STRICT: Filter by category
        if preferences["categories"]:
            category_filtered = []
            for p in filtered:
                if any(cat.lower() in p.get("category", "").lower() for cat in preferences["categories"]):
                    category_filtered.append(p)
            filtered = category_filtered if category_filtered else filtered  # Keep original if no matches
            
        # STRONG: Filter by features - prefer products with matching tags
        if preferences["features"]:
            products_with_features = [p for p in filtered if any(
                feat in p.get("tags", [])
                for feat in preferences["features"]
            )]
            # Use feature-matched products if any exist
            if products_with_features:
                filtered = products_with_features
            
        # Filter by rating
        if preferences["rating_min"] > 0:
            filtered = [p for p in filtered if p.get("rating", 0) >= preferences["rating_min"]]
            
        return filtered if filtered else products  # Return original if filters eliminate everything
        
    def rank_products(self, products: List[Dict], query: str, similarity_scores: List[Tuple[Dict, float]] = None, preferences: Dict = None) -> List[Dict]:
        """Rank products based on relevance with improved scoring"""
        if not products:
            return []
            
        # If we have similarity scores from vector DB, use them as primary signal
        if similarity_scores:
            product_dict = {p['id']: p for p in products}
            ranked = []
            for p, score in sorted(similarity_scores, key=lambda x: x[1], reverse=True):
                ranked.append(p)
            return ranked
            
        # Advanced ranking based on relevance
        scored_products = []
        query_lower = query.lower()
        keywords = preferences.get('keywords', []) if preferences else []
        
        for product in products:
            score = 0.0
            product_name_lower = product['name'].lower()
            product_desc_lower = product.get('description', '').lower()
            product_tags = [t.lower() for t in product.get('tags', [])]
            
            # Exact name match (highest priority)
            if query_lower == product_name_lower:
                score += 100.0
            # Partial name match
            elif query_lower in product_name_lower:
                score += 50.0
            
            # Keyword matches in name
            for keyword in keywords:
                if keyword in product_name_lower:
                    score += 10.0
            
            # Description matches
            for keyword in keywords:
                if keyword in product_desc_lower:
                    score += 5.0
            
            # Tag matches (strong signal)
            matching_tags = 0
            for keyword in keywords:
                if any(keyword in tag or tag in keyword for tag in product_tags):
                    score += 8.0
                    matching_tags += 1
            
            # Category match bonus (if preferences extracted)
            if preferences and preferences.get('categories'):
                if product.get('category') in preferences['categories']:
                    score += 15.0
            
            # Price relevance (if budget specified)
            if preferences and preferences.get('budget_max'):
                product_price = product.get('price', 0)
                budget_max = preferences['budget_max']
                if product_price <= budget_max:
                    # Boost products closer to budget limit
                    score += (1 - (product_price / budget_max)) * 5.0
            
            # Rating boost (secondary signal)
            rating = product.get('rating', 0)
            score += rating * 2.0
            
            scored_products.append((product, score))
            
        return [p for p, _ in sorted(scored_products, key=lambda x: x[1], reverse=True)]
        
    def generate_recommendation_text(self, products: List[Dict], user_query: str) -> str:
        """Generate simple, direct recommendation summary without AI"""
        if not products:
            return "No products found matching your criteria. Try adjusting your search."
        
        count = len(products)
        if count == 1:
            p = products[0]
            return f"Found 1 matching product: {p['name']} (${p['price']}, Rating: ⭐ {p.get('rating', 'N/A')})"
        else:
            return f"Found {count} matching products. Showing best matches below sorted by relevance:"
            
    def add_to_history(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        
    def get_history(self) -> List[Dict]:
        """Get conversation history"""
        return self.conversation_history
        
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
