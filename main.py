import storage
import copy
import expenses
from utils import validate_date, get_current_date, BackPressed, prompt

# Initialize data
expense = storage.load_data()
temp_expenses = copy.deepcopy(expense)



# Main application loop
while True:
    print("\n  What do you wanna do?")
    print("  ─────────────────────────")
    print("  [a] Add Expense")
    print("  [r] Remove Expense")
    print("  [v] View Expense Data")
    print("  [s] Save")
    print("  [q] Quit")
    print("  [sq] Save and Quit")
    print("  ─────────────────────────")
    choice = input("\nEnter your choice: ")

    match choice.lower():
        case "a":
            try:
                while True:
                    raw = prompt(f"Enter Date(dd-mm-yyyy) [press Enter for today {get_current_date()}]: ")
                    date = raw or get_current_date()
                    if validate_date(date):
                        break
                    print("Invalid date. Please use DD-MM-YYYY format (e.g. 09-05-2026).")
                expenses.add_exp(date, expense)
            except BackPressed:
                print("Operation cancelled.")
        case "r":
            try:
                expenses.remove_exp(expense)
            except BackPressed:
                print("Operation cancelled.")
        case "v":
            expenses.view_exp(expense)
        case "s":
            storage.save_data(expense)
        case "q":
            if temp_expenses == expense:
                break
            else:
                q = input("Some changes are not saved, are you sure you wanna discard all changes and quit?(y/n): ")
                if q.lower() == "n":
                    storage.save_data(expense)
                    input("Changes saved! Press Enter to quit...")
                    break
                elif q.lower() == "y":
                    break
                else:
                    input("Invalid choice! Try again later...")
        case "sq":
            storage.save_data(expense)
            input("Your file has been saved! Press enter to quit...")
            break
        case _:
            print("Please choose a valid option from the given choices...")
            continue
