About The Project

ABRA.NEXUS aggregates regional feeds from major reporting networks (GMA, ABS-CBN, PNA) alongside localized search parameters to index news telemetry across Bangued, Bucay, Dolores, Peñarrubia, Tayum, La Paz, San Juan, and all remaining sectors of Abra, Philippines.

Key Features:

Hyper-Local Targeting: Filter news by specific municipality or news source.

Smart Data Extraction: HTML parsing via BeautifulSoup to automatically retrieve thumbnail images.

TTL Caching: Built-in 15-minute memory cache to ensure ultra-fast response times and prevent upstream blocking.

React Native Ready: Cleaned ISO timestamps, trimmed article titles, and pre-configured CORS middleware.

Built With

Getting Started

Follow these instructions to set up and run the local development server on your machine.

Prerequisites

Python 3.8+ installed on your system.

python --version


Installation

Clone the repository

git clone https://github.com/TeenTech/abra-news-api.git
cd abra-news-api


Set up a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Launch the FastAPI Server

uvicorn main:app --reload


Access Interactive API Docs
Open http://127.0.0.1:8000/docs in your web browser.

Usage

Endpoint Telemetry Overview

Endpoint

Method

Description

/

GET

System health check and root landing

/api/news/latest

GET

Fetches general Abra province news telemetry

/api/news/municipality/{name}

GET

Filters news by municipality (e.g., Bangued, Bucay, Dolores)

/api/news/source/{domain}

GET

Filters news by target domain (e.g., gmanetwork.com)

Roadmap

[x] Initial RSS feed aggregation logic

[x] CORS middleware integration for mobile client support

[x] BeautifulSoup thumbnail image extraction

[x] 15-minute TTL query caching engine

[x] React Native client application (App.js)

[ ] Cloud deployment to Render / Railway

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

Creator: TeenTech

Project Link: https://github.com/TeenTech/abra-news-api

Acknowledgments

FastAPI Framework

Feedparser Library

Beautiful Soup 4

Best-README-Template