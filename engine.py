import json

FILE = "storage.json"

def load_state():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "weight": 75,
            "fatigue": 50,
            "recovery": 50,
            "food_index": 0
        }

def save_state(state):
    with open(FILE, "w") as f:
        json.dump(state, f)

def update_state(state, mode):
    if mode == "train":
        state["fatigue"] += 10
        state["recovery"] -= 5
        state["weight"] -= 0.2

    if mode == "rest":
        state["fatigue"] -= 15
        state["recovery"] += 15

    state["fatigue"] = max(0, min(100, state["fatigue"]))
    state["recovery"] = max(0, min(100, state["recovery"]))

    return state
