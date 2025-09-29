from decimal import Decimal
from datetime import datetime
from exptrack.database import load_from_json

archive = {}

DATE_FMT = "%d.%m.%Y"

def parse_date(date):
    return datetime.strptime(date, DATE_FMT)

def add():
    item = input("what item did you buy?\n: ")
    date = input("when did you buy it?\n: ")
    price = Decimal(input("What was the price?\n: "))
    archive[item] = {"price": price, "date": date}
    print(archive)
    print(f"Added Item: {item} | Price: {price:.2f} | Date: {date}")

def show_by_day():
    chosen_date = input("Insert date (format DD.MM.YYYY)\n: ")
    chosen_dt = parse_date(chosen_date)
    loaded = load_from_json()
    found = False
    for item, data in loaded.items():
        try:
            current_dt = parse_date(data['date'])
        except Exception:
            continue
        if current_dt.date() == chosen_dt.date():
            print(f"Item: {item} | Price: {data['price']:.2f} | Date: {data['date']}")
            found = True
    return

def show_by_month():
    chosen_month = input("Insert month (format MM.YYYY)\n: ")
    print(f"Purchase history for {chosen_month}:")
    chosen_mth = datetime.strptime("01." + chosen_month, DATE_FMT)
    ch_month, ch_year = chosen_mth.month, chosen_mth.year
    loaded = load_from_json()
    m_purchases = []
    for item, data in loaded.items():
        try:
            current_dt = datetime.strptime(data['date'], DATE_FMT)
            cu_month, cu_year = current_dt.month, current_dt.year
        except Exception:
            continue
        if cu_month == ch_month and cu_year == ch_year:
            print(f"Item: {item} | Price: {data['price']:.2f} | Date: {data['date']}")
        
def show_by_year():
    chosen_year = input("Insert year (format YYYY)\n: ")
    print(f"Purchase history for {chosen_year}: ")
    chosen_y = datetime.strptime("01.01." + chosen_year, DATE_FMT)
    ch_year = chosen_y.year
    loaded = load_from_json()
    y_purchases = []
    for item, data in loaded.items():
        try:
            current_dt = datetime.strptime(data['date'], DATE_FMT)
            cu_year = current_dt.year
        except Exception:
            continue
        if cu_year == ch_year:
            print(f"Item: {item} | Price: {data['price']:.2f}  | Date: {data['date']}")