##### MAIN MENU #####
from Budget import Budget
from Transaction import Transaction

class Ultimatetracker(Budget):

  def init(self):
        self.mainMenu()

  def mainMenu(self):

        print("** WELCOME TO ULTIMATE TRACKER **\n")
        print("WHAT DO YOU WANT TO DAY?:")
        try:

            print("1 = SET BUDGET")
            print("2 = SET TRANSACTION")
            print("3 = SEE HISTORY")
            print("4 = EXIT")

            selection=int(input("Enter 1-4: "))


            if selection==1: 
                Budget.setBudget(self)
                self.mainMenu()
            elif selection==2:
                Transaction.__init__(self)
                self.mainMenu()
            elif selection==3:
                self.seeHistory()
            elif selection==4:
                exit
            else:
                print("INVALID")
                print("Try again!")
                self.mainMenu()
        except:
            print("Write a number from 1-6 \n")
            self.mainMenu()



if name == 'main':

    Ultimatetracker()
