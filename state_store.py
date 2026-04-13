import json, pathlib
from state.state_schema import CustomerState
STORE=pathlib.Path('data/state_store.json')

def load_state(cid):
    if not STORE.exists(): return None
    data=json.loads(STORE.read_text())
    return CustomerState.parse_obj(data.get(cid))

def save_state(state):
    data={}
    if STORE.exists(): data=json.loads(STORE.read_text())
    data[state.customer_id]=state.dict()
    STORE.parent.mkdir(exist_ok=True)
    STORE.write_text(json.dumps(data,default=str,indent=2))
