import os

# This finds the directory where storage.py actually lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "data.txt")
DATA_DIR = os.path.join(BASE_DIR, "data")

def ensure_data_dir():
    """Creates the data directory if it doesn't exist"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_data():
    """Reads data from the file and returns a dictionary"""
    expenses = {}
    if not os.path.exists(DATA_FILE):
        return expenses

    try:
        with open(DATA_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if not line: continue
                
                var_date, var_amount, var_reason = line.split('|')
                var_amount = int(var_amount)
                
                if var_date not in expenses:
                    expenses[var_date] = []
                expenses[var_date].append({"amount": var_amount, "reason": var_reason})
    except (FileNotFoundError, ValueError):
        print("Warning: Data file is empty or corrupted. Starting from beginning...")
    
    return expenses

def save_data(expenses_dict):
    """Writes the entire dictionary to the data file"""
    ensure_data_dir()
    with open(DATA_FILE, "w") as file:
        for date, exp_list in expenses_dict.items():
            for exp in exp_list:
                file.write(f"{date}|{exp['amount']}|{exp['reason']}\n")