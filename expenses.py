from datetime import date as date_type
from utils import parse_date, validate_date, prompt

CATEGORIES = ["Food", "Travel", "Bills", "Shopping", "Other"]


def add_exp(func_date: str, expense: dict) -> None:
    while True:
        choice2 = prompt(f"Do you wanna add expense amount for {func_date}? (y/n) [back to cancel]: ")
        if choice2.lower() == 'y':
            try:
                a = int(prompt("Enter the expense amount: "))
            except ValueError:
                print("Invalid amount entered.")
                continue
            r = prompt("Enter Reason: ")
            print("Select Category:")
            for i, cat in enumerate(CATEGORIES, 1):
                print(f"  {i}. {cat}")
            cat_choice = prompt("Enter category number: ")
            try:
                cat_idx = int(cat_choice) - 1
                if 0 <= cat_idx < len(CATEGORIES):
                    category = CATEGORIES[cat_idx]
                else:
                    category = "Other"
            except ValueError:
                category = "Other"
            if func_date not in expense:
                expense[func_date] = []
            expense[func_date].append({
                "amount": a,
                "reason": r,
                "category": category
            })
        elif choice2.lower() == 'n':
            print("Exiting adding mode...")


def view_exp(expense):
    """Sorts and displays all expenses by date."""
    if not expense:
        print("No expenses recorded.")
        input("Press Enter to continue...")
        return
    for exp_date in sorted(expense, key=lambda d: parse_date(d) or date_type.min):
        print("-" * 45)
        print(f"For date {exp_date}:")
        print("-" * 45)

        for exp in expense[exp_date]:
            print(f"\nExpense Amount: {exp['amount']}")
            print(f"Reason: {exp['reason']}")
            print(f"Category: {exp.get('category', 'Other')}")

        print()
        
    input("Press Enter to continue...")


def remove_exp(expense: dict) -> None:
    """Prompt user for details and remove a specific expense entry."""
    func_date = prompt("Enter the date from which you want expense to be removed [back to cancel]: ")

    if not validate_date(func_date):
        print("Invalid date format. Please use DD-MM-YYYY (e.g. 09-05-2026).")
        return

    try:
        func_amount = int(prompt("Enter the exact amount of the expense you want to remove: "))
    except ValueError:
        print("Invalid amount entered.")
        return

    func_reason = prompt("Enter the exact reason of the expense you want to remove: ")
    func_category = prompt("Enter the exact category of the expense you want to remove: ")

    if func_date not in expense:
        print("Entered date is not in the record.")
        print(f"Entered Date: {func_date}")
        return

    exp_list = expense[func_date]
    found = False

    for exp in exp_list:
        if exp["amount"] == func_amount and exp["reason"] == func_reason and exp.get("category") == func_category:
            print(f"\nAmount: {exp['amount']}")
            print(f"Reason: {exp['reason']}")
            print(f"Category: {exp.get('category', 'Other')}")
            confirm = prompt("\nAre you sure you want to delete this expense? (y/n) [back to cancel]: ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                input()
                return
            exp_list.remove(exp)
            print("\nExpense removed from record.")
            found = True
            break

    if not exp_list:
        del expense[func_date]

    if not found:
        print("No matching expense found with given combination of date, amount, and reason.")

    input("\nPress Enter to continue...")
#---------------------------------------------------------------------------------------#