"""
Program: InventoryClass.py
Created by Kevin Rayne B. Samonte (GROUP 6)
Class Inventory for Ice Cream Vending Machine Project
"""

import IceCreamConeClass

class Inventory:

    def __init__(self):

        #Declaring the names, price, and quantity variables from IceCreamCone class in IceCreamConeClass.py
        self.items = [
            IceCreamConeClass.IceCreamCone("Vanilla Ice Cream Cone", 15.00, 20),
            IceCreamConeClass.IceCreamCone("Chocolate Ice Cream Cone", 15.00, 20),
            IceCreamConeClass.IceCreamCone("Strawberry Ice Cream Cone", 20.00, 20),
            IceCreamConeClass.IceCreamCone("Ube Ice Cream Cone", 25.00, 0)
        ]

    def isEmpty(self, current_quantity):
        if current_quantity == 0:
            print("The machine is empty, would you like to order another flavor")
            return True
        else:
            return False