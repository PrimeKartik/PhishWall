# src/engines/url_engine.py
import re
import difflib
from urllib.parse import urlparse
from src.config import WHITELISTED_DOMAINS, BRANDS, SUSPICIOUS_TLDS, SUSPICIOUS_KEYWORDS

def normalize_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url

def normalize_domain(domain: str) -> str:
    replacements = {"0": "o", "1": "l", "3": "e", "4": "a", "5": "s"}
    for k, v in replacements.items():
        domain = domain.replace(k, v)
    return domain

def is_whitelisted(domain: str) -> bool:
    domain = domain.replace("www.", "")
    return domain in WHITELISTED_DOMAINS

def analyze_url(url: str):
    url = normalize_url(url)
    parsed = urlparse(url)

    domain = parsed.netloc.lower().replace("www.", "")
    path = parsed.path.lower()

    risk_score = 0
    reasons = []

    if is_whitelisted(domain):
        return 0, ["Whitelisted trusted domain"]

    # IP address detection
    if re.match(r'^\d+\.\d+\.\d+\.\d+', domain):
        risk_score += 50
        reasons.append("High Risk: IP address used instead of domain")

    # Suspicious TLD
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            risk_score += 25
            reasons.append(f"Suspicious TLD detected: {tld}")

    # Brand impersonation & Typosquatting
    original_domain_part = domain.split(".")[0]
    normalized_domain_part = normalize_domain(original_domain_part)

    for brand in BRANDS:
        # Exact match in subdomain/path but not official domain
        if brand in domain and domain != brand + ".com":
            risk_score += 40
            reasons.append(f"Brand impersonation attempt: {brand}")
            
        # Normalization check (g00gle -> google)
        if normalized_domain_part == brand and original_domain_part != brand:
            risk_score += 80
            reasons.append(f"CRITICAL: Intentional typosquatting of brand: {brand}")

        # Similarity check (gooogle -> google)
        similarity = difflib.SequenceMatcher(None, original_domain_part, brand).ratio()
        if similarity > 0.8 and original_domain_part != brand:
            risk_score += 45
            reasons.append(f"High Similarity to trusted brand: {brand}")

    # Suspicious keywords
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in domain:
            risk_score += 20
            reasons.append(f"Suspicious keyword in domain: {keyword}")
        if keyword in path:
            risk_score += 15
            reasons.append(f"Suspicious keyword in path: {keyword}")

    if domain.count(".") > 3:
        risk_score += 20
        reasons.append("Excessive subdomain levels (Cloaking attempt)")

    return min(risk_score, 100), reasons
