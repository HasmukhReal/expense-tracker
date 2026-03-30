#------------------------------- Expense Adding Function -------------------------------#
def add_exp(func_date, expense):
    while True:
        choice2 = input(f"Do you wanna add expense amount for {func_date}?(y/n): ")
        if choice2.lower() == 'y':
            try:
                a = int(input("Enter the expense amount: "))
            except ValueError:
                print("Invalid amount entered.")
                continue
            r = input("Enter Reason: ")
            if func_date in expense:
                pass
            else:
                expense[func_date] = []
            expense[func_date].append({
                "amount": a,
                "reason": r
            })
        elif choice2.lower() == 'n':
            print("Exiting adding mode...")
            break
        else:
            print("Wrong Input... Try Again!")
#---------------------------------------------------------------------------------------#


#---------------------------- Expense list viewing function ----------------------------#
def view_exp(expense):
    if not expense:
        print("No expenses recorded.")
        input("Press Enter to continue...")
        return
    for date in sorted(expense):
        print("-" * 45)
        print(f"For date {date}:")
        print("-" * 45)

        for exp in expense[date]:
            print(f"\nExpense Amount: {exp['amount']}")
            print(f"Reason: {exp['reason']}")

        print()
        
    input("Press Enter to continue...")
#---------------------------------------------------------------------------------------#


#------------------------------ Expense Removing Function ------------------------------#
def remove_exp(expense):
    func_date = input("Enter the date from which you want expense to be removed: ")

    try:
        func_amount = int(input("Enter the exact amount of the expense you want to remove: "))
    except ValueError:
        print("Invalid amount entered.")
        return

    func_reason = input("Enter the exact reason of the expense you want to remove: ")

    if func_date not in expense:
        print("Entered date is not in the record.")
        print(f"Entered Date: {func_date}")
        return

    exp_list = expense[func_date]
    found = False

    for exp in exp_list:
        if exp["amount"] == func_amount and exp["reason"] == func_reason:
            print(f"\nAmount: {exp['amount']}")
            print(f"Reason: {exp['reason']}")
            confirm = input("\nAre you sure you want to delete this expense? (y/n): ")
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