import os
import sys
from datetime import date


class Budget():

    def setBudget(self):
        self.budget = int(input("\nPlease enter your budget today: "))
        self.budget = 0
        self.budgetlist = []
        self.date = date
        self.datelist = []

        try:
            if self.budget <= 0:
                print("Please be serious and enter your budget for today!\n")
                self.setBudget()
            else:
                # "SPARA BUDGETEN I PROGRAMMET SÅ DEN KAN FÖLJA MED?"
                self.budget_list.append(self.budget)
                # Lägg till i TOTALT(expenses)
                print(self.budget, "kr  Budget has been added!", "  ",  date.today(), "\n\n")
        except:
            print("Please enter your budget!\n")
            self.setBudget()
