"""
Username: aancha.14.2025; Name: Aanchala Bhongade; Student no.: 2830709
Part 1: Vendor class; Text Based Flower Shop Simulation.
Brief: In this script, class for vendor is defined, initialising for name and price attributes for vendors at the time of replenishing greenhouse. This class is
       imported in main script.
"""
class Vendor:
    """Defining the class for Vendor"""
    def __init__(self, name, prices):
        """Initialising the name and price attributes for Vendor"""
        self.name = name
        self.prices = prices

    def __str__(self):
        return self.name

