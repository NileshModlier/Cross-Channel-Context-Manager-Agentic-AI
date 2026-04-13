def detect_sentiment(text):
    t=text.lower()
    if 'angry' in t or 'frustrated' in t: return 'frustrated',0.8
    return 'neutral',0.6
