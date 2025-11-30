"""
Username: aancha.14.2025; Name: Aanchala Bhongade; Student no.: 2830709
Part 1: Text Based Flower Shop Simulation.
Brief: This script is the main script for running all the classes and functions, it takes all the input needed to run the simulation. It performs all the calculation
       needed in flower shop.
"""
#main script to run the Flower shop simulation
from Flower_Shop import Flower_Shop
from Vendor import Vendor

#Availaible vendors
vendor = [
    Vendor("Evergreen Essentials", {'roses': 2.80, 'daisies': 1.50, 'greenery': 0.95}),
    Vendor("FloraGrow Distributors", {'roses': 1.60, 'daisies': 1.20, 'greenery': 1.80})
]

def get_input(prompt, min_value=0, max_value=None):
    """For getting valid int input."""
    while True:
        try:
            value_str = input(prompt).strip()
            if not value_str:
                raise ValueError("Invalid input.")
            value = int(value_str)
            if value < min_value:
                raise ValueError(f"AtLeast need {min_value} value.")
            if max_value is not None and value > max_value:
                raise ValueError(f"AtLeast need {max_value} value.")
            return value
        except ValueError as e:
            print(f"Invalid: {e}. Please try again.")

def manage_florist(shop):
    """Adding and removing the florists as needed, with specialisation if has any."""
    while True:
        print(f"Current florists: {len(shop.florists)}")

        if len(shop.florists) == 4:
            print("Maximum florists capacity reached.")
        print("\nManage the florists?(add/rmv/na): ")
        choice = input().strip().lower()
        print()

        if choice == 'na':
            break
        elif choice == 'add':
            #check for number of florists
            if len(shop.florists) >= 4:
                print("Cannnot add more florists, reached maximum.")
                continue
            try:
                available_spots = 4 - len(shop.florists)
                count_input = input(f"How many florists you want to hire? (Max {available_spots}): ").strip()

                if not count_input.isdigit():
                    print("Please enter valid number.\n")
                    continue

                count = int(count_input)

                if count < 1:
                    print("Atleast 1 florists is must.")
                    continue
                if count > available_spots:
                    print(f"You can add {available_spots} more florists only.")
                    continue

                #looping for adding number of florists as requested by user
                for i in range(count):
                    print(f"Hiring  florists {i+1} of {count}......")
                    while True:
                        name = input("Enter a name: ").strip()
                        if not name:
                            print("This cannot be empty.\n")
                            continue
                        print("Does this florist has a speciality?(yes/no): ", end="")
                        speciality_input = input().strip().lower()
                        while speciality_input not in {'yes', 'no'}:
                            print("Invalid input. Please enter yes/no: ", end="")
                            speciality_input = input().strip().lower()

                        speciality = None
                        if speciality_input == 'yes':
                            print("Available bouquets are: Fern-tastic, Be-Leaf in Yourself, You Rose to the Ocassion")
                            speciality = input("Enter the bouquet type:").strip()
                            if speciality not in shop.bouquets:
                                print("Invalid input.\n")
                                continue
                        try:
                            shop.add_florist(name, speciality)
                            break
                        except ValueError as e:
                            print(f"Error: {e}")

            except ValueError as e:
                print(f"Invalid input: {e}")
        elif choice == 'rmv':
            if len(shop.florists) <= 1:
                print("Atleast 1 florists is must.")
                continue
            try:
                name = input("Enter a name to remove: ").strip()
                shop.remove_florist(name)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Please type 'add', 'rmv' or 'na'.\n")
def sales_plan(shop):
    """Validating the sales plan."""
    bouquet_types = list(shop.bouquets.keys())
    while True:
        print("\nHow many of each bouquet you want to sell?")
        plan = {}
        for bouq in bouquet_types:
            max_qty = shop.bouquets[bouq]['demand']
            qty = get_input(f"{bouq} (Max {max_qty}): ", 0, max_qty)
            plan[bouq] = qty
        try:
            #calling sales plan to handle the error
            shop.sales_plan(plan)
            return plan
        except ValueError as e:
            print(f"Plan rejected: {e}")

def choose_vendors(capatalise=None):
    """Choosing the vendor for each supply."""
    chosen = {}
    for supply in ['roses', 'daisies', 'greenery']:
        while True:
            choice = input(
                f"Where do you want to purchase {supply} from Evergreen Essentials(0) or FloraGrow Distributors(1)?\nPress (i) for info: ").strip().lower()
            if choice == 'i':
                print(f"Evergreen: £{vendor[0].prices[supply]:.2f}/bunch")
                print(f"FloraGrow: £{vendor[1].prices[supply]:.2f}/bunch")
                continue
            try:
                choice = int(choice)
                if choice not in [0, 1]: #handling input error
                    raise ValueError
                chosen[supply] = vendor[choice]
                break
            except ValueError:
                print("Invalid: Please enter 0, 1 or i.")
    return chosen

def main():
    """To run the simulation."""
    print("-----------------------WELCOME-----------------------")
    print("\nThis is the Flower Shop Simulation (made by Aanchala).")
    print("_____________________________________________________")
    shop = Flower_Shop()

    print("\nBefore starting, you have to decide for how many months you want to run the simulation.")

    months_input = input("For how many months you want to run the simulation? (default: 6):").strip().lstrip()
    if not months_input:
        print("Defaulting to 6 months.")
        months = 6
    else:
        try:
            months = int(months_input)
            if months < 1:
                print("Invalid value, must be atleast 1.")
        except ValueError:
            print("Invalid input. Defaulting to 6 months.")
            months = 6


    for month in range (1, months + 1):
        print(f"\nMonth: {month}")

        print("\nNow you have to manage employees and decide how many bouquets you want to sell of each type.")

        manage_florist(shop)
        while len(shop.florists) < 1:
            print("Error: Atleast 1 florist is must.")
            manage_florist(shop)


        plan = sales_plan(shop)
        print("_____________________________________________________")

        #Starting the month
        shop.total_sales(plan)

        print("Month ended.")
        print("_____________________________________________________")
        print("Calculations at end of month:")
        print(f"Balance cash, Month start: £{shop.cash:.2f}")


        #Calculation of income, by using map and lambda, mapped the plan items to price*qty, then adding.

        income = sum(map(lambda bouq: plan[bouq] * shop.bouquets[bouq]['price'], plan))

        print(f"Income: £{income:.2f}")
        print("Money spent:")

        try:
            flo_cost = shop.florists_payment()
            print(f"Employee costs: £{flo_cost:.2f}")

            rent_cost = shop.rent_payment()
            print(f"Rent: £{rent_cost:.2f}")

            greenhouse_cost = shop.restock_payment()
            print(f"Greenhouse restock cost: £{greenhouse_cost:.2f}")

            shop.depreciation_cost()
            shop.status()

            print("Greenhouse needs to be restocked.")
            chosen_vendors = choose_vendors()
            restock_cost = shop.restock_greenhouse(chosen_vendors)
            print(f"Flowershop restock cost: £{restock_cost:.2f}")
            print(f"Month end Cash Balance: £{shop.cash:.2f}")

        except ValueError as e:
            print(f"\nEnd of Simulation: {e}")
            break


    print("\n_________________________________________________________________")
    print("Simulation is now completed.")

if __name__ == "__main__":
    main()