def decide_route(state):
    return 'human' if state.requires_human else 'automated'
