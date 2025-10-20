import json
from pathlib import Path
from decimal import Decimal
import sqlite3
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR/"data"/"data.db"

def ensure_db():
    with sqlite3.connect(DB_PATH) as db:
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS purchases(
                name text,
                price integer,
                date text
        )
                """)
    return "DB OK"

def create_purchase (purchase):
    with sqlite3.connect(DB_PATH) as db:
        c = db.cursor()
        c.execute("""
                INSERT INTO purchases (name,price,date) VALUES (?,?,?)
                  """, (purchase['name'], (purchase['price']), purchase['date']))
        db.commit()
    return

def load_by_day(date):
    with sqlite3.connect(DB_PATH) as db:
        c = db.cursor()
        c.execute("""
                SELECT * FROM purchases WHERE date = ?
                  """, (date,))
        return c.fetchall()

def load_by_month(chosen_month):
    with sqlite3.connect(DB_PATH) as db:
        c = db.cursor()
        c.execute("""
                SELECT * FROM purchases WHERE date LIKE ?
                  """, ('%.' + chosen_month,))
        rows = c.fetchall()
        if not rows:
            print("No purchases found for this month.")
        else:
            return rows
        
def load_by_year(chosen_year):
    with sqlite3.connect(DB_PATH) as db:
        c = db.cursor()
        pattern = f"%{chosen_year}%"
        c.execute("""
                    SELECT * FROM purchases WHERE date LIKE ?
                   """, (pattern,))
        rows = c.fetchall()
        if not rows:
            print("No purchases found for this year.")
        else:
            return rows
        

#def migrate():
#    loaded = load_from_json()
#    for i, v in loaded.items():
#        name = i
#        price = str(v["price"])
#        date = str(v["date"])
#        c.execute("INSERT INTO purchases (name, price, date) VALUES (?,?,?)", (name, price, date))
#        db.commit()
#    db.close()
