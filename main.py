import storage
import copy
import expenses

#-------------------------------- Initializing the data --------------------------------#
expense = storage.load_data()
temp_expenses = copy.deepcopy(expense)
#---------------------------------------------------------------------------------------#



#-------------------------------------------- The Main Code --------------------------------------------#
while True:
    print("What do you wanna do?")
    print("a = Add Expense\nr = Remove Expense\nv = View Expense Data\ns = Save\nq = Quit\nsq = Save and Quit")
    choice = input("")

    match choice.lower():
        case "a":
            date = input("Enter Date(dd-mm-yyyy): ")
            expenses.add_exp(date, expense)
        case "r":
            expenses.remove_exp(expense)
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
#-------------------------------------------------------------------------------------------------------#
