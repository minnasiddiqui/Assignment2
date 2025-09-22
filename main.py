import data
from sandwichmaker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    machine_on = True
    while machine_on:
        choice = input("What would you like? (small/medium/large/off): ")
        if choice == 'off':
            machine_on = False
        elif choice == "report":
            # just print resources directly
            print("Resources report:", sandwich_maker_instance.machine_resources)
        elif choice in ['small', 'medium', 'large']:
            sandwich_recipe = recipes[choice]
            order_ingredients = sandwich_recipe['ingredients']
            cost = sandwich_recipe['cost']

            #Check resources
            if sandwich_maker_instance.check_resources(order_ingredients):
                #Process the payment of customer using cashier instance
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, cost):
                    #Then make sandwich
                    sandwich_maker_instance.make_sandwich(choice, order_ingredients)
                    print(choice, "sandwich is ready. Bon appetit!")
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()