# AI Product Recommendation Agent - Architecture Diagram

## System Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE LAYER                              │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Streamlit Web Application                                           │  │
│  │  ├─ Search Input Component                                           │  │
│  │  ├─ Filter Sidebar (Budget, Category, Features)                      │  │
│  │  ├─ Product Display Cards                                            │  │
│  │  ├─ Chat History & Preferences                                       │  │
│  │  └─ Settings & Configuration Panel                                   │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└────────────┬─────────────────────────────────────────────────────┬─────────┘
             │                                                     │
             ▼                                                     ▼
┌─────────────────────────────┐                   ┌────────────────────────────┐
│   REQUEST PROCESSING         │                   │  CONFIGURATION LAYER       │
│                              │                   │                            │
│ ├─ Parse User Query          │                   │ ├─ API Keys Setup          │
│ ├─ Extract Search Term       │                   │ ├─ Model Selection         │
│ ├─ Apply User Preferences    │                   │ ├─ Thresholds & Limits     │
│ └─ Format Requests           │                   │ └─ Feature Flags           │
└────────────┬─────────────────┘                   └────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                    RECOMMENDATION ENGINE LAYER                             │
│                    (ProductRecommendationAgent)                            │
│                                                                            │
│  ┌──────────────────┐  ┌──────────────────┐  ┌────────────────────────┐   │
│  │ Preference       │  │ Product          │  │ Ranking &              │   │
│  │ Extraction       │  │ Filtering        │  │ Score Calculation      │   │
│  │                  │  │                  │  │                        │   │
│  │ • Budget         │  │ • Price Range    │  │ • Relevance Score      │   │
│  │ • Features       │  │ • Category       │  │ • Rating Boost         │   │
│  │ • Category       │  │ • Features       │  │ • Similarity Score     │   │
│  │ • Rating         │  │ • Ratings        │  │ • Tag Matching         │   │
│  └──────────────────┘  └──────────────────┘  └────────────────────────┘   │
│           │                    │                        │                 │
│           └────────────────────┼────────────────────────┘                 │
│                                ▼                                          │
│                    ┌──────────────────────────┐                           │
│                    │  LLM Integration Layer   │                           │
│                    │  (OpenAI/Claude)         │                           │
│                    │                          │                           │
│                    │ • Text Generation        │                           │
│                    │ • Query Understanding    │                           │
│                    │ • Recommendation Text    │                           │
│                    └──────────────────────────┘                           │
└─────┬──────────────────────────────────────────────────────────────────────┘
      │
      ├──────────────────────────────┬────────────────────────────┐
      │                              │                            │
      ▼                              ▼                            ▼
┌──────────────────────────┐   ┌─────────────────────┐   ┌──────────────────┐
│  VECTOR DATABASE LAYER   │   │  LLM API LAYER      │   │ DATA MANAGEMENT  │
│                          │   │                     │   │                  │
│ ChromaDB / FAISS         │   │ OpenAI GPT          │   │ Product Catalog  │
│                          │   │ - gpt-4o-mini       │   │ - Sample Data    │
│ ├─ Embeddings Store      │   │ - gpt-3.5-turbo     │   │ - Google Sheets  │
│ ├─ Similarity Search     │   │                     │   │ - Shopify API    │
│ ├─ Vector Indexing       │   │ Function:           │   │ - Firebase       │
│ └─ Retrieval             │   │ • Parse Preferences │   │                  │
│                          │   │ • Generate Text     │   │ Features:        │
│ Speed: O(log n)          │   │ • Score Products    │   │ • Real-time Sync │
│ Supports: Semantic       │   │                     │   │ • User Profiles  │
│           Search         │   │ Cost: ~$0.001/req   │   │ • Preferences    │
└──────────────────────────┘   └─────────────────────┘   └──────────────────┘
      │                              │                            │
      └──────────────┬───────────────┴────────────────────────────┘
                     │
                     ▼
         ┌──────────────────────────────┐
         │  RESPONSE AGGREGATION &      │
         │  FORMATTING                  │
         │                              │
         │ • Combine Results            │
         │ • Format for Display         │
         │ • Add Metadata               │
         │ • Store in History           │
         └──────────────────────────────┘
                     │
                     ▼
         ┌──────────────────────────────┐
         │  OUTPUT TO USER              │
         │                              │
         │ • Recommendation Text        │
         │ • Product Cards              │
         │ • Rankings                   │
         │ • Alternative Suggestions    │
         └──────────────────────────────┘
```

## Data Flow Diagram

```
USER INPUT
   │
   ▼
