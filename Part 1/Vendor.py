"""
Username: aancha.14.2025
Name: Aanchala Bhongade
Student no.: 2830709
Part 1: Vendor Class; Text Based Flower Shop Simulation.
Brief: This script represents Vendors. It stores vendors details and
       pricing for inventory items, which gives simulation objects during
       the restocking of greenhouse.
"""
class Vendor:
    """Defining the class for Vendor"""
    def __init__(self, name, prices):
        """Initialising the name and price attributes for Vendor"""
        self.name = name
        self.prices = prices

    def __str__(self):
        return self.name

