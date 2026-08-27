⚡ ABRA.NEXUS // Cyber-Local News Grid v1.0

CLASSIFIED INTELLIGENCE FEED // CORDILLERA ADMINISTRATIVE REGION (CAR)
A high-throughput, low-latency news telemetry engine serving Abra Province and its 27 municipal sectors.

🌌 Overview

ABRA.NEXUS is an automated, real-time news aggregation grid built on FastAPI. Designed to interface seamlessly with modern mobile neural HUDs (React Native), it extracts hyper-local news telemetry across major regional media networks (GMA, ABS-CBN, PNA) and localized communication channels (Damdamag Abra).

Equipped with volatile TTL memory caching, automated thumbnail parsing engines, and ISO timestamp mutation pipelines, it delivers hyper-structured JSON payloads directly to mobile endpoints.

       [ Regional News Sources ] 
      (Google / GMA / ABS-CBN / PNA)
                    │
                    ▼
          ┌───────────────────┐
          │   ABRA.NEXUS      │
          │   (FastAPI Engine)│
          └─────────┬─────────┘
                    │  ◄── [ 15-Min Volatile TTLCache Matrix ]
                    │  ◄── [ BeautifulSoup DOM Image Extractor ]
                    ▼
     [ React Native Mobile Client ]


🛠 Core Systems & Tech Stack

System Component

Technology

Operational Function

Core Framework

FastAPI

Asynchronous, high-performance web API framework

Server Engine

Uvicorn

Lightning-fast ASGI server implementation

Data Ingestion

feedparser

Real-time RSS/Atom feed signal parsing

HTML Mutation

BeautifulSoup4

DOM element extraction for media assets (Thumbnails)

Memory Matrix

cachetools (TTLCache)

900s (15-min) volatile cache to prevent source throttling

Security Protocol

CORSMiddleware

Universal cross-origin access for mobile clients

📡 Telemetry Endpoints

GET /

Handshake Protocol: Verifies system operational status and links to interactive diagnostic UI (/docs).

GET /api/news/latest

Primary Provincial Feed: Streams broad, real-time news telemetry across the entirety of Abra Province.

GET /api/news/municipality/{municipality_name}

Sector-Specific Scanning: Targets municipal nodes across Abra:

Bangued | Bucay | Dolores | Peñarrubia | Tayum ... and all 27 municipal sectors.

GET /api/news/source/{source_name}

Domain Isolation: Filters telemetry streams to specific media channels:

gmanetwork.com | news.abs-cbn.com | pna.gov.ph

⚡ Systems Initialization Protocol

Execute these commands in your local terminal sequence to activate the API node:

1. Clone & Access Directory

git clone https://github.com/YourUsername/abra-news-api.git
cd abra-news-api


2. Activate Virtual Subsystem

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate


3. Inject Dependencies

pip install -r requirements.txt


4. Ignite Core Engine

uvicorn main:app --reload


🛸 Diagnostic Dashboard: Access the visual swagger UI at http://127.0.0.1:8000/docs

🧬 Data Normalization & Cache Matrix

15-Minute Volatile Memory Matrix: Caches up to 100 unique search query keys for 900 seconds (TTLCache), dramatically accelerating response times to sub-10ms for recurring mobile queries.

DOM Asset Extraction: Scans raw HTML payloads using BeautifulSoup to extract hidden <img> thumbnail URLs, serving a clean "image_url" key in every JSON object.

ISO-8601 Timestamp Standard: Converts legacy string dates into standardized UTC strings (YYYY-MM-DDTHH:MM:SSZ) for seamless parsing in JavaScript/React Native.

🌌 System Roadmap

[x] Phase 1: Core RSS Telemetry Grid & FastAPI Architecture

[x] Phase 2: DOM Image Extraction & TTLCache Optimization

[ ] Phase 3: Orbital Uplink (Cloud Deployment via Render / Railway)

[ ] Phase 4: React Native HUD Frontend Integration

👥 Grid Operators

Lead Developer & System Architect: @YourUsername

Maintained under the Cordillera Neural Network Protocol.