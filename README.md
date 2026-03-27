---
title: PhishWall Engine
emoji: 🛡️
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
app_port: 7860
---

<div align="center">
  
# 🛡️ PhishWall

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-success?style=flat-square)](https://opensource.org/licenses/MIT)

**Enterprise-grade neural wall against phishing and SMS fraud.** <br>
*PhishWall is a modular, high-performance security engine designed to detect phishing URLs and fraudulent SMS patterns in real-time.*

</div>

---

## 🔴 Live Demo

You can try the live production environment hosted on Hugging Face Spaces:

**[🔗 Access PhishWall Live System](https://primekartik-phishwall.hf.space)**

*(Note: The first request may take a few seconds as the server wakes up. All subsequent requests are fast).*

---

## 🚀 Key Features

* **Advanced URL Intelligence**: Detects typosquatting, brand impersonation, deceptive TLDs, and IP-based attacks.
* **SMS Fraud Engine**: Analyzes urgency tactics, financial bait, UPI scam patterns, and multi-language (Hinglish/Hindi) threats.
* **Neural Dashboard**: A high-impact, responsive UI for real-time analysis built with modern glassmorphism aesthetics.
* **REST Ecosystem**: Built with modern standard FastAPI high-performance architecture, robust data validation using Pydantic, and automated OpenAPI specs.
* **Chrome Extension Ready**: Seamlessly integrates directly into your browser context for real-time browsing protection.

---

## 💻 API Documentation

PhishWall exposes a robust HTTP API for integration with other apps or services.

**Endpoint:** `POST /scan`

### Example Request (`curl`)
```bash
curl -X 'POST' \
  'https://primekartik-phishwall.hf.space/scan' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'input_text=http://www.g00gle-login-update.com'
```

### JSON Response Structure
```json
{
  "input": "http://www.g00gle-login-update.com",
  "result": "PHISHING / FRAUD",
  "risk_score": 100,
  "risk_level": "HIGH",
  "reasons": [
    "CRITICAL: Intentional typosquatting of brand: google",
    "Brand impersonation attempt: google",
    "Suspicious keyword in domain: login",
    "Suspicious keyword in domain: update"
  ]
}
```

---

## 🛠️ Local Development & Setup

If you wish to run the engine locally for development:

### 1. Backend Server Setup
```bash
# Clone the repository
git clone https://github.com/PrimeKartik/PhishWall.git
cd PhishWall

# Install required dependencies
pip install -r requirements.txt

# Start the FastAPI engine
python app.py
```
* **Dashboard:** Open `http://localhost:8000`
* **API Swagger UI:** Open `http://localhost:8000/docs`

### 2. Browser Extension Installation
1. Navigate to `chrome://extensions/` in your Chrome browser.
2. Enable **Developer mode** in the top-right corner.
3. Click **Load unpacked** and select the `phiswall_extension` folder from this directory.
4. Update the endpoint in your extension's background script to communicate with either your `localhost` or the **Live Demo URL**.

---

## 🏗️ Architecture Stack

PhishWall's codebase is heavily modularized for future scaling:

```text
phishwall/
├── src/                  # Core Intelligence Source
│   ├── engines/          # Detection Logic Models
│   │   ├── url_engine.py # URL/Domain heuristic tree
│   │   └── sms_engine.py # SMS text heuristics
│   └── config.py         # Global rules and thresholds
├── static/               # Neural UI Assets (HTML, CSS, JS)
│   └── index.html        # Main dashboard
├── phiswall_extension/   # Manifest V3 Chrome Extension
├── Dockerfile            # Hugging Face deployment container
└── app.py                # Core routing engine (FastAPI)
```

---

## 🛡️ Security Roadmap

- [x] Integrate Browser extension for real-time protection.
- [x] Containerize application and push to Hugging Face production space.
- [ ] Implement Google Safe Browsing API integration.
- [ ] Train Machine Learning models for deep-context URL tracking.
- [ ] Add JWT User Authentication & Historical Logging.

---

<div align="center">
  <i>Developed with ❤️ by the PhishWall Security Team</i>
</div>
