def detect_intent(text):
    t=text.lower()
    if 'refund' in t: return 'refund_request',0.85
    if 'price' in t: return 'pricing_query',0.8
    return 'general_support',0.6
