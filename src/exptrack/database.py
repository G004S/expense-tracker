import json
from decimal import Decimal
def save_to_json(archive):
    copy = {}
    for i, v in archive.items():
        price = str(v['price'])
        date = v["date"]
        copy[i] = {"price": price, "date": date}
        
    with open ("db.json", "w") as f:
        json.dump(copy, f, indent=4)

def load_from_json():
    with open ("data\db.json", "r") as f:
       ld = json.load(f)
       loaded = {}
       for i, v in ld.items():
            price = Decimal(v['price'])
            date = v['date']
            loaded[i] = {"price": price, "date": date}
    return loaded