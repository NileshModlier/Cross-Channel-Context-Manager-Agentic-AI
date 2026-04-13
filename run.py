from ingestion.normalizer import normalize_message
from agents.intent_agent import detect_intent
from agents.sentiment_agent import detect_sentiment
from state.state_schema import *
from state.state_store import load_state,save_state
from datetime import datetime

raw={"customer_id":"CUST_001","channel":"whatsapp","text":"I want refund","timestamp":"2026-03-24T10:00:00"}
msg=normalize_message(raw)
intent,ic=detect_intent(msg['text'])
sent,sc=detect_sentiment(msg['text'])
state=load_state(msg['customer_id'])
if not state:
 state=CustomerState(customer_id=msg['customer_id'],active_intent=IntentState(name=intent,confidence=ic,last_updated=datetime.utcnow()),sentiment=SentimentState(label=sent,confidence=sc,last_updated=datetime.utcnow()),conversation_goal=intent,open_tasks=["analyze"],channel_history=[],summary_memory="",created_at=datetime.utcnow(),last_updated=datetime.utcnow())
state.channel_history.append(ChannelEvent(channel=msg['channel'],timestamp=msg['timestamp'],summary=msg['text']))
state.last_updated=datetime.utcnow()
save_state(state)
print('State updated')
