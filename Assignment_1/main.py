### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

        if self.machine_resources['bread'] < ingredients['bread']:
            print(f"Sorry there is not enough bread")
            return False
        if self.machine_resources['ham'] < ingredients['ham']:
            print(f"Sorry there is not enough ham")
            return False
        if self.machine_resources['cheese'] < ingredients['cheese']:
            print(f"Sorry there is not enough cheese")
            return False

        return True

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

### Make an instance of SandwichMachine class and write the rest of the codes ###