from exptrack.app import  archive, add, show_by_day, show_by_month, show_by_year
from exptrack.database import save_to_json, load_from_json, migrate
archive.clear
archive.update(load_from_json())

migrate()


#while True:
 #   menu = input("Choose your option:\n[1] --> Add purcahse\n[2] --> Show by day\n[3] --> Show by month\n[4] --> Show by year\n[0] --> Exit\n: ")
  #  if menu == "1":
   #     add()
    #    save_to_json(archive)
   #elif menu == "2":
    #    show_by_day()
    #elif menu == "3":
    #    show_by_month()
    #elif menu == "4":
    #    show_by_year()
    #elif menu == "0":
    #    break