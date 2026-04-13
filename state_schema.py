from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class IntentState(BaseModel):
    name:str
    confidence:float=Field(ge=0,le=1)
    last_updated:datetime

class SentimentState(BaseModel):
    label:str
    confidence:float=Field(ge=0,le=1)
    last_updated:datetime

class ChannelEvent(BaseModel):
    channel:str
    timestamp:datetime
    summary:str

class CustomerState(BaseModel):
    customer_id:str
    active_intent:IntentState
    sentiment:SentimentState
    conversation_goal:str
    open_tasks:List[str]
    channel_history:List[ChannelEvent]
    summary_memory:str
    requires_human:bool=False
    created_at:datetime
    last_updated:datetime
