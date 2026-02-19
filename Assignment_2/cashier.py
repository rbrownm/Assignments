class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 0

        large_dollars = int(input("How many Large Dollars?: "))
        if large_dollars > 0:
            total += large_dollars

        half_dollars = int(input("How many Half Dollars?: "))
        if half_dollars > 0:
            total += half_dollars * .5

        quarters = int(input("How many Quarters?: "))
        if quarters > 0:
            total += quarters * .25

        nickels = int(input("How many Nickels?: "))
        if nickels > 0:
            total += nickels * .05

        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins == cost:
            print(f"Here is ${coins - cost:.1f} in change.")
            return True

        elif coins < cost:
            print(f"Sorry that's not enough money. Money Refunded.")
            return False

        else:
            print(f"Here is ${coins - cost:.2f} in change.")
            return True
