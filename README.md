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
   git clone https://github.com/G004S/expense-tracker.git
   cd expense-tracker

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. Run the program:
    python -m exptrack.cli


## 📸 Example (CLI)
Choose your option:
[1] --> Add purchase
[2] --> Show by day
[3] --> Show by month
[4] --> Show by year
[0] --> Exit


## 🎯 What I learned
1.Working with files (JSON)
2.Using decimal to avoid floating point issues in money calculations
3.Parsing and validating dates with datetime
4.Organizing a Python project using the src layout
5.Building a simple CLI application
6.Preparing projects for GitHub portfolio