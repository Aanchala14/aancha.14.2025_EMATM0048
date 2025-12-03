"""
Username: aancha.14.2025
Name: Aanchala Bhongade
Student no.: 2830709
Part 1: Florist Class, Text Based Flower Shop Simulation.
Brief: In this python script, I have defined, Florists class and
       specialisedflorists subclass. This script initialise florists
       name and their specialisation if any. It uses Polymorphism
       and Inheritance to handle different time required to make
       particular bouquet based on their specialisation.
"""
class Florist:
    """
    Class defined for florists.
    The class defines the florists without specialisation.
    """
    def __init__(self, name):
        """initialising the florist name"""
        self.name = name
        self.speciality = None # florists with no specific speciality


    def get_speed (self, bouquet_type):
        """
        This returns us to the time taken for specific bouquet.
        Florist without speciality takes 1.0 (100%) of the time.
        """
        return 1.0

    def __str__(self):
        return self.name

class Specialisedflorist(Florist):
    """
    This is the subclass of Florist for specialised florist.
    Using inheritance, we inherit here using Florists overriding from bouquet type.
    """
    def __init__(self, name, speciality):
        super().__init__(name) #Intialising the parent attributes
        self.speciality = speciality

    def get_speed(self, bouquet_type):
        """
        By Polymorphism: overriding the parent method.
        it returns 0.5, half the time if bouquet type matches speicality.
        """
        if bouquet_type == self.speciality:
            return 0.5
        return 1.0

    def __str__(self):
        return f"{self.name} (specialises in {self.speciality})"
