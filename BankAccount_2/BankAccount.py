class BankAccount:
    bank_title = 'Capital-One'


    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number


    def deposit(self, deposit_amount):
        self.current_balance += deposit_amount


    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.current_balance or self.current_balance - withdraw_amount < self.minimum_balance:
            print(f"Account balance does not meet requirements to withdraw ${withdraw_amount}")
            return
        self.current_balance -= withdraw_amount



    def print_customer_information(self):
        print(f"Bank Title: {BankAccount.bank_title}\n")
        print(f"Customer Name: {self.customer_name}\n")
        print(f"Customer Balance: {self.current_balance}\n")
        print(f"Minimum Balance: {self.minimum_balance}\n")
        print(f"Account Number: {self._account_number}\n")


