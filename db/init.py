import os
import json

def init_db():
    os.makedirs("data", exist_ok=True)
    if not os.path.isfile("data/db.json"):
        with open("data/db.json", mode="wt", encoding="utf-8") as f:
            json.dump([], f)