import json
from pathlib import Path
from decimal import Decimal
import sqlite3
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR/"data"/"data.db"
db = sqlite3.connect(DB_PATH)
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS purchases(
          name text,
          price text,
          date text
)
          """)

def migrate():
    loaded = load_from_json()
    for i, v in loaded.items():
        name = i
        price = str(v["price"])
        date = str(v["date"])
        c.execute("INSERT INTO purchases (name, price, date) VALUES (?,?,?)", (name, price, date))
        db.commit()
    db.close()


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