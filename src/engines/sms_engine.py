# src/engines/sms_engine.py
import re

def analyze_sms(message: str):
    msg = message.lower()
    risk_score = 0
    reasons = []

    # Link in SMS
    if "http" in msg or "www." in msg or ".com" in msg or ".in" in msg:
        risk_score += 35
        reasons.append("Suspicious link in SMS (Vector for data theft)")

    # Financial bait
    financial_words = ["reward", "cashback", "bonus", "prize", "lottery", "₹", "rs", "credited", "won"]
    if any(word in msg for word in financial_words):
        risk_score += 30
        reasons.append("Financial bait detected (Common phishing hook)")

    # Urgency tactics
    urgency_words = ["urgent", "immediately", "now", "expire", "turant", "warning", "last chance"]
    if any(word in msg for word in urgency_words):
        risk_score += 20
        reasons.append("Urgency tactic detected (Social engineering)")

    # Account threats
    threat_words = ["kyc", "verify", "update", "account blocked", "band ho jayega", "suspended"]
    if any(word in msg for word in threat_words):
        risk_score += 35
        reasons.append("Account threat pattern detected (Credential harvesting)")

    # UPI scams
    if "upi" in msg or "collect request" in msg or "pin" in msg:
        risk_score += 40
        reasons.append("CRITICAL: UPI scam pattern detected")

    # Hindi detection
    if re.search(r'[\u0900-\u097F]', message):
        risk_score += 5
        reasons.append("Contains Hindi script")

    # Hindi scam words
    hindi_words = ["केवाईसी", "खाता", "तुरंत", "बंद हो जाएगा", "अपडेट करें", "इनाम"]
    if any(word in message for word in hindi_words):
        risk_score += 40
        reasons.append("High Risk: Hindi scam pattern detected")

    # Hinglish
    hinglish_words = ["aapka", "khata", "turant", "update karein", "band ho"]
    if any(word in msg for word in hinglish_words):
        risk_score += 25
        reasons.append("Hinglish scam pattern detected")

    return min(risk_score, 100), reasons
