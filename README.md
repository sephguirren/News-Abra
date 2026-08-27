<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TeenTech/abra-news-api">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Abra_provincial_seal.svg/1200px-Abra_provincial_seal.svg.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ABRA.NEXUS</h3>

  <p align="center">
    Cordillera Neural News Telemetry - Localized API for Abra, Philippines
    <br />
    <a href="https://github.com/TeenTech/abra-news-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TeenTech/abra-news-api">View Demo</a>
    ·
    <a href="https://github.com/TeenTech/abra-news-api/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/TeenTech/abra-news-api/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/TeenTech/abra-news-api)

**ABRA.NEXUS** aggregates regional feeds from major reporting networks alongside localized search parameters to index news telemetry across Bangued, Bucay, Dolores, Peñarrubia, Tayum, La Paz, San Juan, and all remaining sectors of Abra, Philippines.

Key Features:
* **Hyper-Local Targeting:** Filter news by specific municipality or news source.
* **Smart Data Extraction:** HTML parsing to automatically retrieve thumbnail images.
* **TTL Caching:** Built-in 15-minute memory cache to ensure ultra-fast response times.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]
* [![FastAPI][FastAPI.tiangolo.com]][FastAPI-url]
* [![React Native][ReactNative.dev]][ReactNative-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.8+
  ```sh
  python --version
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/TeenTech/abra-news-api.git
   ```
2. Create and activate a virtual environment
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Start the server
   ```sh
   uvicorn main:app --reload
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use the interactive API documentation to test the endpoints locally.

1. Open your browser to `http://127.0.0.1:8000/docs`
2. Expand the `/api/news/municipality/{municipality_name}` endpoint.
3. Click "Try it out", enter a municipality like `Bucay`, and execute.

_For more examples, please refer to the [Documentation](https://github.com/TeenTech/abra-news-api)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Initial RSS feed aggregation logic
- [x] CORS middleware integration
- [x] BeautifulSoup thumbnail image extraction
- [x] 15-minute TTL query caching engine
- [ ] Cloud deployment to Render / Railway
- [ ] Complete React Native mobile client

See the [open issues](https://github.com/TeenTech/abra-news-api/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

TeenTech - Project Lead - uateentech@example.com

Project Link: [https://github.com/sephguirren/News-Abra]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [FastAPI Framework](https://fastapi.tiangolo.com/)
* [Feedparser Library](https://github.com/kurtmckee/feedparser)
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)