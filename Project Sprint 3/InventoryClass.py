"""
Program: InventoryClass.py
Created by Kevin Rayne B. Samonte (GROUP 6)
Class Inventory for Ice Cream Vending Machine Project
"""

import IceCreamConeClass

class Inventory:

    def __init__(self):

        self.items = [
            IceCreamConeClass.IceCreamCone("Vanilla Ice Cream Cone", 15.00, 20),
            IceCreamConeClass.IceCreamCone("Chocolate Ice Cream Cone", 15.00, 20),
            IceCreamConeClass.IceCreamCone("Strawberry Ice Cream Cone", 20.00, 20),
            IceCreamConeClass.IceCreamCone("Ube Ice Cream Cone", 25.00, 2)
        ]

    def isEmpty(self, current_quantity):
        if current_quantity == 0:
            ctr = input("The machine is empty, Would you like to order another flavor? Enter 1 if YES 2 if NO: ")
            if ctr == "1":
                return True
            else:
                print("\nThank you for using our vending machine!\n")
                exit()
        else:
            return False
