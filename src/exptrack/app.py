from decimal import Decimal
from datetime import datetime

archive = {}

DATE_FMT = "%d.%m.%Y"

def parse_date(date):
    return datetime.strptime(date, DATE_FMT)

def add():
    purchase = {
        'name': input("what item did you buy?\n: "),
        'date':  input("when did you buy it?\n: "),
        'price':  int(Decimal(input("What was the price?\n: ").replace(",", "."))*100)
    }
    return purchase

def show_by_day():
    chosen_date = input("Insert date (format DD.MM.YYYY)\n: ")
    return chosen_date

def show_by_month():
    chosen_month = str(input("Insert month (format MM.YYYY)\n: "))
    return chosen_month

def show_by_year():
    chosen_year = str(input("Insert year (format YYYY)\n: "))
    return chosen_year