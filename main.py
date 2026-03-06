import copy

expenses = {} # Main data loader
temp_expenses = {} # Save checker

#------------------------------- Data reading from file -------------------------------#
try:
    with open("data.txt", 'r') as file:
        for line in file:
            line = line.strip()
            var_date, var_amount, var_reason = line.split('|')
            var_amount = int(var_amount)
            if var_date not in expenses:
                expenses[var_date] = [{"amount": var_amount, "reason": var_reason}]
            else:
                expenses[var_date].append({"amount": var_amount, "reason": var_reason})
        temp_expenses = copy.deepcopy(expenses)
except FileNotFoundError:
    pass
#--------------------------------------------------------------------------------------#

#------------------------------- Expense Adding Function -------------------------------#
def add_exp(func_date):
    while True:
        choice2 = input(f"Do you wanna add expense amount for {func_date}?(y/n): ")
        if choice2.lower() == 'y':
            try:
                a = int(input("Enter the expense amount: "))
            except ValueError:
                print("Invalid amount entered.")
                return
            r = input("Enter Reason: ")
            if func_date in expenses:
                pass
            else:
                expenses[func_date] = []
            expenses[func_date].append({
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
def view_exp():
    if not expenses:
        print("No expenses recorded.")
        input("Press Enter to continue...")
        return
    for date in sorted(expenses):
        print("-" * 45)
        print(f"For date {date}:")
        print("-" * 45)

        for exp in expenses[date]:
            print(f"\nExpense Amount: {exp['amount']}")
            print(f"Reason: {exp['reason']}")

        print()
        
    input("Press Enter to continue...")
#---------------------------------------------------------------------------------------#

#------------------------- Saving added expenses in data file --------------------------#
def save_exp():
    global temp_expenses
    with open("data.txt", "w") as file:
        for date, exp_list in expenses.items():
            for exp in exp_list:
                file.write(f"{date}|{exp['amount']}|{exp['reason']}\n")
    temp_expenses = copy.deepcopy(expenses)
#---------------------------------------------------------------------- -----------------#

#------------------------------ Expense Removing Function ------------------------------#
def remove_exp():
    func_date = input("Enter the date from which you want expense to be removed: ")

    try:
        func_amount = int(input("Enter the exact amount of the expense you want to remove: "))
    except ValueError:
        print("Invalid amount entered.")
        return

    func_reason = input("Enter the exact reason of the expense you want to remove: ")

    if func_date not in expenses:
        print("Entered date is not in the record.")
        print(f"Entered Date: {func_date}")
        return

    exp_list = expenses[func_date]
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
        del expenses[func_date]

    if not found:
        print("No matching expense found with given combination of date, amount, and reason.")

    input("\nPress Enter to continue...")
#---------------------------------------------------------------------------------------#



#-------------------------------------------- The Main Code --------------------------------------------#
while True:
    print("What do you wanna do?")
    print("a = Add Expense\nr = Remove Expense\nv = View Expense Data\ns = Save\nq = Quit\nsq = Save and Quit")
    choice = input("")

    match choice.lower():
        case "a":
            date = input("Enter Date(dd-mm-yyyy): ")
            add_exp(date)
        case "r":
            remove_exp()
        case "v":
            view_exp()
        case "s":
            save_exp()
        case "q":
            if temp_expenses == expenses:
                break
            else:
                q = input("Some changes are not save, are you sure you wanna discard all changes and quit?(y/n): ")
                if q.lower() == "n":
                    save_exp()
                    input("Changes saved! Press Enter to quit...")
                    break
                elif q.lower() == "y":
                    break
                else:
                    input("Invalid choice! Try again later...")
        case "sq":
            save_exp()
            input("Your file has been saved! Press enter to quit...")
            break
        case _:
            print("Please choose a valid option from the given choices...")
            continue
#-------------------------------------------------------------------------------------------------------#