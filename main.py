from exptrack.app import add, show_by_day, show_by_month, show_by_year
from exptrack.database import create_purchase, ensure_db, load_by_day, load_by_month, load_by_year
ensure_db()

while True:
    menu = input("Choose your option:\n[1] --> Add purcahse\n[2] --> Show by day\n[3] --> Show by month\n[4] --> Show by year\n[0] --> Exit\n: ")
    if menu == "1":
        purchase = add()
        create_purchase(purchase)
    elif menu == "2":
        date = show_by_day()
        print(load_by_day(date))
    elif menu == "3":
        chosen_month = show_by_month()
        print(load_by_month(chosen_month))
    elif menu == "4":
        chosen_year = show_by_year()
        print(load_by_year(chosen_year))

    elif menu == "0":
        break