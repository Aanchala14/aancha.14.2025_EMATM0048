class Vendor:
    """Defining the class for Vendor"""
    def __init__(self, name, prices):
        """Initialising the name and price attributes for Vendor"""
        self.name = name
        self.prices = prices

    def __str__(self):
        return self.name

