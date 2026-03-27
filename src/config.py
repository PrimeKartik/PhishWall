# src/config.py

WHITELISTED_DOMAINS = {
    "google.com", "microsoft.com", "apple.com",
    "amazon.com", "paypal.com", "openai.com",
    "github.com", "youtube.com", "wikipedia.org",
    "timesofindia.com", "ndtv.com"
}

BRANDS = [
    "google", "paypal", "amazon", "facebook",
    "apple", "microsoft", "bankofamerica"
]

SUSPICIOUS_TLDS = {
    ".tk", ".ml", ".ga", ".cf", ".gq",
    ".xyz", ".top", ".click", ".online"
}

SUSPICIOUS_KEYWORDS = {
    "login", "verify", "secure", "update",
    "account", "banking", "confirm",
    "password", "signin"
}
