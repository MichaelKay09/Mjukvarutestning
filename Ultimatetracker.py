##### MAIN MENU #####
from Budget import Budget
from Transaction import Transaction
from datetime import date


def mainMenu():
    my_budget = Budget()
    my_record = Transaction()

    while(True):
        print("\n--------------------------MENU-------------------------------")
        print("1 = SET BUDGET")
        print("2 = SET TRANSACTION")
        print("3 = SEE TRANSACTION HISTORY")
        print("4 = SEE BUDGET HISTORY")
        print("5 = EXIT")
        print("-------------------------------------------------------------\n")

        selection = 0
        try:
            selection = int(input("Enter choice: "))
        except:
            print("Wrong format!!!")
            mainMenu()

        if selection == 1:
            try:
                budgetName = input("Enter budget name: ")
                budgetAmount = int(input("Enter your budget amount: "))
                my_budget.date = date.today()
                my_budget.setBudget(budgetName, budgetAmount)
                print("\n")
            except:
                print("Wrong format!!!")
                mainMenu()

        elif selection == 2:
            try:
                recordName = input("Enter transaction name: ")
                recordAmount = int(input("Enter your transaction amount: "))
                recordDate = input("Enter your transaction date: ")

                my_record.Add_Transaction(recordName, recordAmount, recordDate)
            except:
                print("Wrong format!!!")
                mainMenu()

        elif selection == 3:
            my_record.get_all_transc()

        elif selection == 4:
            my_budget.seeHistory()

        elif selection == 5:
            break

        else:
            break


print("\n** WELCOME TO ULTIMATE TRACKER **")
print("WHAT DO YOU WANT TO DAY?:")
mainMenu()
