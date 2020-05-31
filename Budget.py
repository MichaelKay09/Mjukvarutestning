import os
import sys
from datetime import date


class Budget():
    budget_id = 0
    budget_name = ""
    budget_amount = 0
    budgetlist = []
    date = 0

    def setBudget(self, name, amount):
        try:
            if(amount <= 0):
                print("Please enter amount in right format")

            else:
                self.budget_name = name
                self.budget_amount = int(amount)
                Budget.budgetlist.append(
                    [self.budget_name, self.budget_amount, self.date, self.budget_id])
                Budget.budget_id += 1
                print("Budget for {} has been created and {} has been added to it".format(
                    self.budget_name, self.budget_amount))
        except:
            print("Error!!!")

    def seeHistory(self):
        num = 0
        if(len(Budget.budgetlist) <= 0):
            print("No records has been registered!!!")
        else:
            for i in Budget.budgetlist:
                print(str("{}. {}".format(num, i[:2])))
                num += 1

    def find_budget_name(self, num):
        my_num = int(num)
        return str(Budget.budgetlist[my_num][0])

    def update_budget(self, index, amount):
        if(amount <= 0):
            print("ERROR COULD NOT ADD TRANSACTION!!!")

        else:
            transaction_added = False
            indx = int(index)
            mybudget = Budget.budgetlist[indx][1]
            if(mybudget < amount):
                print("Not enough Money in your account!!!")
            else:
                nybudget = mybudget - amount
                Budget.budgetlist[indx][1] = nybudget
                print("Transaction Added")
                transaction_added = True
            return transaction_added
