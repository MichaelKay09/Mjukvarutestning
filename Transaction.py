from datetime import date
from Budget import Budget


class Transaction(Budget):
    name, amount, date = "", "", ""
    transactions = []
    trans_id = 0
    budget = Budget()

    def Add_Transaction(self, name, amount, myDate):
        try:
            num = 0
            self.name = name
            self.amount = int(amount)
            if(len(Transaction.budgetlist) <= 0):
                print("Please set budget first")

            else:
                print(
                    "\nChoose the budget to add the transaction to from the list below")
                Transaction.Budget_list()
                print("\n")
                num = int(input("Write the number of your choice: "))
                budget_name = Transaction.budget.find_budget_name(num)
                Transaction.transactions.append("Name: {}, Amount: {}kr, Date: {}, Type: {}".format(
                    self.name, self.amount, myDate, budget_name))
                amount = int(amount)
                Transaction.budget.update_budget(num, amount)

        except:
            print("Wrong format!!!")

    def Budget_list():
        Transaction.budget.seeHistory()

    def get_all_transc(self):
        if(len(Transaction.transactions) <= 0):
            print("No records has been registered!!!")
        else:
            for x in Transaction.transactions:
                print(str(x))
