About The Project

ABRA.NEXUS aggregates regional feeds from major reporting networks alongside localized search parameters to index news telemetry across Bangued, Bucay, Dolores, Peñarrubia, Tayum, La Paz, San Juan, and all remaining sectors of Abra, Philippines.

Key Features:

Hyper-Local Targeting: Filter news by specific municipality or news source.

Smart Data Extraction: HTML parsing to automatically retrieve thumbnail images.

TTL Caching: Built-in 15-minute memory cache to ensure ultra-fast response times.

Built With

Getting Started

To get a local copy up and running follow these simple steps.

Prerequisites

Python 3.8+

python --version


Installation

Clone the repo

git clone https://github.com/TeenTech/abra-news-api.git


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


Install Python packages

pip install -r requirements.txt


Start the server

uvicorn main:app --reload


Usage

Use the interactive API documentation to test the endpoints.

Open your browser to http://127.0.0.1:8000/docs

Expand the /api/news/municipality/{municipality_name} endpoint.

Click "Try it out", enter a municipality like Bucay, and execute.

Roadmap

[x] Initial RSS feed aggregation logic

[x] CORS middleware integration

[x] BeautifulSoup thumbnail image extraction

[x] 15-minute TTL query caching engine

[ ] Cloud deployment to Render / Railway

[ ] Complete React Native mobile client

Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

License

Distributed under the MIT License.

Contact

TeenTech - Project Lead

Project Link: https://github.com/TeenTech/abra-news-api

Acknowledgments

FastAPI Framework

Feedparser Library

Beautiful Soup 4