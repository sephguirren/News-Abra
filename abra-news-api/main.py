from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import feedparser
import urllib.parse
import uvicorn
import time
from datetime import datetime
from bs4 import BeautifulSoup
from cachetools import TTLCache, cached

# Initialize the FastAPI application
app = FastAPI(
    title="Abra Local News API",
    description="A REST API fetching local news for Abra, Philippines and its municipalities.",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This is crucial for allowing your React Native app (or web frontends) 
# to make requests to this backend without getting blocked by security policies.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace "*" with your specific app domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base URL for Google News RSS searches, localized to the Philippines
GOOGLE_NEWS_RSS_URL = "https://news.google.com/rss/search?q={query}&hl=en-PH&gl=PH&ceid=PH:en"

# Setup 15-minute Cache (900 seconds) for up to 100 different queries
# This prevents your API from getting blocked by Google if your mobile app gets popular
news_cache = TTLCache(maxsize=100, ttl=900)

@cached(cache=news_cache)
def fetch_rss_news(query: str):
    """
    Helper function to construct the URL, fetch the RSS feed, 
    and format the entries into a clean JSON structure.
    """
    # Safely encode the search query for the URL (e.g., changes spaces to %20)
    encoded_query = urllib.parse.quote(query)
    url = GOOGLE_NEWS_RSS_URL.format(query=encoded_query)
    
    # Parse the RSS feed using feedparser
    feed = feedparser.parse(url)
    
    # Check if the feed is empty or failed to parse
    if getattr(feed, 'bozo', 0) != 0 and not feed.entries:
        return []

    articles = []
    # Loop through the feed entries and extract the data we need
    for entry in feed.entries:
        
        # --- 1. DATA CLEANING: Clean Title ---
        raw_title = entry.title
        # Google News titles look like "News Title - Publisher Name"
        # This removes the "- Publisher Name" from the end for a cleaner look
        clean_title = raw_title.rsplit('-', 1)[0].strip() if '-' in raw_title else raw_title

        # --- 2. DATA CLEANING: Format Date ---
        try:
            # Convert the parsed time tuple into a standard ISO 8601 string
            # React Native's Date object prefers this standard format
            dt = datetime.fromtimestamp(time.mktime(entry.published_parsed))
            clean_date = dt.isoformat() + "Z"
        except Exception:
            clean_date = entry.published  # Fallback to the raw string if parsing fails
        
        # --- 3. EXTRACT THUMBNAIL: Parse HTML ---
        thumbnail_url = None
        if hasattr(entry, 'description'):
            # The description actually contains HTML. We use BeautifulSoup to read it.
            soup = BeautifulSoup(entry.description, 'html.parser')
            img_tag = soup.find('img')
            if img_tag and img_tag.get('src'):
                thumbnail_url = img_tag['src']

        # Append the beautifully cleaned data to our list
        articles.append({
            "title": clean_title,
            "original_title": raw_title,
            "link": entry.link,
            "published_at": clean_date,
            "source": entry.source.title if hasattr(entry, 'source') else "Unknown",
            "image_url": thumbnail_url
        })
    
    return articles

@app.get("/")
def read_root():
    """Root endpoint to verify the API is running."""
    return {
        "message": "Welcome to the Abra Local News API!", 
        "documentation": "Go to /docs to see the endpoints and test them."
    }

@app.get("/api/news/latest")
def get_latest_abra_news():
    """Fetches the latest general news for the province of Abra."""
    query = "Abra Province Philippines"
    news = fetch_rss_news(query)
    
    if not news:
        raise HTTPException(status_code=404, detail="No news found for Abra at this time.")
        
    return {"status": "success", "total_results": len(news), "data": news}

@app.get("/api/news/municipality/{municipality_name}")
def get_municipality_news(municipality_name: str):
    """
    Fetches news for a specific municipality in Abra. 
    Try passing 'Bangued', 'Bucay', 'Dolores', or 'Peñarrubia'.
    """
    # Construct a highly targeted query
    query = f"{municipality_name} Abra Philippines"
    news = fetch_rss_news(query)
    
    return {
        "status": "success", 
        "municipality": municipality_name, 
        "total_results": len(news), 
        "data": news
    }

@app.get("/api/news/source/{source_name}")
def get_news_by_source(source_name: str):
    """
    Fetches Abra news from a specific source domain.
    Examples for source_name: 'gmanetwork.com', 'news.abs-cbn.com', 'pna.gov.ph'
    """
    # The 'site:' operator forces Google News to only return results from that domain
    query = f"Abra Province site:{source_name}"
    news = fetch_rss_news(query)
    
    return {
        "status": "success", 
        "source": source_name, 
        "total_results": len(news), 
        "data": news
    }

# This block allows you to run the file directly using `python main.py`
if __name__ == "__main__":
    print("Starting the Abra Local News API server...")
    # Run the app on port 8000. 'main' refers to the name of this file (main.py),
    # and 'app' refers to the FastAPI instance we created at the top.
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)