from .account_project import Account
import unittest
import types


class AccountTests(unittest.TestCase):
    def setUp(self):
        self.account = Account('Alis', 1000)
        self.account.add_transaction(20)
        self.account.add_transaction(60)
        self.account.add_transaction(50)

    def test_init(self):
        self.assertEqual(self.account.owner, 'Alis')
        self.assertEqual(self.account.amount, 1000)
        self.assertEqual(self.account._transactions, [20, 60, 50])

    def test_add_transaction_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.account.add_transaction(12.5)

    def test_add_transaction(self):
        self.account.add_transaction(10)
        self.assertEqual(self.account._transactions, [20, 60, 50, 10])

    def test_balance(self):
        self.account.add_transaction(10)
        self.assertEqual(self.account.balance, 1140)

    def test_validate_transaction_static_method(self):
        self.assertTrue(isinstance(self.account.validate_transaction, types.FunctionType))

    def test_validate_transaction_raises_error(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account, -1030)

    def test_validate_transaction_add_amount(self):
        self.assertEqual(Account.validate_transaction(self.account, 150), "New balance: 1280")

    def test_custom_str(self):
        self.assertEqual(str(self.account), "Account of Alis with starting amount: 1000")

    def test_custom_repr(self):
        self.assertEqual(repr(self.account), "Account(Alis, 1000)")

    def test_custom_len(self):
        self.assertEqual(len(self.account), 3)

    def test_custom_getitem(self):
        self.assertEqual(self.account[1], 60)

    def test_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.assertEqual(self.account[4], 40)

    def test_custom_iter(self):
        self.assertEqual([self.account[t] for t in range(len(self.account))], [20, 60, 50])

    def test_custom_gt(self):
        account2 = Account('John', 560)
        account2.add_transaction(10)
        account2.add_transaction(-40)
        self.assertGreater(self.account, account2)

    def test_custom_ge(self):
        self.account2 = Account('John', 560)
        self.account2.add_transaction(10)
        self.account2.add_transaction(100)
        self.account2.add_transaction(460)
        self.assertGreaterEqual(self.account, self.account2)


    def test_custom_lt(self):
        self.account2 = Account('John', 1260)
        self.account2.add_transaction(10)
        self.account2.add_transaction(-40)
        self.assertLess(self.account, self.account2)

    def test_custom_le(self):
        self.account2 = Account('John', 1160)
        self.account2.add_transaction(10)
        self.account2.add_transaction(-40)
        self.assertLessEqual(self.account, self.account2)

    def test_custom_eq(self):
        self.account2 = Account('John', 1160)
        self.account2.add_transaction(10)
        self.account2.add_transaction(-40)
        self.assertEqual(self.account, self.account2)

    def test_custom_ne(self):
        self.account2 = Account('John', 1360)
        self.account2.add_transaction(10)
        self.account2.add_transaction(-40)
        self.assertNotEqual(self.account, self.account2)

    def test_custom_add(self):
        self.account2 = Account('John', 1500)
        self.account2.add_transaction(10)
        self.account2.add_transaction(-40)
        self.account_new = self.account + self.account2
        self.assertEqual(self.account_new.owner, self.account.owner + '&' + self.account2.owner)
        self.assertEqual(self.account_new.amount, self.account.amount+self.account2.amount)
        self.assertEqual(self.account_new._transactions, self.account._transactions+self.account2._transactions)

    def test_custom_reversed(self):
        self.assertEqual(reversed(self.account), [50, 60, 20])


if __name__ == '__main__':
    unittest.main()