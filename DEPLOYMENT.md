# 🚀 Setup & Deployment Guide

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git
- OpenAI API key (free tier: https://platform.openai.com)

## Local Setup (5 minutes)

### Step 1: Clone Repository
```bash
git clone https://github.com/your-username/product-recommender.git
cd product-recommender
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
# Create .env file
cat > .env << EOF
OPENAI_API_KEY=sk-your-api-key-here
EOF

# Or manually create .env and add:
# OPENAI_API_KEY=your_key_here
```

Get your OpenAI API key:
1. Visit https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy and save it
4. Add to `.env` file

### Step 5: Run Application
```bash
streamlit run app.py
```

App will open at: `http://localhost:8501`

## Deployment Options

### Option 1: Streamlit Cloud (Recommended - FREE)

**Pros:**
- Free hosting
- Automatic deployments
- Easy environment variable management
- Custom domain support

**Steps:**

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Streamlit Cloud**
   - Visit https://share.streamlit.io
   - Click "New app"
   - Select your GitHub repository
   - Choose `app.py` as main file
   - Click "Deploy"

3. **Set Environment Variables**
   - In Streamlit Cloud dashboard
   - Go to "Advanced settings"
   - Add `OPENAI_API_KEY` secret
   - Redeploy

4. **Share Your App**
   - Get the URL: `https://your-username-product-recommender.streamlit.app`
   - Share with anyone

**Demo URL Format:**
```
https://[your-username]-product-recommender.streamlit.app
```

### Option 2: Heroku (Pay-as-you-go)

**Steps:**

1. **Install Heroku CLI**
   ```bash
   # Windows/macOS: Download from https://devcenter.heroku.com/articles/heroku-cli
   
   # Linux:
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Create Heroku App**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Create Procfile**
   ```bash
   echo "web: streamlit run --server.port=\$PORT app.py" > Procfile
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set OPENAI_API_KEY=your_api_key
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **View Logs**
   ```bash
   heroku logs --tail
   ```

### Option 3: Docker (Advanced)

**Create Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Build and Run:**
```bash
# Build image
docker build -t product-recommender:latest .

# Run container
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your_key \
  product-recommender:latest

# Access at http://localhost:8501
```

**Deploy to Docker Hub:**
```bash
# Tag image
docker tag product-recommender:latest username/product-recommender:latest

# Push to Docker Hub
docker push username/product-recommender:latest
```

### Option 4: AWS (EC2)

**Steps:**

1. **Launch EC2 Instance**
   - Ubuntu 22.04 LTS (free tier eligible)
   - t2.micro instance type
   - Security group: Allow ports 22 (SSH), 8501 (Streamlit)

2. **Connect and Setup**
   ```bash
   # SSH into instance
   ssh -i your-key.pem ubuntu@your-instance-ip
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and dependencies
   sudo apt install python3-pip python3-venv -y
   
   # Clone repo
   git clone https://github.com/your-username/product-recommender.git
   cd product-recommender
   
   # Setup venv
   python3 -m venv venv
   source venv/bin/activate
   
   # Install packages
   pip install -r requirements.txt
   
   # Create .env file
   echo "OPENAI_API_KEY=your_key" > .env
   ```

3. **Run with Screen (Background)**
   ```bash
   screen -S streamlit
   streamlit run app.py --server.port=8501
   
   # Ctrl+A then D to detach
   ```

4. **Access**
   ```
   http://your-instance-ip:8501
   ```

### Option 5: Google Cloud Run (Serverless)

**Steps:**

1. **Create `cloudbuild.yaml`:**
   ```yaml
   steps:
   - name: 'gcr.io/cloud-builders/docker'
     args: ['build', '-t', 'gcr.io/$PROJECT_ID/product-recommender', '.']
   - name: 'gcr.io/cloud-builders/docker'
     args: ['push', 'gcr.io/$PROJECT_ID/product-recommender']
   - name: 'gcr.io/cloud-builders/gke-deploy'
     args:
     - run
     - --filename=k8s/
     - --image=gcr.io/$PROJECT_ID/product-recommender
   ```

2. **Deploy**
   ```bash
   gcloud run deploy product-recommender \
     --source . \
     --platform managed \
     --region us-central1 \
     --set-env-vars OPENAI_API_KEY=your_key
   ```

3. **Get URL**
   ```bash
   gcloud run services describe product-recommender --region us-central1
   ```

## Performance Optimization

### Cache Embeddings
```python
@st.cache_resource
def load_vector_db():
    return VectorDatabase()

db = load_vector_db()
```

### Limit Product Dataset
```python
# In config/settings.py
MAX_PRODUCTS = 500  # Limit for faster search
```

### Use Smaller Embedding Model
```python
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # Lightweight
# Instead of: "all-mpnet-base-v2"  # Heavier
```

## Monitoring & Debugging

### View Logs (Streamlit Cloud)
- Dashboard → App settings → View logs

### Local Testing
```bash
# Run with debug enabled
streamlit run app.py --logger.level=debug

# Profile performance
streamlit run app.py --profile-memory
```

### Error Handling Checklist
- [ ] API key is valid
- [ ] Network connection active
- [ ] All dependencies installed
- [ ] No port conflicts (8501)
- [ ] Python version >= 3.9

## Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit
```

### "OpenAI API rate limit"
- Wait 1-2 minutes
- Upgrade to paid plan
- Reduce requests per minute

### "Vector DB initialization fails"
```bash
# Clear cache
rm -rf ~/.streamlit/cache

# Reinstall ChromaDB
pip install --upgrade chromadb
```

### "Slow performance on first load"
- This is normal! Embeddings are generated on first run
- Subsequent requests will be 10x faster

### Port 8501 already in use
```bash
# Use different port
streamlit run app.py --server.port=8502
```

## Cost Estimation

| Service | Monthly Cost | Notes |
|---------|-------------|-------|
| Streamlit Cloud | FREE | Recommended for most |
| OpenAI API | ~$1-50 | ~$0.001 per request |
| Heroku | $7+ | Cheapest paid option |
| AWS Free Tier | FREE | 12 months free |
| Google Cloud Run | ~$0.40 | Per 1M requests |

**To minimize costs:**
- Use gpt-3.5-turbo instead of gpt-4
- Cache embeddings
- Batch requests when possible
- Use free tier services

## Security Best Practices

### Environment Variables
```bash
# ✅ Good
export OPENAI_API_KEY=sk-xxx
echo "OPENAI_API_KEY=sk-xxx" > .env

# ❌ Bad
OPENAI_API_KEY = "sk-xxx"  # In code
python app.py --api-key=sk-xxx  # In command line
```

### Production Checklist
- [ ] Store secrets in environment variables
- [ ] Use HTTPS (automatic on Streamlit Cloud)
- [ ] Rotate API keys regularly
- [ ] Monitor API usage
- [ ] Set rate limits
- [ ] Use strong passwords
- [ ] Enable 2FA on hosting platform

## Scaling for 10,000+ Products

1. **Switch to Pinecone (Cloud Vector DB)**
   ```python
   VECTOR_DB_TYPE = "pinecone"
   PINECONE_API_KEY = "xxx"
   PINECONE_INDEX = "products"
   ```

2. **Add Database (Firebase/Supabase)**
   ```python
   # Store product metadata separately
   # Query: Vector DB for candidates → DB for details
   ```

3. **Implement Caching**
   ```python
   @st.cache_data(ttl=3600)
   def get_popular_products():
       return db.search("popular", top_k=100)
   ```

4. **Add Request Queue (Celery)**
   ```bash
   celery -A app worker --loglevel=info
   ```

## Next Steps

1. ✅ Deploy to Streamlit Cloud
2. 📊 Monitor usage analytics
3. 🔄 Integrate real product data
4. 💾 Add user feedback system
5. 🚀 Scale to 10k+ products
6. 💰 Set up payment processing
7. 📈 Add recommendation analytics

---

**Need Help?**
- GitHub Issues: https://github.com/your-username/product-recommender/issues
- Streamlit Docs: https://docs.streamlit.io
- OpenAI Docs: https://platform.openai.com/docs
