"""
Streamlit UI for AI Product Recommendation Agent
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import streamlit as st
from config.settings import STREAMLIT_PAGE_CONFIG, SAMPLE_PRODUCTS, OPENAI_API_KEY, DEFAULT_LLM_MODEL
from src.agents.recommendation_agent import ProductRecommendationAgent
from src.vectors.db import VectorDatabase
import pandas as pd

# Page configuration
st.set_page_config(**STREAMLIT_PAGE_CONFIG)

# Custom CSS
st.markdown("""
<style>
    .main { padding: 20px; }
    .product-card { 
        border: 1px solid #ddd; 
        border-radius: 8px; 
        padding: 15px; 
        margin: 10px 0;
        background: #f9f9f9;
    }
    .product-title { font-size: 18px; font-weight: bold; color: #1f77b4; }
    .product-price { font-size: 20px; font-weight: bold; color: #d62728; }
    .product-rating { color: #ff7f0e; }
    .recommendation-box {
        background: #e7f3ff;
        border-left: 4px solid #1f77b4;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "agent" not in st.session_state:
    st.session_state.agent = ProductRecommendationAgent(
        api_key=OPENAI_API_KEY,
        model=DEFAULT_LLM_MODEL
    )
    
if "vector_db" not in st.session_state:
    st.session_state.vector_db = VectorDatabase()
    st.session_state.vector_db.add_products(SAMPLE_PRODUCTS)
    
if "history" not in st.session_state:
    st.session_state.history = []

# Header
st.title("🛍️ Smart Product Recommendation Engine")
st.markdown("""
**Intelligent Product Search & Filtering**
- 🔍 Semantic product search
- 📊 Real-time ranking
- ✅ Accurate price & category filtering
""")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # API Status
    if OPENAI_API_KEY:
        st.success("✅ OpenAI API connected")
    else:
        st.warning("⚠️ OpenAI API not configured (using templates)")
        
    # Model selection
    selected_model = st.selectbox(
        "LLM Model",
        ["gpt-4o-mini", "gpt-3.5-turbo"],
        help="Select the language model for recommendations"
    )
    st.session_state.agent.model = selected_model
    
    # Similarity threshold
    similarity_threshold = st.slider(
        "Similarity Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="Minimum similarity score for products"
    )
    
    # Max recommendations
    max_recs = st.slider(
        "Max Recommendations",
        min_value=1,
        max_value=10,
        value=5,
        help="Maximum number of products to recommend"
    )
    
    # Clear history button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.history = []
        st.session_state.agent.clear_history()
        st.success("History cleared!")
        
    st.divider()
    st.markdown("### 📊 Products Available")
    st.metric("Total Products", len(SAMPLE_PRODUCTS))

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Search input
    user_query = st.text_input(
        "🔍 What product are you looking for?",
        placeholder="E.g., 'affordable wireless headphones under $200'",
        label_visibility="collapsed"
    )
    
    # Search button
    search_button = st.button("🚀 Get Recommendations", use_container_width=True)
    
with col2:
    # Quick filters
    st.subheader("Quick Filters")
    selected_category = st.selectbox(
        "Category",
        ["All", "Electronics", "Furniture", "Home"],
        label_visibility="collapsed"
    )

# Display recommendations
if search_button and user_query:
    with st.spinner("🔍 Searching for the perfect products..."):
        # Extract preferences
        preferences = st.session_state.agent.extract_preferences(user_query)
        
        # Search with vector DB
        search_results = st.session_state.vector_db.search(
            user_query,
            top_k=max_recs * 2,
            threshold=similarity_threshold
        )
        
        # Get products and scores
        products_with_scores = [(p, score) for p, score in search_results]
        products = [p for p, _ in products_with_scores]
        
        # Filter by preferences
        filtered_products = st.session_state.agent.filter_products(products, preferences)
        
        # Rank products
        ranked_products = st.session_state.agent.rank_products(
            filtered_products,
            user_query,
            products_with_scores[:len(filtered_products)] if filtered_products else [],
            preferences
        )[:max_recs]
        
        # Generate recommendation text
        recommendation_text = st.session_state.agent.generate_recommendation_text(
            ranked_products,
            user_query
        )
        
        # Add to history
        st.session_state.agent.add_to_history("user", user_query)
        st.session_state.agent.add_to_history("assistant", recommendation_text)
        st.session_state.history.append({"role": "user", "content": user_query})
        st.session_state.history.append({"role": "assistant", "content": recommendation_text})
        
        # Display recommendation
        st.markdown(f"""
        <div class="recommendation-box">
        <strong>💡 Recommendation:</strong><br>{recommendation_text}
        </div>
        """, unsafe_allow_html=True)
        
        # Display products
        st.subheader(f"📦 Top Recommendations ({len(ranked_products)} products found)")
        
        if ranked_products:
            for idx, product in enumerate(ranked_products, 1):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"""
                    <div class="product-card">
                    <div class="product-title">{idx}. {product['name']}</div>
                    <div class="product-price">${product['price']}</div>
                    <div style="margin: 10px 0;">{product.get('description', 'N/A')}</div>
                    <div class="product-rating">⭐ {product.get('rating', 'N/A')} | Category: {product['category']}</div>
                    <div style="margin-top: 8px; color: #666;">
                        Tags: {', '.join(product.get('tags', []))}
                    </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                with col2:
                    # Add to cart/favorites (placeholder)
                    if st.button("❤️", key=f"fav_{product['id']}"):
                        st.success(f"Added {product['name']} to favorites!")
        else:
            st.info("❌ No products found matching your criteria. Try adjusting your filters.")

# Display conversation history in tabs
if st.session_state.history:
    st.divider()
    tab1, tab2 = st.tabs(["💬 Chat History", "📋 All Products"])
    
    with tab1:
        st.subheader("Conversation History")
        for msg in st.session_state.history:
            if msg["role"] == "user":
                st.markdown(f"**You:** {msg['content']}")
            else:
                st.markdown(f"**AI Assistant:** {msg['content']}")
                
    with tab2:
        st.subheader("Available Products")
        
        # Display all products in a table
        products_df = pd.DataFrame([{
            "Product": p['name'],
            "Price": f"${p['price']}",
            "Category": p['category'],
            "Rating": p.get('rating', 'N/A'),
            "Description": p.get('description', '')[:50] + "..."
        } for p in SAMPLE_PRODUCTS])
        
        st.dataframe(products_df, use_container_width=True, hide_index=True)

# Footer
st.divider()
st.markdown("""
---
**🚀 AI Product Recommendation Agent v1.0**
- Powered by OpenAI GPT & ChromaDB Vector Search
- © 2025 All rights reserved
""")
