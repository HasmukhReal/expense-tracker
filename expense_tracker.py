expenses = {}
def expense_record(func_date):
    while True:
        choice2 = input(f"Do you wanna add expense amount for {func_date}?(y/n): ")
        if choice2.lower() == 'y':
            a = int(input("Enter the expense amount: "))
            r = input("Enter Reason: ")
            expenses[func_date].append({
                "amount": a,
                "reason": r
            })
        elif choice2.lower() == 'n':
            print("Exiting adding mode...")
            break
        else:
            print("Wrong Input... Try Again!")

while True:
    print("What do you wanna do?")
    print("a = Add Expense\nr = Remove Expense\ns = Save\nq = Quit\nsq = Save and Quit")
    choice = input("")

    match choice.lower():
        case "a":
            date = input("Enter Date(dd-mm-yyyy): ")