┌─────────────────────────────────────┐
│ 1. USER QUERY                       │
│ "wireless headphones under $200"    │
└─────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────┐
│ 2. PREFERENCE EXTRACTION            │
│ • Budget: $0-200                    │
│ • Features: wireless                │
│ • Category: None                    │
└─────────────────────────────────────┘
   │
   ├─────────────────────────┬────────────────────────┐
   │                         │                        │
   ▼                         ▼                        ▼
┌──────────────────┐  ┌─────────────────┐  ┌────────────────────┐
│ 3a. VECTOR SEARCH│  │ 3b. FILTER      │  │ 3c. LLM ANALYSIS   │
│                  │  │ PRODUCTS        │  │ (Optional)         │
│ Query to Vector  │  │                 │  │                    │
│ • Generate       │  │ Apply Budget    │  │ • Enhance under-   │
│   Embeddings     │  │ Apply Features  │  │   standing         │
│ • Search DB      │  │ Apply Category  │  │ • Extract nuance   │
│ • Get matches    │  │ • Return: 5     │  │ • Add context      │
│ • Score 0.7+     │  │   products      │  │                    │
└──────────────────┘  └─────────────────┘  └────────────────────┘
   │                         │                        │
   └─────────────────────────┼────────────────────────┘
                             │
                             ▼
              ┌────────────────────────────┐
              │ 4. PRODUCT RANKING         │
              │                            │
              │ Score = 0.75*semantic +    │
              │          0.1*rating +      │
              │          0.1*tag_match +   │
              │          0.05*price        │
              │                            │
              │ Result: Top 5 products     │
              │ sorted by relevance        │
              └────────────────────────────┘
                             │
                             ▼
              ┌────────────────────────────┐
              │ 5. RECOMMENDATION TEXT     │
              │ GENERATION                 │
              │                            │
              │ LLM Prompt:                │
              │ "Top 3 products are...     │
              │  These match because..."   │
              │                            │
              │ Output: Natural language   │
              │ explanation                │
              └────────────────────────────┘
                             │
                             ▼
              ┌────────────────────────────┐
              │ 6. RESPONSE OUTPUT         │
              │                            │
              │ • Recommendation text      │
              │ • Product cards            │
              │ • Prices & ratings         │
              │ • Alternative options      │
              └────────────────────────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │ DISPLAYED      │
                     │ TO USER        │
                     └────────────────┘
```

## Component Interaction Diagram

```
┌────────────────────────────────────────────────────────────┐
│                   STREAMLIT APP                            │
│                                                            │
│  app.py                                                    │
│  ├─ User Interface Components                              │
│  ├─ Session State Management                               │
│  ├─ Display Logic                                          │
│  └─ Interaction Handlers                                   │
└─────────────┬────────────────────────────────────────────┘
              │
              │ imports & uses
              │
              ▼
┌────────────────────────────────────────────────────────────┐
│              RECOMMENDATION AGENT                          │
│                                                            │
│  src/agents/recommendation_agent.py                        │
│  ├─ extract_preferences()                                  │
│  ├─ filter_products()                                      │
│  ├─ rank_products()                                        │
│  ├─ generate_recommendation_text()                         │
│  └─ add_to_history()                                       │
└─────────────┬────────────────┬────────────────────────────┘
              │                │
              │                │ imports & uses
              │                │
    imports & │                ▼
    uses      │         ┌──────────────────────────┐
              │         │  OpenAI API Client       │
              │         │                          │
              │         │  openai.ChatCompletion.  │
              │         │  create()                │
              │         └──────────────────────────┘
              │
              ▼
┌────────────────────────────────────────────────────────────┐
│              VECTOR DATABASE                               │
│                                                            │
│  src/vectors/db.py                                         │
│  ├─ VectorDatabase class                                   │
│  ├─ add_products()                                         │
│  ├─ search()                                               │
│  └─ get_all_products()                                     │
│                                                            │
│  Supports:                                                 │
│  ├─ ChromaDB backend                                       │
│  └─ FAISS backend                                          │
└──────────┬──────────────────────────────────────────────────┘
           │
           ├─────────────────────────┬──────────────────┐
           │                         │                  │
           ▼                         ▼                  ▼
    ┌──────────────┐         ┌──────────────┐   ┌────────────────┐
    │ ChromaDB     │         │ FAISS        │   │ Sentence-      │
    │ Library      │         │ Library      │   │ Transformers   │
    │              │         │              │   │                │
    │ • Collection │         │ • Index      │   │ • Encoder      │
    │ • Query      │         │ • Search     │   │ • Embeddings   │
    │ • Add        │         │ • Add        │   │ • Similarity   │
    └──────────────┘         └──────────────┘   └────────────────┘
