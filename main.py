expenses = {}

#------------------------------- Data reading from file -------------------------------#
with open("data.txt", 'r') as file:
    for line in file:
        line = line.strip()
        var_date, var_amount, var_reason = line.split('|')
        var_amount = int(var_amount)
        if var_date not in expenses:
            expenses[var_date] = [{"amount": var_amount, "reason": var_reason}]
        else:
            expenses[var_date].append({"amount": var_amount, "reason": var_reason})
#--------------------------------------------------------------------------------------#

#------------------------------- Expense Adding Function -------------------------------#
def add_exp(func_date):
    while True:
        choice2 = input(f"Do you wanna add expense amount for {func_date}?(y/n): ")
        if choice2.lower() == 'y':
            a = int(input("Enter the expense amount: "))
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
    for date, exp_list in expenses.items():
        print("-" * 45)
        print(f"For date {date}:")
        print("-" * 45)

        for exp in exp_list:
            print(f"\nExpense Amount: {exp['amount']}")
            print(f"Reason: {exp['reason']}")

        print()
        
    input("Press Enter to continue...")
#---------------------------------------------------------------------------------------#

#------------------------- Saving added expenses in data file --------------------------#
def save_exp():
    with open("data.txt", "w") as file:
        for date, exp_list in expenses.items():
            for exp in exp_list:
                file.write(f"{date}|{exp['amount']}|{exp['reason']}\n")
#---------------------------------------------------------------------------------------#



#------------------------------------------------ The Main Code ------------------------------------------------#
while True:
    print("What do you wanna do?")
    print("a = Add Expense\nr = Remove Expense\nv = View Expense Data\ns = Save\nq = Quit\nsq = Save and Quit")
    choice = input("")

    match choice.lower():
        case "a":
            date = input("Enter Date(dd-mm-yyyy): ")
            add_exp(date)
        case "r":
            pass
        case "v":
            view_exp()
        case "s":
            save_exp()
        case "q":
            break
        case "sq":
            save_exp()
            input("Your file has been saved! Press enter to quit...")
            break
        case _:
            print("Please choose a valid option from the given choices...")
            continue
#---------------------------------------------------------------------------------------------------------------#