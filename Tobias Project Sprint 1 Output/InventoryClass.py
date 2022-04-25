"""
Program: InventoryClass.py
Created by Richelle Louise Tobias (GROUP 6)
Class Inventory for Ice Cream Vending Machine Project

N0TE: PATULOY NALANG NG PROGRAM FOR THIS CLASS
"""

import IceCreamConeClass

class Inventory:

    def __init__(self):

        #Declaring the names, price, and quantity variables from IceCreamCone class in IceCreamConeClass.py
        self.items = [
            IceCreamConeClass.IceCreamCone("Vanilla Ice Cream Cone", 15.00, 20),
            IceCreamConeClass.IceCreamCone("Chocolate Ice Cream Cone", 15.00, 20),
            IceCreamConeClass.IceCreamCone("Strawberry Ice Cream Cone", 20.00, 20),
            IceCreamConeClass.IceCreamCone("Ube Ice Cream Cone", 25.00, 20)
        ]