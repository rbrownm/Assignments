from BankAccount import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):

        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

        self.transfer_limit = transfer_limit
        self.transfers_performed = 0



    def transfer(self, transfer_amount, account_to_transfer):
        if self.transfers_performed >= self.transfer_limit:
            print("Transfer limit reached")
            return

        if self.current_balance - transfer_amount < self.minimum_balance:
            print("Not enough funds available!")
            return

        self.current_balance -= transfer_amount
        self.transfers_performed += 1
        account_to_transfer.deposit(transfer_amount)
