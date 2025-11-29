"""
Configuration settings for Product Recommendation Agent
"""
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"
LOG_DIR = PROJECT_ROOT / "logs"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
VECTOR_DB_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# LLM Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# Default LLM model
DEFAULT_LLM_MODEL = "gpt-4o-mini"  # Fast and cost-effective
BACKUP_LLM_MODEL = "gpt-3.5-turbo"

# Vector DB Configuration
VECTOR_DB_TYPE = "chroma"  # Options: "chroma", "faiss", "pinecone"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIM = 384

# Agent Configuration
MAX_RECOMMENDATIONS = 10
SIMILARITY_THRESHOLD = 0.3
SEARCH_TOP_K = 20

# Streamlit Configuration
STREAMLIT_PAGE_CONFIG = {
    "page_title": "AI Product Recommender",
    "page_icon": "🛍️",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Sample product data (200+ products across 15+ real-world categories)
SAMPLE_PRODUCTS = [
    # ELECTRONICS - Laptops (3)
    {"id": 1, "name": "MacBook Pro 16 inch", "category": "Electronics", "price": 2999.99, "description": "High-performance laptop with Apple M3 chip, perfect for professionals and creators", "tags": ["laptop", "portable", "professional", "powerful", "apple"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=MacBook"},
    {"id": 2, "name": "Dell XPS 15", "category": "Electronics", "price": 1999.99, "description": "Premium Windows laptop with powerful graphics and stunning display for work and gaming", "tags": ["laptop", "windows", "gaming", "professional"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Dell+XPS"},
    {"id": 3, "name": "Lenovo ThinkPad", "category": "Electronics", "price": 1299.99, "description": "Business laptop with excellent keyboard and battery life, ideal for professionals", "tags": ["laptop", "business", "portable", "keyboard"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=ThinkPad"},
    
    # ELECTRONICS - Headphones (3)
    {"id": 4, "name": "Sony WH-1000XM5 Wireless Headphones", "category": "Electronics", "price": 399.99, "description": "Premium wireless headphones with industry-leading noise cancellation and 30-hour battery", "tags": ["wireless", "headphones", "audio", "noise-cancelling", "premium"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=Sony+Headphones"},
    {"id": 5, "name": "Bose QuietComfort Headphones", "category": "Electronics", "price": 349.99, "description": "Comfortable noise-cancelling headphones with excellent sound quality and portability", "tags": ["wireless", "headphones", "audio", "noise-cancelling"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Bose+Headphones"},
    {"id": 6, "name": "JBL Flip Bluetooth Speaker", "category": "Electronics", "price": 129.99, "description": "Portable wireless speaker with great sound quality and water-resistant design", "tags": ["wireless", "speaker", "bluetooth", "portable", "waterproof"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=JBL+Speaker"},
    
    # ELECTRONICS - Monitors (3)
    {"id": 7, "name": "Dell UltraWide Gaming Monitor 38 inch", "category": "Electronics", "price": 1499.99, "description": "Curved ultrawide gaming monitor with 144Hz refresh rate and immersive display", "tags": ["monitor", "gaming", "ultrawide", "144hz", "curved"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=Dell+UltraWide"},
    {"id": 8, "name": "LG 4K Monitor 27 inch", "category": "Electronics", "price": 599.99, "description": "4K professional monitor with accurate color for designers and content creators", "tags": ["monitor", "4k", "professional", "designer", "color-accurate"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=LG+4K+Monitor"},
    {"id": 9, "name": "ASUS Gaming Monitor 144Hz", "category": "Electronics", "price": 349.99, "description": "High-refresh-rate gaming monitor with responsive display and adjustable stand", "tags": ["monitor", "gaming", "144hz", "responsive"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=ASUS+Gaming"},
    
    # FURNITURE - Chairs (4)
    {"id": 10, "name": "Herman Miller Aeron Office Chair", "category": "Furniture", "price": 1495.00, "description": "Premium ergonomic office chair with adjustable lumbar support and mesh back design", "tags": ["office", "chair", "ergonomic", "comfortable", "premium"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=Herman+Miller"},
    {"id": 11, "name": "Steelcase Leap Office Chair", "category": "Furniture", "price": 899.99, "description": "Professional ergonomic chair designed for extended computer work and comfort", "tags": ["office", "chair", "ergonomic", "professional"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Steelcase"},
    {"id": 12, "name": "IKEA Markus Gaming Chair", "category": "Furniture", "price": 199.99, "description": "Affordable gaming chair with high back and padded armrests for comfort", "tags": ["office", "chair", "gaming", "budget-friendly"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=IKEA+Gaming"},
    {"id": 13, "name": "Executive Leather Office Chair", "category": "Furniture", "price": 599.99, "description": "Comfortable leather chair with executive styling suitable for professional offices", "tags": ["office", "chair", "leather", "executive"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Leather+Chair"},
    
    # FURNITURE - Desks (4)
    {"id": 14, "name": "Fully Jarvis Standing Desk", "category": "Furniture", "price": 599.99, "description": "Electric standing desk with adjustable height for ergonomic work positions", "tags": ["office", "furniture", "desk", "standing", "electric"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Standing+Desk"},
    {"id": 15, "name": "Wooden Office Desk", "category": "Furniture", "price": 399.99, "description": "Spacious wooden desk with storage compartments for home and professional offices", "tags": ["office", "furniture", "desk", "wooden"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Wooden+Desk"},
    {"id": 16, "name": "Gaming Desk with LED Lights", "category": "Furniture", "price": 299.99, "description": "Modern gaming desk with RGB lighting and integrated cable management system", "tags": ["office", "furniture", "desk", "gaming", "led"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Gaming+Desk"},
    {"id": 17, "name": "Small Computer Desk", "category": "Furniture", "price": 149.99, "description": "Compact desk ideal for small spaces, apartments, and dorm rooms", "tags": ["office", "furniture", "desk", "compact", "budget"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Small+Desk"},
    
    # HOME - Lighting (3)
    {"id": 18, "name": "Philips Hue Smart Light Bulbs", "category": "Home", "price": 79.99, "description": "WiFi-enabled smart light bulbs with 16 million color options and voice control", "tags": ["smart", "home", "lights", "wifi", "color-changing"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Philips+Hue"},
    {"id": 19, "name": "LIFX Smart Bulbs Starter Kit", "category": "Home", "price": 49.99, "description": "WiFi smart bulbs that don't require a hub, easy setup and installation", "tags": ["smart", "home", "lights", "wifi", "budget"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=LIFX+Bulbs"},
    {"id": 20, "name": "Nanoleaf Modular Light Panels", "category": "Home", "price": 199.99, "description": "Modern modular LED light panels for creative room decoration and ambiance", "tags": ["smart", "home", "lights", "decorative", "rgb"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Nanoleaf"},
    
    # HOME - Accessories (2)
    {"id": 21, "name": "LED Desk Lamp", "category": "Home", "price": 39.99, "description": "Adjustable LED desk lamp with touch controls and USB charging port", "tags": ["lamp", "home", "desk", "led", "charging"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=LED+Lamp"},
    {"id": 22, "name": "Office Storage Cabinet", "category": "Furniture", "price": 199.99, "description": "Spacious cabinet with doors for organizing office supplies and documents", "tags": ["office", "furniture", "storage", "cabinet"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Storage+Cabinet"},
    
    # ELECTRONICS - Keyboards (4)
    {"id": 23, "name": "Corsair K95 Platinum Mechanical Keyboard", "category": "Electronics", "price": 229.99, "description": "Premium mechanical keyboard with Cherry MX switches and macro keys for gaming", "tags": ["keyboard", "mechanical", "gaming", "rgb", "premium"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Corsair+K95"},
    {"id": 24, "name": "Logitech MX Keys Wireless Keyboard", "category": "Electronics", "price": 99.99, "description": "Professional wireless keyboard with scissor switches and backlit keys", "tags": ["keyboard", "wireless", "professional", "typing"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Logitech+MX"},
    {"id": 25, "name": "Razer BlackWidow Elite Gaming Keyboard", "category": "Electronics", "price": 179.99, "description": "Gaming keyboard with Razer Green switches and programmable keys", "tags": ["keyboard", "gaming", "mechanical", "rgb"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Razer+BlackWidow"},
    {"id": 26, "name": "Budget Membrane Keyboard", "category": "Electronics", "price": 29.99, "description": "Affordable membrane keyboard with numeric keypad", "tags": ["keyboard", "budget", "typing"], "rating": 4.2, "image_url": "https://via.placeholder.com/300x300?text=Budget+Keyboard"},
    
    # ELECTRONICS - Mice (4)
    {"id": 27, "name": "Logitech MX Master 3S Mouse", "category": "Electronics", "price": 99.99, "description": "Premium ergonomic mouse with precision scrolling and multi-device connectivity", "tags": ["mouse", "wireless", "ergonomic", "professional"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=MX+Master"},
    {"id": 28, "name": "Razer DeathAdder Elite Gaming Mouse", "category": "Electronics", "price": 69.99, "description": "High-precision gaming mouse with 16,000 DPI sensor", "tags": ["mouse", "gaming", "wireless", "precision"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Razer+DeathAdder"},
    {"id": 29, "name": "SteelSeries Rival 3 Gaming Mouse", "category": "Electronics", "price": 49.99, "description": "Lightweight gaming mouse with responsive sensor and comfortable grip", "tags": ["mouse", "gaming", "lightweight"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=SteelSeries+Rival"},
    {"id": 30, "name": "Basic Wired Mouse", "category": "Electronics", "price": 19.99, "description": "Simple wired mouse for everyday computing", "tags": ["mouse", "wired", "budget"], "rating": 4.0, "image_url": "https://via.placeholder.com/300x300?text=Basic+Mouse"},
    
    # ELECTRONICS - Tablets & Accessories (4)
    {"id": 31, "name": "iPad Pro 12.9 inch", "category": "Electronics", "price": 1099.99, "description": "Premium tablet with M2 chip and stunning Liquid Retina display", "tags": ["tablet", "ipad", "portable", "apple", "professional"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=iPad+Pro"},
    {"id": 32, "name": "Samsung Galaxy Tab S9", "category": "Electronics", "price": 799.99, "description": "Android tablet with 120Hz AMOLED display and powerful processor", "tags": ["tablet", "android", "portable", "gaming"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Galaxy+Tab"},
    {"id": 33, "name": "Microsoft Surface Go", "category": "Electronics", "price": 399.99, "description": "Portable 2-in-1 tablet with Windows 11 and kickstand", "tags": ["tablet", "windows", "portable", "2-in-1"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Surface+Go"},
    {"id": 34, "name": "Apple Pencil Pro", "category": "Electronics", "price": 129.99, "description": "Advanced stylus for iPad with precision and pressure sensitivity", "tags": ["stylus", "ipad", "accessories", "professional"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Apple+Pencil"},
    
    # ELECTRONICS - Webcams & Cameras (3)
    {"id": 35, "name": "Logitech C920 Pro Webcam", "category": "Electronics", "price": 79.99, "description": "1080p HD webcam with auto-focus and noise-reducing microphone", "tags": ["webcam", "streaming", "video", "professional"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Logitech+C920"},
    {"id": 36, "name": "4K USB Webcam", "category": "Electronics", "price": 149.99, "description": "Ultra HD 4K webcam for professional streaming and video calls", "tags": ["webcam", "4k", "streaming", "professional"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=4K+Webcam"},
    {"id": 37, "name": "Mirrorless Camera Sony A6400", "category": "Electronics", "price": 899.99, "description": "Compact mirrorless camera with fast autofocus and 4K video recording", "tags": ["camera", "sony", "professional", "4k", "photography"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=Sony+A6400"},
    
    # ELECTRONICS - Phone Accessories (3)
    {"id": 38, "name": "Anker PowerCore 26800mAh Power Bank", "category": "Electronics", "price": 59.99, "description": "High-capacity portable charger with dual USB ports and LED display", "tags": ["powerbank", "charger", "portable", "mobile"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Anker+PowerBank"},
    {"id": 39, "name": "iPhone 15 Pro Magnetic Case", "category": "Electronics", "price": 39.99, "description": "Premium protective case with MagSafe charging support", "tags": ["case", "iphone", "protection", "magsafe"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=iPhone+Case"},
    {"id": 40, "name": "USB-C Fast Charger 65W", "category": "Electronics", "price": 29.99, "description": "Multi-port fast charger compatible with laptops and phones", "tags": ["charger", "usb-c", "fast-charging"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=USB+C+Charger"},
    
    # FURNITURE - Filing & Organization (4)
    {"id": 41, "name": "5-Drawer File Cabinet", "category": "Furniture", "price": 299.99, "description": "Metal file cabinet with locks for secure document storage", "tags": ["office", "storage", "filing", "cabinet"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=File+Cabinet"},
    {"id": 42, "name": "Shelving Unit 5-Tier", "category": "Furniture", "price": 129.99, "description": "Industrial style metal shelving for storage and organization", "tags": ["storage", "shelving", "industrial", "organization"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Shelving"},
    {"id": 43, "name": "Mobile Pedestal Filing Cabinet", "category": "Furniture", "price": 179.99, "description": "Compact filing cabinet on wheels that fits under desks", "tags": ["office", "filing", "storage", "mobile"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Mobile+Pedestal"},
    {"id": 44, "name": "Desk Organizer Set", "category": "Furniture", "price": 49.99, "description": "Multiple compartments for pens, papers, and desk accessories", "tags": ["organization", "desk", "accessories", "storage"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Desk+Organizer"},
    
    # FURNITURE - Shelving & Racks (3)
    {"id": 45, "name": "Gaming Monitor Stand Riser", "category": "Furniture", "price": 49.99, "description": "Elevated monitor stand with storage space underneath", "tags": ["desk", "stand", "storage", "gaming"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Monitor+Stand"},
    {"id": 46, "name": "Wall-Mounted Shelves Set", "category": "Furniture", "price": 79.99, "description": "Floating shelves for modern home and office decoration", "tags": ["shelves", "wall-mounted", "storage", "home"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Wall+Shelves"},
    {"id": 47, "name": "Corner Desk Shelf", "category": "Furniture", "price": 89.99, "description": "Space-saving corner shelf perfect for small offices", "tags": ["desk", "shelf", "corner", "compact"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Corner+Shelf"},
    
    # FURNITURE - Tables (4)
    {"id": 48, "name": "Glass Conference Table 8-Seat", "category": "Furniture", "price": 799.99, "description": "Modern glass conference table for meeting rooms", "tags": ["table", "conference", "office", "professional"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Conference+Table"},
    {"id": 49, "name": "Adjustable Height Cafe Table", "category": "Furniture", "price": 249.99, "description": "Modern cafe table with adjustable legs for different heights", "tags": ["table", "cafe", "adjustable"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Cafe+Table"},
    {"id": 50, "name": "Coffee Table", "category": "Furniture", "price": 199.99, "description": "Stylish wooden coffee table with storage drawer", "tags": ["table", "coffee", "living-room", "wooden"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Coffee+Table"},
    {"id": 51, "name": "Gaming Desk with Cable Management", "category": "Furniture", "price": 329.99, "description": "Large gaming desk with integrated cable management system", "tags": ["desk", "gaming", "large", "organization"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Gaming+Desk+Large"},
    
    # HOME - Smart Home Devices (5)
    {"id": 52, "name": "Amazon Echo Dot 5th Gen", "category": "Home", "price": 49.99, "description": "Compact smart speaker with Alexa voice assistant", "tags": ["smart-speaker", "alexa", "voice-control", "home"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Echo+Dot"},
    {"id": 53, "name": "Google Nest Mini", "category": "Home", "price": 39.99, "description": "Compact smart speaker with Google Assistant integration", "tags": ["smart-speaker", "google", "voice-control", "home"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Nest+Mini"},
    {"id": 54, "name": "Smart WiFi Door Lock", "category": "Home", "price": 199.99, "description": "Smart lock with keyless entry and smartphone control", "tags": ["smart-lock", "security", "wifi", "home"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Smart+Lock"},
    {"id": 55, "name": "Smart Thermostat", "category": "Home", "price": 249.99, "description": "Programmable thermostat with remote control and learning features", "tags": ["thermostat", "smart", "temperature", "energy-saving"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Smart+Thermostat"},
    {"id": 56, "name": "Smart Plug Outlet", "category": "Home", "price": 24.99, "description": "WiFi smart plug to control any device remotely", "tags": ["smart-plug", "outlet", "wifi", "automation"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Smart+Plug"},
    
    # HOME - Air Quality & Comfort (4)
    {"id": 57, "name": "Air Purifier HEPA Filter", "category": "Home", "price": 149.99, "description": "Quiet air purifier with HEPA filter for allergen removal", "tags": ["air-purifier", "health", "filter", "home"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Air+Purifier"},
    {"id": 58, "name": "Humidifier Ultrasonic", "category": "Home", "price": 79.99, "description": "Quiet ultrasonic humidifier with essential oil diffuser", "tags": ["humidifier", "health", "aroma", "home"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Humidifier"},
    {"id": 59, "name": "White Noise Machine", "category": "Home", "price": 49.99, "description": "Sound machine for sleep with multiple noise options", "tags": ["sound-machine", "sleep", "relaxation", "home"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=White+Noise"},
    {"id": 60, "name": "Smart Air Purifier with App", "category": "Home", "price": 299.99, "description": "Premium air purifier with WiFi control and air quality monitoring", "tags": ["air-purifier", "smart", "app-control", "premium"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Smart+Air+Purifier"},
    
    # HOME - Decor & Lighting (5)
    {"id": 61, "name": "Desk Plant with LED Light", "category": "Home", "price": 34.99, "description": "Decorative plant with integrated LED grow light", "tags": ["plant", "light", "decor", "desktop"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Plant+Light"},
    {"id": 62, "name": "RGB Corner Light Lamp", "category": "Home", "price": 69.99, "description": "Tall corner lamp with RGB color-changing light", "tags": ["lamp", "rgb", "corner", "ambiance"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Corner+RGB"},
    {"id": 63, "name": "Wall Art Canvas Set", "category": "Home", "price": 59.99, "description": "Set of 3 decorative canvas art pieces for home", "tags": ["art", "wall-decor", "canvas", "home"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Canvas+Art"},
    {"id": 64, "name": "Desk Organizer with Pen Holder", "category": "Home", "price": 19.99, "description": "Wooden desk organizer for pens, papers, and small items", "tags": ["organizer", "desk", "storage", "decor"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Wood+Organizer"},
    {"id": 65, "name": "Motivational Wall Posters Pack", "category": "Home", "price": 29.99, "description": "Set of inspirational posters for home and office", "tags": ["posters", "wall-decor", "motivation", "home"], "rating": 4.2, "image_url": "https://via.placeholder.com/300x300?text=Posters"},
    
    # HOME - Cleaning & Organization (4)
    {"id": 66, "name": "Desk Cable Organizer Kit", "category": "Home", "price": 19.99, "description": "Cable clips and ties for organizing desk cables", "tags": ["organization", "cables", "desk", "accessories"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Cable+Organizer"},
    {"id": 67, "name": "Drawer Divider Organizer", "category": "Home", "price": 24.99, "description": "Adjustable drawer dividers for organizing office supplies", "tags": ["organization", "drawers", "storage"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Drawer+Divider"},
    {"id": 68, "name": "Dust Cover for Electronics", "category": "Home", "price": 14.99, "description": "Protective dust covers for monitors and devices", "tags": ["dust-cover", "protection", "electronics"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Dust+Cover"},
    {"id": 69, "name": "Document Holder Stand", "category": "Home", "price": 19.99, "description": "Adjustable document holder for desk and office use", "tags": ["holder", "document", "desk", "organization"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Document+Holder"},
    
    # ELECTRONICS - Network & Connectivity (3)
    {"id": 70, "name": "WiFi 6 Router TP-Link", "category": "Electronics", "price": 149.99, "description": "High-speed WiFi 6 router with excellent coverage", "tags": ["router", "wifi", "network", "high-speed"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=WiFi+Router"},
    {"id": 71, "name": "Network Switch 16-Port Gigabit", "category": "Electronics", "price": 99.99, "description": "Enterprise-grade network switch for office connectivity", "tags": ["switch", "network", "ethernet", "office"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Network+Switch"},
    {"id": 72, "name": "USB Hub Multi-Port 7-in-1", "category": "Electronics", "price": 39.99, "description": "Portable USB hub with multiple ports and fast data transfer", "tags": ["usb-hub", "connectivity", "portable", "accessories"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=USB+Hub"},
    
    # SHOES - Running (4)
    {"id": 73, "name": "Nike Air Zoom Pegasus", "category": "Shoes", "price": 129.99, "description": "Lightweight running shoes with responsive cushioning for everyday running", "tags": ["running", "nike", "lightweight", "cushioning"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Nike+Pegasus"},
    {"id": 74, "name": "Adidas Ultraboost 22", "category": "Shoes", "price": 199.99, "description": "Premium running shoes with Boost technology and energy return", "tags": ["running", "adidas", "premium", "cushioning"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Adidas+Ultraboost"},
    {"id": 75, "name": "New Balance 990v6", "category": "Shoes", "price": 249.99, "description": "Iconic running shoe with superior comfort and stability", "tags": ["running", "new-balance", "comfort", "stability"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=New+Balance+990"},
    {"id": 76, "name": "Brooks Ghost 15", "category": "Shoes", "price": 149.99, "description": "Versatile running shoe with smooth transitions and cushioning", "tags": ["running", "brooks", "versatile", "neutral"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Brooks+Ghost"},
    
    # SHOES - Casual (4)
    {"id": 77, "name": "Converse Chuck Taylor High Top", "category": "Shoes", "price": 59.99, "description": "Classic casual high-top sneaker in various colors", "tags": ["casual", "converse", "vintage", "budget"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Chuck+Taylor"},
    {"id": 78, "name": "Vans Old Skool", "category": "Shoes", "price": 69.99, "description": "Iconic skate shoe with durable canvas and timeless design", "tags": ["casual", "vans", "skate", "durable"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Vans+Old+Skool"},
    {"id": 79, "name": "Adidas Stan Smith", "category": "Shoes", "price": 89.99, "description": "Classic minimalist sneaker with clean white leather design", "tags": ["casual", "adidas", "minimalist", "white"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Stan+Smith"},
    {"id": 80, "name": "Puma Rs-X", "category": "Shoes", "price": 99.99, "description": "Retro-inspired casual shoe with modern comfort", "tags": ["casual", "puma", "retro", "comfort"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Puma+RS-X"},
    
    # SHOES - Sports (4)
    {"id": 81, "name": "Nike Lebron 21", "category": "Shoes", "price": 199.99, "description": "Premium basketball shoe with ankle support and responsive cushioning", "tags": ["basketball", "nike", "sports", "support"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Nike+Lebron"},
    {"id": 82, "name": "Adidas Dame Cert", "category": "Shoes", "price": 149.99, "description": "Basketball shoe designed for quick cuts and lateral support", "tags": ["basketball", "adidas", "sports", "lateral"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Adidas+Dame"},
    {"id": 83, "name": "Nike Metcon 9", "category": "Shoes", "price": 179.99, "description": "Training shoe for crossfit and gym workouts with stability", "tags": ["training", "crossfit", "gym", "stability"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Nike+Metcon"},
    {"id": 84, "name": "Asics Gel-Kayano", "category": "Shoes", "price": 169.99, "description": "Cushioned training shoe for intensive gym sessions", "tags": ["training", "asics", "cushioned", "gym"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Asics+Gel"},
    
    # SHOES - Formal (3)
    {"id": 85, "name": "Cole Haan Oxford Dress Shoes", "category": "Shoes", "price": 249.99, "description": "Premium leather dress shoes with comfort technology", "tags": ["formal", "dress", "leather", "premium"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Cole+Haan+Oxford"},
    {"id": 86, "name": "Allen Edmonds Loafers", "category": "Shoes", "price": 279.99, "description": "Handcrafted leather loafers for professional occasions", "tags": ["formal", "dress", "leather", "handcrafted"], "rating": 4.9, "image_url": "https://via.placeholder.com/300x300?text=Allen+Edmonds"},
    {"id": 87, "name": "Budget Dress Shoes", "category": "Shoes", "price": 89.99, "description": "Affordable formal shoes for business casual attire", "tags": ["formal", "dress", "budget", "business"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Budget+Dress"},
    
    # SHOES - Budget (4)
    {"id": 88, "name": "Walmart Basic Sneaker", "category": "Shoes", "price": 39.99, "description": "Affordable everyday sneaker for casual wear", "tags": ["casual", "budget", "everyday"], "rating": 4.1, "image_url": "https://via.placeholder.com/300x300?text=Basic+Sneaker"},
    {"id": 89, "name": "Target Athletic Shoes", "category": "Shoes", "price": 49.99, "description": "Budget-friendly athletic shoes for light activities", "tags": ["athletic", "budget", "lightweight"], "rating": 4.2, "image_url": "https://via.placeholder.com/300x300?text=Target+Athletic"},
    {"id": 90, "name": "Amazon Basics Walking Shoes", "category": "Shoes", "price": 44.99, "description": "Comfortable walking shoes for everyday use", "tags": ["walking", "budget", "comfort"], "rating": 4.2, "image_url": "https://via.placeholder.com/300x300?text=Walking+Shoes"},
    {"id": 91, "name": "Payless Casual Loafers", "category": "Shoes", "price": 34.99, "description": "Casual loafers at budget-friendly price", "tags": ["casual", "loafers", "budget"], "rating": 4.0, "image_url": "https://via.placeholder.com/300x300?text=Casual+Loafers"},
    
    # CLOTHING - Men's (8)
    {"id": 92, "name": "Ralph Lauren Polo Shirt", "category": "Clothing", "price": 89.99, "description": "Classic cotton polo shirt available in multiple colors", "tags": ["casual", "polo", "cotton", "men"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Polo+Shirt"},
    {"id": 93, "name": "Levi's 501 Jeans", "category": "Clothing", "price": 79.99, "description": "Classic straight leg jeans - American iconic style", "tags": ["jeans", "casual", "men", "durable"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Levis+Jeans"},
    {"id": 94, "name": "Tommy Hilfiger Oxford Button-Down", "category": "Clothing", "price": 69.99, "description": "Business casual button-down shirt for office", "tags": ["business", "casual", "button-down", "men"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Oxford+Shirt"},
    {"id": 95, "name": "Nike Dri-FIT T-Shirt", "category": "Clothing", "price": 34.99, "description": "Moisture-wicking athletic t-shirt for workouts", "tags": ["sports", "athletic", "moisture-wicking", "men"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Nike+Tshirt"},
    {"id": 96, "name": "Adidas Track Pants", "category": "Clothing", "price": 59.99, "description": "Comfortable athletic track pants for gym and casual", "tags": ["sports", "athletic", "comfortable", "men"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Track+Pants"},
    {"id": 97, "name": "Calvin Klein Boxer Briefs", "category": "Clothing", "price": 24.99, "description": "Premium underwear with superior comfort", "tags": ["underwear", "comfortable", "premium", "men"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Boxer+Briefs"},
    {"id": 98, "name": "The North Face Fleece Jacket", "category": "Clothing", "price": 129.99, "description": "Warm fleece jacket for outdoor activities", "tags": ["jacket", "outdoor", "warm", "fleece"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Fleece+Jacket"},
    {"id": 99, "name": "Banana Republic Chino Pants", "category": "Clothing", "price": 89.99, "description": "Business casual chino pants for work and outings", "tags": ["pants", "business", "casual", "chino"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Chino+Pants"},
    
    # CLOTHING - Women's (8)
    {"id": 100, "name": "Victoria's Secret Sports Bra", "category": "Clothing", "price": 49.99, "description": "Comfortable sports bra for active lifestyle", "tags": ["sports", "bra", "comfortable", "women"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Sports+Bra"},
    {"id": 101, "name": "Lululemon Align Yoga Pants", "category": "Clothing", "price": 128.00, "description": "Premium yoga pants with superior comfort", "tags": ["yoga", "pants", "premium", "women"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Yoga+Pants"},
    {"id": 102, "name": "Forever 21 Casual Dress", "category": "Clothing", "price": 29.99, "description": "Trendy casual dress for everyday wear", "tags": ["dress", "casual", "trendy", "women"], "rating": 4.2, "image_url": "https://via.placeholder.com/300x300?text=Casual+Dress"},
    {"id": 103, "name": "H&M Sweater", "category": "Clothing", "price": 39.99, "description": "Cozy sweater for cold weather", "tags": ["sweater", "warm", "casual", "women"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Sweater"},
    {"id": 104, "name": "Gap Skinny Jeans", "category": "Clothing", "price": 74.99, "description": "Flattering skinny jeans for casual style", "tags": ["jeans", "casual", "skinny", "women"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Skinny+Jeans"},
    {"id": 105, "name": "Zara Formal Blouse", "category": "Clothing", "price": 79.99, "description": "Elegant formal blouse for business occasions", "tags": ["blouse", "formal", "business", "women"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Formal+Blouse"},
    {"id": 106, "name": "Uniqlo Heattech Leggings", "category": "Clothing", "price": 34.99, "description": "Thermal leggings for winter comfort", "tags": ["leggings", "warm", "thermal", "women"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Heattech+Leggings"},
    {"id": 107, "name": "Mango Casual T-Shirt", "category": "Clothing", "price": 29.99, "description": "Simple casual t-shirt in multiple colors", "tags": ["tshirt", "casual", "women"], "rating": 4.2, "image_url": "https://via.placeholder.com/300x300?text=Tshirt"},
    
    # BEAUTY & PERSONAL CARE (10)
    {"id": 108, "name": "Maybelline Mascara", "category": "Beauty", "price": 7.99, "description": "Long-lasting volumizing mascara", "tags": ["cosmetics", "mascara", "makeup", "budget"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Mascara"},
    {"id": 109, "name": "Shiseido Premium Serum", "category": "Beauty", "price": 89.99, "description": "Anti-aging serum with premium ingredients", "tags": ["skincare", "anti-aging", "premium", "serum"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Premium+Serum"},
    {"id": 110, "name": "Olay Moisturizer", "category": "Beauty", "price": 24.99, "description": "Daily moisturizer for all skin types", "tags": ["skincare", "moisturizer", "budget"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Moisturizer"},
    {"id": 111, "name": "MAC Lipstick", "category": "Beauty", "price": 17.99, "description": "Professional grade lipstick in various shades", "tags": ["cosmetics", "lipstick", "makeup"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Lipstick"},
    {"id": 112, "name": "Clinique Face Wash", "category": "Beauty", "price": 19.99, "description": "Gentle face wash for daily use", "tags": ["skincare", "face-wash", "gentle"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Face+Wash"},
    {"id": 113, "name": "Gillette Razor", "category": "Beauty", "price": 9.99, "description": "Comfortable razor for smooth shaving", "tags": ["shaving", "razor", "grooming"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Razor"},
    {"id": 114, "name": "Colgate Toothpaste", "category": "Beauty", "price": 3.99, "description": "Cavity protection toothpaste", "tags": ["oral-care", "toothpaste", "budget"], "rating": 4.2, "image_url": "https://via.placeholder.com/300x300?text=Toothpaste"},
    {"id": 115, "name": "Dove Deodorant", "category": "Beauty", "price": 4.99, "description": "Long-lasting deodorant protection", "tags": ["deodorant", "grooming", "budget"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Deodorant"},
    {"id": 116, "name": "Neutrogena Sunscreen SPF 50", "category": "Beauty", "price": 8.99, "description": "High SPF protection against UV rays", "tags": ["sunscreen", "protection", "skincare"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Sunscreen"},
    {"id": 117, "name": "Dyson Hair Dryer", "category": "Beauty", "price": 399.99, "description": "Premium ionic hair dryer for fast drying", "tags": ["hair-dryer", "premium", "grooming"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Hair+Dryer"},
    
    # SPORTS & OUTDOORS (10)
    {"id": 118, "name": "Spalding Basketball", "category": "Sports", "price": 59.99, "description": "Official NBA basketball for games and practice", "tags": ["basketball", "sports", "outdoor"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Basketball"},
    {"id": 119, "name": "Wilson Tennis Racket", "category": "Sports", "price": 129.99, "description": "Professional grade tennis racket", "tags": ["tennis", "racket", "sports"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Tennis+Racket"},
    {"id": 120, "name": "Yoga Mat", "category": "Sports", "price": 34.99, "description": "Non-slip yoga mat for exercise", "tags": ["yoga", "fitness", "mat"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Yoga+Mat"},
    {"id": 121, "name": "Dumbbells Set", "category": "Sports", "price": 79.99, "description": "Adjustable dumbbells for home gym", "tags": ["weights", "fitness", "gym"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Dumbbells"},
    {"id": 122, "name": "Bicycle Mountain Bike", "category": "Sports", "price": 399.99, "description": "Off-road mountain bike for trails", "tags": ["bike", "mountain", "outdoor"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Mountain+Bike"},
    {"id": 123, "name": "Fishing Rod & Reel", "category": "Sports", "price": 79.99, "description": "Complete fishing setup for beginners", "tags": ["fishing", "outdoor", "recreation"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Fishing+Rod"},
    {"id": 124, "name": "Tent Camping 4-Person", "category": "Sports", "price": 149.99, "description": "Waterproof tent for camping adventures", "tags": ["camping", "tent", "outdoor"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Camping+Tent"},
    {"id": 125, "name": "Skateboard", "category": "Sports", "price": 69.99, "description": "Complete skateboard for tricks and cruising", "tags": ["skateboard", "sports", "recreation"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Skateboard"},
    {"id": 126, "name": "Soccer Ball", "category": "Sports", "price": 24.99, "description": "Official size soccer ball for games", "tags": ["soccer", "ball", "sports"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Soccer+Ball"},
    {"id": 127, "name": "Gym Bag", "category": "Sports", "price": 49.99, "description": "Spacious gym bag with compartments", "tags": ["gym", "bag", "sports"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Gym+Bag"},
    
    # KITCHEN & APPLIANCES (12)
    {"id": 128, "name": "Ninja Blender", "category": "Kitchen", "price": 89.99, "description": "High-power blender for smoothies and soups", "tags": ["blender", "kitchen", "appliance"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Blender"},
    {"id": 129, "name": "Instant Pot Pressure Cooker", "category": "Kitchen", "price": 79.99, "description": "Multi-function pressure cooker for fast cooking", "tags": ["pressure-cooker", "kitchen", "appliance"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Instant+Pot"},
    {"id": 130, "name": "Cuisinart Coffee Maker", "category": "Kitchen", "price": 49.99, "description": "Programmable coffee maker for morning brew", "tags": ["coffee-maker", "kitchen", "appliance"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Coffee+Maker"},
    {"id": 131, "name": "KitchenAid Mixer", "category": "Kitchen", "price": 199.99, "description": "Professional stand mixer for baking", "tags": ["mixer", "kitchen", "baking"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Stand+Mixer"},
    {"id": 132, "name": "Microwave Oven", "category": "Kitchen", "price": 99.99, "description": "Countertop microwave with multiple settings", "tags": ["microwave", "kitchen", "appliance"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Microwave"},
    {"id": 133, "name": "Toaster Oven", "category": "Kitchen", "price": 69.99, "description": "Compact toaster oven for quick meals", "tags": ["oven", "kitchen", "appliance"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Toaster+Oven"},
    {"id": 134, "name": "Dishwasher", "category": "Kitchen", "price": 399.99, "description": "Energy-efficient dishwasher for home", "tags": ["dishwasher", "kitchen", "appliance"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Dishwasher"},
    {"id": 135, "name": "Refrigerator Stainless Steel", "category": "Kitchen", "price": 899.99, "description": "Large capacity refrigerator with freezer", "tags": ["refrigerator", "kitchen", "large"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Refrigerator"},
    {"id": 136, "name": "Cooking Pot Set", "category": "Kitchen", "price": 79.99, "description": "Non-stick cookware set with lids", "tags": ["cookware", "kitchen", "non-stick"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Cookware+Set"},
    {"id": 137, "name": "Knife Set", "category": "Kitchen", "price": 99.99, "description": "Professional chef knife set", "tags": ["knives", "kitchen", "professional"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Knife+Set"},
    {"id": 138, "name": "Cutting Board", "category": "Kitchen", "price": 24.99, "description": "Large bamboo cutting board", "tags": ["cutting-board", "kitchen", "eco"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Cutting+Board"},
    {"id": 139, "name": "Vacuum Sealer", "category": "Kitchen", "price": 59.99, "description": "Food vacuum sealer for storage", "tags": ["sealer", "kitchen", "food-storage"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Vacuum+Sealer"},
    
    # BOOKS (8)
    {"id": 140, "name": "The Great Gatsby", "category": "Books", "price": 9.99, "description": "Classic American novel by F. Scott Fitzgerald", "tags": ["fiction", "classic", "novel"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Great+Gatsby"},
    {"id": 141, "name": "Atomic Habits", "category": "Books", "price": 14.99, "description": "Self-help book on building better habits", "tags": ["self-help", "productivity", "non-fiction"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Atomic+Habits"},
    {"id": 142, "name": "To Kill a Mockingbird", "category": "Books", "price": 9.99, "description": "Pulitzer Prize-winning novel about justice", "tags": ["fiction", "classic", "drama"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Mockingbird"},
    {"id": 143, "name": "Educated", "category": "Books", "price": 16.99, "description": "Memoir about education and family", "tags": ["memoir", "biography", "non-fiction"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Educated"},
    {"id": 144, "name": "The Lean Startup", "category": "Books", "price": 15.99, "description": "Business book on entrepreneurship", "tags": ["business", "startup", "non-fiction"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Lean+Startup"},
    {"id": 145, "name": "1984", "category": "Books", "price": 11.99, "description": "Dystopian novel by George Orwell", "tags": ["fiction", "science-fiction", "classic"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=1984"},
    {"id": 146, "name": "Thinking, Fast and Slow", "category": "Books", "price": 17.99, "description": "Psychology book about human decision-making", "tags": ["psychology", "non-fiction", "science"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=Thinking+Fast"},
    {"id": 147, "name": "The Hobbit", "category": "Books", "price": 12.99, "description": "Fantasy adventure by J.R.R. Tolkien", "tags": ["fantasy", "adventure", "fiction"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Hobbit"},
    
    # TOYS & GAMES (10)
    {"id": 148, "name": "LEGO Creator Set", "category": "Toys", "price": 39.99, "description": "Creative LEGO building set for all ages", "tags": ["lego", "toy", "building"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=LEGO+Set"},
    {"id": 149, "name": "Monopoly Board Game", "category": "Toys", "price": 19.99, "description": "Classic family board game", "tags": ["board-game", "family", "game"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Monopoly"},
    {"id": 150, "name": "PlayStation 5", "category": "Toys", "price": 499.99, "description": "Next-gen gaming console with 4K capability", "tags": ["gaming", "console", "video-game"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=PS5"},
    {"id": 151, "name": "Xbox Series X", "category": "Toys", "price": 499.99, "description": "Microsoft's premium gaming console", "tags": ["gaming", "console", "video-game"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Xbox+Series+X"},
    {"id": 152, "name": "Rubik's Cube", "category": "Toys", "price": 6.99, "description": "Classic 3D puzzle toy", "tags": ["puzzle", "toy", "brain-teaser"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Rubiks+Cube"},
    {"id": 153, "name": "Barbie Doll", "category": "Toys", "price": 19.99, "description": "Classic doll in fashionable outfit", "tags": ["doll", "toy", "collectible"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Barbie+Doll"},
    {"id": 154, "name": "Hot Wheels Car Set", "category": "Toys", "price": 14.99, "description": "Collection of die-cast toy cars", "tags": ["car", "toy", "collectible"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Hot+Wheels"},
    {"id": 155, "name": "Pokémon Card Booster Box", "category": "Toys", "price": 99.99, "description": "Collectible trading card game booster", "tags": ["cards", "collectible", "game"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Pokemon+Cards"},
    {"id": 156, "name": "Scrabble", "category": "Toys", "price": 16.99, "description": "Word-building board game for families", "tags": ["board-game", "word-game", "family"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Scrabble"},
    {"id": 157, "name": "Drone DJI Mavic", "category": "Toys", "price": 649.99, "description": "Professional grade drone with 4K camera", "tags": ["drone", "camera", "tech"], "rating": 4.7, "image_url": "https://via.placeholder.com/300x300?text=DJI+Drone"},
    
    # BABY & KIDS (8)
    {"id": 158, "name": "Baby Stroller", "category": "Baby", "price": 299.99, "description": "Lightweight and durable baby stroller", "tags": ["stroller", "baby", "travel"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Stroller"},
    {"id": 159, "name": "Baby Car Seat", "category": "Baby", "price": 199.99, "description": "Safety-certified infant car seat", "tags": ["car-seat", "baby", "safety"], "rating": 4.8, "image_url": "https://via.placeholder.com/300x300?text=Car+Seat"},
    {"id": 160, "name": "Baby Monitor Camera", "category": "Baby", "price": 79.99, "description": "Video monitor with night vision", "tags": ["monitor", "baby", "safety"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Baby+Monitor"},
    {"id": 161, "name": "Crib Bedding Set", "category": "Baby", "price": 49.99, "description": "Soft cotton crib bedding set", "tags": ["bedding", "baby", "sleep"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Crib+Bedding"},
    {"id": 162, "name": "Diaper Bag", "category": "Baby", "price": 59.99, "description": "Stylish diaper bag with multiple compartments", "tags": ["diaper-bag", "baby", "travel"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Diaper+Bag"},
    {"id": 163, "name": "Bottle Sterilizer", "category": "Baby", "price": 49.99, "description": "Electric sterilizer for baby bottles", "tags": ["sterilizer", "baby", "hygiene"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Sterilizer"},
    {"id": 164, "name": "Kids Bicycle", "category": "Baby", "price": 129.99, "description": "Training bike with stabilizer wheels", "tags": ["bicycle", "kids", "outdoor"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Kids+Bike"},
    {"id": 165, "name": "Learning Tablet for Kids", "category": "Baby", "price": 79.99, "description": "Educational tablet with parental controls", "tags": ["tablet", "educational", "kids"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Kids+Tablet"},
    
    # PET SUPPLIES (10)
    {"id": 166, "name": "Dog Bed Deluxe", "category": "Pets", "price": 79.99, "description": "Orthopedic dog bed for comfort", "tags": ["dog-bed", "pet", "comfort"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Dog+Bed"},
    {"id": 167, "name": "Cat Scratching Post", "category": "Pets", "price": 49.99, "description": "Tall scratching post with multiple levels", "tags": ["scratching-post", "cat", "pet"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Scratching+Post"},
    {"id": 168, "name": "Pet Food Bowl Set", "category": "Pets", "price": 19.99, "description": "Stainless steel bowls for food and water", "tags": ["bowl", "pet", "feeding"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Pet+Bowls"},
    {"id": 169, "name": "Dog Leash & Collar", "category": "Pets", "price": 29.99, "description": "Durable leash and collar set", "tags": ["leash", "collar", "dog", "pet"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Leash+Collar"},
    {"id": 170, "name": "Pet Crate", "category": "Pets", "price": 89.99, "description": "Portable pet crate for travel", "tags": ["crate", "pet", "travel"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Pet+Crate"},
    {"id": 171, "name": "Dog Toys Pack", "category": "Pets", "price": 24.99, "description": "Set of interactive toys for dogs", "tags": ["toys", "dog", "pet"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Dog+Toys"},
    {"id": 172, "name": "Cat Litter Box", "category": "Pets", "price": 34.99, "description": "Self-cleaning litter box", "tags": ["litter-box", "cat", "pet"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Litter+Box"},
    {"id": 173, "name": "Pet Grooming Kit", "category": "Pets", "price": 39.99, "description": "Complete grooming tools for pets", "tags": ["grooming", "pet", "tools"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Grooming+Kit"},
    {"id": 174, "name": "Fish Tank Aquarium", "category": "Pets", "price": 89.99, "description": "20-gallon aquarium with filter", "tags": ["aquarium", "fish", "pet"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Aquarium"},
    {"id": 175, "name": "Bird Cage", "category": "Pets", "price": 79.99, "description": "Large bird cage with perches", "tags": ["cage", "bird", "pet"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Bird+Cage"},
    
    # AUTOMOTIVE (8)
    {"id": 176, "name": "Car Floor Mats", "category": "Automotive", "price": 49.99, "description": "All-weather rubber floor mats", "tags": ["floor-mats", "car", "interior"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Floor+Mats"},
    {"id": 177, "name": "Car Seat Covers", "category": "Automotive", "price": 59.99, "description": "Protective seat covers for vehicle", "tags": ["seat-covers", "car", "protection"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Seat+Covers"},
    {"id": 178, "name": "Dashboard Camera", "category": "Automotive", "price": 129.99, "description": "1080P dashcam for vehicle security", "tags": ["dashcam", "car", "security"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Dashcam"},
    {"id": 179, "name": "Car Air Purifier", "category": "Automotive", "price": 34.99, "description": "Portable air purifier for vehicles", "tags": ["air-purifier", "car", "health"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Air+Purifier"},
    {"id": 180, "name": "Car Phone Mount", "category": "Automotive", "price": 19.99, "description": "Magnetic phone holder for dashboard", "tags": ["phone-mount", "car", "accessories"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Phone+Mount"},
    {"id": 181, "name": "Jump Starter Battery", "category": "Automotive", "price": 79.99, "description": "Portable jump starter for vehicles", "tags": ["jump-starter", "car", "emergency"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Jump+Starter"},
    {"id": 182, "name": "Car Vacuum Cleaner", "category": "Automotive", "price": 49.99, "description": "Portable vacuum cleaner for cars", "tags": ["vacuum", "car", "cleaning"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Car+Vacuum"},
    {"id": 183, "name": "Car Wax Kit", "category": "Automotive", "price": 29.99, "description": "Complete car detailing wax kit", "tags": ["wax", "car", "detailing"], "rating": 4.2, "image_url": "https://via.placeholder.com/300x300?text=Wax+Kit"},
    
    # HEALTH & FITNESS (8)
    {"id": 184, "name": "Treadmill Electric", "category": "Fitness", "price": 399.99, "description": "Programmable electric treadmill", "tags": ["treadmill", "fitness", "cardio"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Treadmill"},
    {"id": 185, "name": "Exercise Bike", "category": "Fitness", "price": 299.99, "description": "Stationary exercise bike for home gym", "tags": ["bike", "fitness", "cardio"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Exercise+Bike"},
    {"id": 186, "name": "Rowing Machine", "category": "Fitness", "price": 349.99, "description": "Full-body rowing machine", "tags": ["rowing-machine", "fitness", "workout"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Rowing+Machine"},
    {"id": 187, "name": "Blood Pressure Monitor", "category": "Health", "price": 39.99, "description": "Digital blood pressure monitor", "tags": ["health", "medical", "monitoring"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=BP+Monitor"},
    {"id": 188, "name": "Smart Scale", "category": "Health", "price": 49.99, "description": "WiFi enabled smart weighing scale", "tags": ["scale", "health", "fitness"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Smart+Scale"},
    {"id": 189, "name": "Resistance Bands Set", "category": "Fitness", "price": 24.99, "description": "Multiple resistance bands for workouts", "tags": ["resistance-bands", "fitness", "training"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Resistance+Bands"},
    {"id": 190, "name": "Massage Gun", "category": "Health", "price": 129.99, "description": "Electric massage gun for muscle recovery", "tags": ["massage", "recovery", "health"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Massage+Gun"},
    {"id": 191, "name": "Foam Roller", "category": "Fitness", "price": 29.99, "description": "Foam roller for muscle recovery", "tags": ["foam-roller", "fitness", "recovery"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Foam+Roller"},
    
    # TRAVEL & LUGGAGE (8)
    {"id": 192, "name": "Carry-On Luggage", "category": "Travel", "price": 79.99, "description": "Lightweight carry-on suitcase", "tags": ["luggage", "travel", "lightweight"], "rating": 4.5, "image_url": "https://via.placeholder.com/300x300?text=Carry+On"},
    {"id": 193, "name": "Travel Backpack", "category": "Travel", "price": 89.99, "description": "Spacious travel backpack with compartments", "tags": ["backpack", "travel", "organizing"], "rating": 4.6, "image_url": "https://via.placeholder.com/300x300?text=Travel+Backpack"},
    {"id": 194, "name": "Passport Holder", "category": "Travel", "price": 14.99, "description": "RFID blocking passport holder", "tags": ["passport", "travel", "security"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Passport+Holder"},
    {"id": 195, "name": "Travel Pillow", "category": "Travel", "price": 19.99, "description": "Memory foam neck travel pillow", "tags": ["pillow", "travel", "comfort"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Travel+Pillow"},
    {"id": 196, "name": "Luggage Lock", "category": "Travel", "price": 9.99, "description": "TSA-approved luggage lock", "tags": ["lock", "travel", "security"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Luggage+Lock"},
    {"id": 197, "name": "Travel Adapter", "category": "Travel", "price": 24.99, "description": "Universal power adapter for travel", "tags": ["adapter", "travel", "power"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Travel+Adapter"},
    {"id": 198, "name": "Travel Toiletry Kit", "category": "Travel", "price": 29.99, "description": "Organizing toiletry bag for travel", "tags": ["toiletry", "travel", "organizing"], "rating": 4.3, "image_url": "https://via.placeholder.com/300x300?text=Toiletry+Kit"},
    {"id": 199, "name": "Compression Packing Cubes", "category": "Travel", "price": 19.99, "description": "Space-saving packing cubes set", "tags": ["packing-cubes", "travel", "organizing"], "rating": 4.4, "image_url": "https://via.placeholder.com/300x300?text=Packing+Cubes"},
]

# Features enabled
FEATURES = {
    "google_sheets_integration": False,  # Enable with credentials
    "shopify_integration": False,         # Enable with store details
    "firebase_sync": False,               # Enable with firebase config
    "user_preferences": True,             # Store user preferences
    "conversation_history": True,         # Maintain chat history
}
