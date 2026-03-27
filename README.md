# PhishWall 🛡️

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)]()

> **Enterprise-grade neural wall against phishing and SMS fraud.**

PhishWall is a modular, high-performance security engine designed to detect phishing URLs and fraudulent SMS patterns in real-time. Built with FastAPI and advanced heuristic analysis, it provides a robust first line of defense against modern cyber threats.

---

## 🚀 Key Features

*   **URL Intelligence**: Detects typosquatting, brand impersonation, suspicious TLDs, and IP-based attacks.
*   **SMS Fraud Engine**: Analyzes urgency tactics, financial bait, UPI scam patterns, and multi-language (Hinglish/Hindi) threats.
*   **Neural UI**: A high-impact, responsive dashboard for real-time analysis built with modern glassmorphism.
*   **FastAPI Backend**: Industry-standard high performance, data validation with Pydantic, and automated OpenAPI documentation.
*   **Modular Architecture**: Built with easily extensible detection engines.
*   **Browser Extension**: Includes a Chrome extension (`phiswall_extension`) for seamless real-time browser protection.

---

## 🛠️ Tech Stack

*   **Backend**: Python 3.9+, FastAPI, Pydantic, Uvicorn
*   **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
*   **Extension**: Chrome Extension API (Manifest V3)
*   **Analysis Logic**: Rule-based heuristics, fuzzy string matching (`difflib`), Regex pattern detection.

---

## 📦 Installation & Setup

### 1. Backend Server Setup

```bash
# Clone the repository
git clone https://github.com/your-repo/phishwall.git
cd phishwall

# Install required dependencies
pip install -r requirements.txt

# Start the FastAPI engine
python app.py
```

*   **UI Dashboard:** Open `http://localhost:8000`
*   **API Documentation:** Open `http://localhost:8000/docs`

### 2. Browser Extension Setup

1. Open Google Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer mode** in the top right corner.
3. Click on **Load unpacked**.
4. Select the `phiswall_extension` folder located inside the repository.
5. The extension will now communicate with your local FastAPI server to provide real-time protection!

---

## 💻 API Usage

You can directly interact with the PhishWall engine via its HTTP API.

**Endpoint:** `POST /scan`

**Input (Form Data):**
*   `input_text`: The URL or SMS content to scan.

**Example Request:**
```bash
curl -X 'POST' \
  'http://localhost:8000/scan' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'input_text=http://www.g00gle-login-update.com'
```

**Example Response:**
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

## 🏗️ Project Architecture

```text
phishwall/
├── src/                  # Core Application Source
│   ├── engines/          # Detection Logic
│   │   ├── url_engine.py # URL/Domain heuristics
│   │   └── sms_engine.py # SMS text heuristics
│   └── config.py         # Global rules and configuration
├── static/               # Frontend Assets (HTML, CSS, JS)
│   └── index.html        # Neural UI dashboard
├── phiswall_extension/   # Chrome browser extension
├── tests/                # Unit & Integration tests
├── app.py                # Main FastAPI Server entry point
└── requirements.txt      # Python dependencies
```

---

## 🛡️ Security Roadmap

- [x] Integrate Browser extension for real-time protection.
- [ ] Integration with Google Safe Browsing API.
- [ ] Machine Learning model for deep context URL analysis.
- [ ] User authentication and scan history tracking.

---

*Developed with ❤️ by the PhishWall Security Team.*
