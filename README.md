# 💰 Expense Tracker

A simple **command-line expense tracker** written in Python.  
Keeps track of daily expenses with JSON storage and provides reports by day, month, and year.  

---

## 🚀 Features
- Add new purchase 
- Save and load data in **JSON**  
- View expenses:
  - by a specific **day**
  - by **month**
  - by **year**
- Calculate total expenses  

---

## 🛠️ Tech Stack
- Python 3.11+
- Built-in modules:
  - `decimal` — precise calculations with money
  - `datetime` — date parsing and filtering
  - `json` — data storage
  - `pathlib` — filesystem paths  

---

## 📂 Project Structure
expense-tracker/
│── src/
│ └── exptrack/
│ ├── app.py # Core logic
│ ├── database.py # JSON save/load
│ └── cli.py # CLI
│── data/
│ └── db.json # Data file
│── README.md

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   cd expense-tracker
