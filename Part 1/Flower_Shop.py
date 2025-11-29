import math
from Florist import Florist, Specialisedflorist

class Flower_Shop:
    """Defining the class for flower shop which manages cash, supplies and """
    def __init__(self):
        """Initialising the attributes, the total cash and full greenhouse capacity."""
        self.cash = 7500.0 #initial balance
        self.supplies = {
            'roses': 200,
            'daisies': 250,
            'greenery': 400
        }

        #defining dictionary for capacity
        self.capacity = {k: v for k, v in self.supplies.items()}
        self.depreciation_rates = {'roses': 0.40, 'daisies': 0.15, 'greenery': 0.05}
        self.restock_cost = {'roses': 1.50, 'daisies': 0.8, 'greenery': 0.20}
        self.florists = []

        #attributes for bouquets for florists
        self.bouquets = {
            'Fern-tastic': {
                'greenery': 4, 'roses' : 0, 'daisies': 2,
                'time': 20/60, 'price': 18.50, 'demand': 175
            },
            'Be-Leaf in Yourself': {
                'greenery': 2, 'roses': 1, 'daisies': 3,
                'time': 30/60, 'price': 17.75, 'demand': 100
            },
            'You Rose to the Occasion': {
                'greenery': 2, 'roses': 4, 'daisies': 2,
                'time': 45/60, 'price': 32.50, 'demand': 250
            }
        }
        self.florists_hourly_rate = 15.50
        self.florists_montly_hours = 80
        self.rent = 800.00

    def add_florist(self, name, speciality =None):
        """
        Defining object to add florists.
        If with speciality then specialisedflorist else florist
        """
        if len(self.florists) >= 4:
            raise ValueError("Cannot be more than 4 florist")
        if any(f.name == name for f in self.florists):
            raise ValueError("Duplicate Name")
        self.florists.append(Florist(name))
        if speciality:
            new_florist = Specialisedflorist(name, speciality)
            print(f"Added florist: {new_florist} with {speciality}.")
        else:
            new_florist = Florist(name)

        self.florists.append(new_florist)
        print(f"Added florist: {new_florist}")

    def remove_florist(self, name):
        """for removing florist by name"""
        if len(self.florists) <= 1:
            raise ValueError("Cannot remove; florist cannot be less than 1.")

        for i, f in enumerate(self.florists):
            if f.name == name:
                removed_name = self.florists.pop(i)
                print(f"Removed florist: {removed_name}")
                return
        raise ValueError("Florist not found")


    def sales_plan(self, user_demand):
        """
        For calculation of supplies and hours needed.
        Using Polymorphism to check florist speed.
        """
        bouq_supplies = {'roses': 0, 'daisies': 0, 'greenery': 0}
        total_hours = 0.0

        for bouq_type, qty in user_demand.items():
            if qty < 0 or not isinstance(qty, int):
                raise ValueError(f"{bouq_type}, this value cannot be negative.")

            #setting limit of bouquet sales according to the given demands
            limit = self.bouquets[bouq_type]['demand']
            if qty > limit:
                raise ValueError(f"f{bouq_type}, cannot exceed the monthlu demand ({limit}).")

            #Calculation of the supplies
            for supply in bouq_supplies:
                bouq_supplies[supply] += qty * self.bouquets[bouq_type][supply]

            time = self.bouquets[bouq_type]['time']
            half_time = time/ 2

            #For checking the time taken we are using Polymorphism.
            #Instead using "if f.specialty == bouq_type", we ask object.
            #Using get_speed here to know if it is 0.5(half_time)?

            specialised_employees = [f for f in self.florists if f.get_speed(bouq_type) == 0.5]
            num_employees = len(specialised_employees)

            #Calculating the capacity for specialised employees
            spec_capacity = num_employees * self.florists_montly_hours/ half_time

            if qty <= spec_capacity:
                total_hours += qty * half_time
            else:
                total_hours += spec_capacity * half_time + (qty - spec_capacity) * time

        available_hours = len(self.florists) * self.florists_montly_hours
        if total_hours > available_hours:
            raise ValueError(f"Labour hours insufficient: Needs {total_hours:.2f} hours, available {available_hours} only.")

        for supply, needed in bouq_supplies.items():
            if needed > self.supplies[supply]:
                raise ValueError(f"{supply} is not enough, we need {needed} and available is {self.supplies[supply]} only.")

        return bouq_supplies

    def total_sales(self, plan):
        """
        consumption of supplies and revenue earned by total sales.
        """
        #Replenishing greenhouse
        new_supplies = self.sales_plan(plan)

        #Revenue calculation
        revenue = sum(qty * self.bouquets[bouq]['price'] for bouq, qty in plan.items())
        self.cash += revenue

        #Supply consumption
        for supply, needed in new_supplies.items():
            self.supplies[supply] -= needed

        print("----****** THIS MONTH IS COMPLETED ******----")

    def florists_payment(self):
        """Payments to florists."""
        flo_pay = len(self.florists) * (self.florists_montly_hours * self.florists_hourly_rate)
        self.cash -= flo_pay
        if self.cash < 0: #checking for bankruptcy
            raise ValueError("Bankrupt: Not enough cash to pay florists.")
        return flo_pay

    def rent_payment(self):
        """Payment of the greenhouse rent."""
        self.cash -= self.rent
        if self.cash < 0:
            raise ValueError("Bankrupt: Not enough cash to pay greenhouse rent.")
        return self.rent

    def restock_payment(self):
        """Cost needed to replenish and maintaining the greenhouse"""
        cost = sum(qty * self.restock_cost[supply] for supply, qty in self.supplies.items())
        self.cash -= cost
        if self.cash < 0:
            raise ValueError("Bankrupt: Not enough cash to restock.")
        return cost

    def depreciation_cost(self):
        """Calculation for depreciation of supplies left after sales."""
        for supply in self.supplies:
            qty = self.supplies[supply]
            #using math's ceil for loss calculation
            loss = math.ceil(qty * self.depreciation_rates[supply])
            self.supplies[supply] = max(0, qty - loss) #supplies used in sales

    def status(self):
        """Showing the current status of the Flower shop."""
        print("\nCurrent Flower shop status:")
        print(f"Staff: {len(self.florists)}")
        for f in self.florists:
            #using __str__ method of specialised florists class
            print(f"- {f}")
        print("Remaining supplies in greenhouse:")
        for supply, qty in self.supplies.items():
            print(f"{supply.capitalize()}: {qty}")
        print(f"Cash Balance: £{self.cash:.2f}")

    def restock_greenhouse(self, choosen_vendors):
        """Replenishing greenhouse with the choosen vendor."""
        total_cost = 0.0
        for supply in self.supplies:
            needed = self.capacity[supply] - self.supplies[supply]
            if needed > 0:
                vendor = choosen_vendors[supply]
                cost = needed * vendor.prices[supply] #cost of vendor
                total_cost += cost
                self.supplies[supply] += needed

        self.cash -= total_cost
        if self.cash < 0: #checking for bankruptcy for replenishing supplies
            raise ValueError("Bankrupt: Not enough to pay vendor for replenishing supplies.")
        return total_cost

 









