import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        response = input("What would you like? (small/ medium/ large/ off/ report): ")

        if response == "off":
            break

        elif response == "report":
            print(f'Bread: {sandwich_maker_instance.machine_resources["bread"]} slice (s)')
            print(f'Ham: {sandwich_maker_instance.machine_resources["ham"]} slice (s)')
            print(f'Cheese: {sandwich_maker_instance.machine_resources["cheese"]} pounds (s)')

        else:
            check_ingredients = sandwich_maker_instance.check_resources(recipes[response]['ingredients'])
            if not check_ingredients:
                continue

            else:
                print('Please insert coins.')
                coins_inserted = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins_inserted, recipes[response]['cost']):
                    sandwich_maker_instance.make_sandwich(response, recipes[response]['ingredients'])
                    print(f'{response} sandwich is ready. Bon appeti!')

if __name__=="__main__":
    main()
