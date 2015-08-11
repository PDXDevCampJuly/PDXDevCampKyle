"""An account file ofr our Simple bank."""

class Account:
    """An Account class that store account info"""

    def __init__(self, balance, person, account_type):
        self.balance = balance
        self.account_type = account_type
        self.owner = person

    def deposit(self, money):
        self.balance += money
        self.check_balance()

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds. Apply for a loan today!!")
        else:
            self.balance -= money
            self.check_balance()

    def check_balance(self):
        print("Your account balance is ${:,.2f}".format(self.balance))


class Person:
    """A class that tracks Persons in our bank."""

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.accounts = {}

    def open_account(self, init_balance, account_name, account_type = 'checking'):
        self.accounts[account_name] = Account(init_balance, self, account_type)
        print("Your account is open!")
        self.accounts[account_name].check_balance()

    def close_account(self, index):
        del self.accounts[index]
        print("Please come back when you have more money.")

    def list_accounts(self):
        for account_name, account in self.accounts.items():
            print("{} is a {} account with a balance of ${:,.2f}.".format(
                account_name,
                account.account_type,
                account.balance
            ))


class Bank:
    """Our top-level class; controls Persons and their Accounts."""

    def __init__(self):
        self.customers = {}
        self.savings_interest = 1.07

    def new_customer(self, first_name, last_name, email):
        self.customers[email] = Person(first_name, last_name, email)

    def remove_customer(self, email):
        del self.customers[email]

    def show_customer_info(self, email):
        customer = self.customers[email]
        print("\nCustomer: {}, {}\nEmail: {}\n".format(
            customer.last_name, customer.first_name, customer.email
        ))
        print("Accounts:\n" + ("-" * 40))
        customer.list_accounts()

    def customer_deposit(self, email, money, account_name):
        self.customers[email].accounts[account_name].deposit(money)

    def customer_withdraw(self, email, money, account_name):
        self.customers[email].accounts[account_name].withdraw(money)

    def make_customer_account(self, email, money, account_name, account_type="checking"):
        self.customers[email].open_account(money, account_name, account_type)

if __name__ == '__main__':
    bank = Bank()
    bank.new_customer("Kyle", "Joecken", "kjoecken@hotmail.com")
    bank.make_customer_account("kjoecken@hotmail.com", 1000, "Primary Checking")
    bank.make_customer_account("kjoecken@hotmail.com", 10000, "Primary Savings", "savings")
    bank.show_customer_info("kjoecken@hotmail.com")
