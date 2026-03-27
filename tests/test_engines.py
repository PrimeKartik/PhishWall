# tests/test_engines.py
import pytest
from src.engines.url_engine import analyze_url
from src.engines.sms_engine import analyze_sms

def test_url_whitelist():
    score, reasons = analyze_url("https://google.com")
    assert score == 0
    assert "Whitelisted" in reasons[0]

def test_url_typosquatting():
    score, reasons = analyze_url("http://g00gle.com")
    assert score >= 40
    assert any("typosquatting" in r.lower() for r in reasons)

def test_url_suspicious_tld():
    score, reasons = analyze_url("http://bank-login.tk")
    assert score >= 15
    assert any(".tk" in r for r in reasons)

def test_sms_financial_bait():
    score, reasons = analyze_sms("Congratulations! You won a prize of ₹10000. Click here: http://scam.com")
    assert score >= 45  # Link (25) + Financial (20)
    assert any("Financial bait" in r for r in reasons)

def test_sms_urgency():
    score, reasons = analyze_sms("URGENT: Your account will be blocked. Update KYC now.")
    assert score >= 35 # Urgency (15) + Account (20)
    assert any("Urgency" in r for r in reasons)

def test_sms_hindi():
    score, reasons = analyze_sms("आपका खाता तुरंत बंद हो जाएगा")
    assert score >= 50 # Hindi script (10) + Hindi scam words (25) + Hinglish (15) 
    # Actually "खाता" is in hindi_words, "आपका" is Hinglish (aapka) - if it matches.
    assert any("Hindi" in r for r in reasons)
