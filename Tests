import unittest
from Budget import Budget
from Transaction import Transaction


class BudgetAndTransactionTest(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        super(BudgetAndTransactionTest, self).setUp(*args, **kwargs)
        self.budget_object = Budget()
        self.transaction_object = Transaction()
        self.budget_object.setBudget(name='Another Budget', amount=500)
        # self.transaction_object.Add_Transaction(name='A test transaction', amount=10, myDate='02/06/2020')

    def test_set_budget(self):
        _budget = self.budget_object.setBudget(name='Test Budget', amount=1000)
        self.assertEqual(_budget, 1000)
        self.assertEqual(self.budget_object.budget_name, 'Test Budget')
        self.assertEqual(self.budget_object.budget_amount, 1000)

    def test_see_history(self):
        _budget_list = self.budget_object.seeHistory()
        self.assertEqual(isinstance(_budget_list, list), True)
        self.assertEqual(self.budget_object.budgetlist, _budget_list)

    def test_find_budget_name(self):
        _budget_name = self.budget_object.find_budget_name(num=0)
        print(_budget_name)
        self.assertEqual(isinstance(_budget_name, str), True)
        self.assertEqual(_budget_name, 'Another Budget')

    def test_update_budget(self):
        _updated_budget = self.budget_object.update_budget(index=0, amount=400)
        self.assertEqual(_updated_budget, True)

    def test_add_transaction(self):
        self.transaction_object.Add_Transaction(name='Buy a book', amount=15, myDate='01/06/2020')
        self.assertEqual(self.transaction_object.amount, 15)
        self.assertEqual(self.transaction_object.name, 'Buy a book')

    def test_budget_list(self):
        _budget_list = self.transaction_object.Budget_list()
        self.assertEqual(isinstance(_budget_list, list), True)
        self.assertEqual(self.budget_object.budgetlist, _budget_list)

    def test_get_all_transactions(self):
        _transactions = self.transaction_object.get_all_transc()
        self.assertEqual(isinstance(_transactions, list), True)
        self.assertEqual(self.transaction_object.transactions, _transactions)


if __name__ == '__main__':
    unittest.main()
