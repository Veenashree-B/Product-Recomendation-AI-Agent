# Quick Start Guide - AI Product Recommendation Agent

## 🚀 5-Minute Setup

### 1. Clone or Download
```bash
git clone https://github.com/your-username/product-recommender.git
cd product-recommender
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
```bash
# Edit .env file
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**Get your API key:**
1. Visit https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key and paste in `.env`

### 5. Run the App
```bash
streamlit run app.py
```

App will open at: `http://localhost:8501`

---

## 💡 Try These Example Queries

1. **"I need a wireless headphone under $200"**
   - Will search for headphones in the electronics category under $200

2. **"Show me a high-quality office chair for my desk"**
   - Will find office furniture with high ratings

3. **"Budget gaming monitor, preferably with 144Hz refresh rate"**
   - Will search for monitors with gaming features

---

## 🎯 What the App Does

1. **Accepts Natural Language Queries**
   - "I want a cheap laptop" → Extracted: budget=$200-500, category=electronics

2. **Searches Product Database**
   - Semantic search using AI embeddings
   - Vector similarity matching (cosine distance)
   - Smart filtering by price, category, features

3. **Ranks Results**
   - Multi-factor ranking: 75% semantic + 10% ratings + 8% keyword + 5% fuzzy + 2% recency
   - Intelligently scores product matches

4. **Generates Recommendations**
   - Uses GPT-4o-mini (cost-effective) to explain why each product is a good fit
   - Falls back to template responses if API unavailable
   - Maintains conversation history

5. **Displays Results**
   - Product cards with image, price, rating, description
   - Chat history
   - Settings sidebar (model selection, thresholds)

---

## 📁 Project Structure

```
product-recommender/
├── app.py                          # Streamlit UI
├── config/
│   └── settings.py                 # Configuration (API keys, models, products)
├── src/
│   ├── agents/
│   │   └── recommendation_agent.py  # Core recommendation logic
│   └── vectors/
│       └── db.py                    # Vector database (ChromaDB/FAISS)
├── requirements.txt                # Python dependencies
├── .env                            # API keys (create this)
├── README.md                       # Full documentation
├── ARCHITECTURE.md                 # Technical architecture
└── DEPLOYMENT.md                   # Deployment guide
```

---

## ⚙️ Configuration

Edit `config/settings.py` to customize:

```python
# Model selection
DEFAULT_LLM_MODEL = "gpt-4o-mini"      # Fast & cheap
BACKUP_LLM_MODEL = "gpt-3.5-turbo"     # Extra cheap fallback

# Vector database
VECTOR_DB_TYPE = "chromadb"            # Options: chromadb, faiss

# Recommendation settings
MAX_RECOMMENDATIONS = 10               # Max products to show
SIMILARITY_THRESHOLD = 0.3             # Min semantic match (0-1)
SEARCH_TOP_K = 20                      # Candidate products to evaluate

# Add your own products
SAMPLE_PRODUCTS = [
    {
        "id": "laptop-1",
        "name": "Gaming Laptop Pro",
        "category": "electronics",
        "price": 1499.99,
        "description": "High-performance laptop for gaming...",
        "tags": ["gaming", "laptop", "portable"],
        "rating": 4.8
    },
    # Add more...
]
```

---

## 🔑 API Keys & Services

### Required: OpenAI API
- **Purpose:** Generate recommendation descriptions
- **Cost:** ~$0.001 per request (very cheap)
- **Setup:**
  1. Create account: https://platform.openai.com
  2. Add payment method
  3. Get API key
  4. Add to `.env`

### Optional: Google Sheets Integration
- Pull product data from Google Sheets
- Set in `ENABLE_GOOGLE_SHEETS = True`

### Optional: Shopify Integration
- Integrate with Shopify store
- Automatically sync products
- Set in `ENABLE_SHOPIFY = True`

### Optional: Firebase
- Store user preferences
- Track recommendation feedback
- Set in `ENABLE_FIREBASE = True`

---

## 🧪 Testing Locally

1. **Start app:**
   ```bash
   streamlit run app.py
   ```

2. **Use sidebar settings:**
   - Select different LLM models
   - Adjust similarity threshold (0.0-1.0)
   - Control number of recommendations (1-10)

3. **Check console output:**
   ```
   Running on local URL: http://localhost:8501
   ```

4. **Test queries:**
   - Type in search box
   - Click "Get Recommendations"
   - View results in chat

---

## 📊 Performance

| Metric | Current | Scalable To |
|--------|---------|-------------|
| Products | 5 sample | 10,000+ with Pinecone |
| Response Time | <2 seconds | <500ms with caching |
| Users | 1-10 concurrent | 100+ with Cloud Run |
| Queries/Month | Unlimited | Up to 1M with OpenAI paid |

---

## ⚡ Speed Tips

1. **First run is slow** (1-2 min)
   - Downloading embedding model (380 MB)
   - Creating vector database
   - Subsequent runs: <2 seconds

2. **Use Streamlit Cloud**
   - Caching works better
   - Auto-reloads on code push
   - Custom domain support

3. **Optimize for production:**
   - Enable @st.cache_resource decorators
   - Use lighter embedding model
   - Batch requests

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### "OpenAI API key is invalid"
- Check `.env` file has correct format
- Get new key from https://platform.openai.com/api-keys
- Make sure key starts with `sk-`

### "Port 8501 is in use"
```bash
streamlit run app.py --server.port 8502
```

### "Slow first load"
This is normal! Streamlit caches embeddings after first run.

### "Vector database error"
```bash
# Clear cache and reinstall
rm -rf ~/.streamlit/cache
pip install --upgrade chromadb
```

---

## 📱 Deploy in 2 Minutes (Streamlit Cloud)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Go to** https://share.streamlit.io
3. **Click "New app"**
4. **Select your GitHub repo**
5. **Set secrets** → Add `OPENAI_API_KEY`
6. **Click Deploy** ✨

Your app is now live at: `https://your-username-product-recommender.streamlit.app`

---

## 📚 More Resources

- **Full Setup:** See `DEPLOYMENT.md`
- **Technical Details:** See `ARCHITECTURE.md`
- **Complete Guide:** See `README.md`
- **API Reference:** Check docstrings in source code

---

## ✨ Next Steps

1. ✅ Get the app running locally
2. 🔑 Set up OpenAI API key
3. 🚀 Deploy to Streamlit Cloud
4. 📊 Add your own product data
5. 💰 Integrate payment system
6. 📈 Monitor analytics

---

**Questions?** Check the full documentation or open a GitHub issue!