```

## Request-Response Flow

```
1. USER SUBMITS QUERY
   "I want comfortable gaming headphones under $150"
                    │
                    ▼
2. STREAMLIT CAPTURES INPUT
   ├─ Query: string
   ├─ Filters: selected values
   └─ Settings: threshold, max results
                    │
                    ▼
3. AGENT PROCESSES
   ProductRecommendationAgent.extract_preferences()
   Returns:
   {
     "budget_max": 150,
     "features": ["comfortable", "gaming"],
     "categories": [],
     "rating_min": 0
   }
                    │
                    ├─────────────────┬──────────────────┐
                    │                 │                  │
                    ▼                 ▼                  ▼
4a. VECTOR SEARCH          4b. FILTER              4c. RANK
    VectorDB.search()      Products by            Products by
    • Get embeddings       • Budget               • Relevance
    • Find similar         • Features             • Rating
    • Return scores        • Category             • Score
                    │                 │                  │
                    └─────────────────┼──────────────────┘
                                      │
                                      ▼
5. COMBINE RESULTS
   Merge search results
   Apply filters
   Final ranking
                    │
                    ▼
6. GENERATE TEXT
   LLM Prompt: "Recommend these products..."
   LLM Response: Natural language recommendation
                    │
                    ▼
7. FORMAT OUTPUT
   ├─ Recommendation text
   ├─ Product cards
   └─ Metadata
                    │
                    ▼
8. DISPLAY IN UI
   ├─ Recommendation box
   ├─ Product listings
   └─ Chat history
                    │
                    ▼
9. STORE IN MEMORY
   Add to session history
   Update preferences
```

## Technology Stack Relationships

```
┌──────────────────────────────────────────────────────────────────┐
│                     USER FACING                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  Streamlit (Web Framework)                                 │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────┬───────────────────────────────────────┘
                           │
┌──────────────────────────┴───────────────────────────────────────┐
│                  APPLICATION LOGIC                              │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  Python (src/, config/)                                    │  │
│  │  ├─ ProductRecommendationAgent                             │  │
│  │  ├─ VectorDatabase                                         │  │
│  │  └─ Settings                                               │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────┬───────────────────────────────────────┘
                           │
    ┌──────────────────────┴──────────────────────┐
    │                                             │
┌───▼──────────────────┐           ┌─────────────▼────────────┐
│  ML & EMBEDDINGS      │           │   EXTERNAL APIs         │
│  ┌────────────────┐   │           │  ┌──────────────────┐   │
│  │ Sentence-      │   │           │  │  OpenAI GPT      │   │
│  │ Transformers   │   │           │  │  - GPT-4o-mini   │   │
│  │                │   │           │  │  - gpt-3.5-turbo │   │
│  │ • Embeddings   │   │           │  │                  │   │
│  │ • Similarity   │   │           │  │  Via HTTP API    │   │
│  └────────────────┘   │           │  └──────────────────┘   │
│                       │           │                         │
│ ┌────────────────┐    │           │  ┌──────────────────┐   │
│ │ Vector DB      │    │           │  │ Data Sources     │   │
│ │                │    │           │  │ (Optional)       │   │
│ │ ChromaDB/FAISS │    │           │  │ • Google Sheets  │   │
│ │                │    │           │  │ • Shopify        │   │
│ │ • Indexing     │    │           │  │ • Firebase       │   │
│ │ • Search       │    │           │  └──────────────────┘   │
│ └────────────────┘    │           │                         │
└───────────────────────┘           └─────────────────────────┘
```

## Deployment Architecture

```
┌────────────────────────────────────────────────────────────┐
│                  STREAMLIT CLOUD                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Your App Running on Streamlit Servers               │  │
│  │  ├─ app.py deployed                                  │  │
│  │  ├─ Dependencies installed                           │  │
│  │  └─ Environment variables set                        │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────┬─────────────────────────────┘
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
    ┌─────────────┐  ┌──────────┐  ┌──────────────┐
    │ External    │  │ Python   │  │ Static Files │
    │ APIs        │  │ Libraries│  │ & Assets     │
    │             │  │ (Cached) │  │              │
    │ OpenAI      │  │          │  │              │
    │ Shopify     │  │ Env Vars │  │              │
    │ Firebase    │  │ (Secure) │  │              │
    └─────────────┘  └──────────┘  └──────────────┘
```

---

This architecture is designed to be:
- **Scalable**: Can handle 100-10,000+ products
- **Maintainable**: Clean separation of concerns
- **Extensible**: Easy to add new data sources or LLM providers
- **Cost-Effective**: Uses efficient embeddings and minimal API calls
- **Production-Ready**: Error handling, logging, and caching built-in
