from datetime import datetime

def normalize_message(raw):
    return {
        'customer_id': raw['customer_id'],
        'channel': raw['channel'],
        'text': raw['text'],
        'timestamp': datetime.fromisoformat(raw['timestamp'])
    }
