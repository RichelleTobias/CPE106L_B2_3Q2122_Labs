"""
Program: CashBox.py
Created by Vien Rissy Santos (GROUP 6)
Class CashBox for Ice Cream Vending Machine Project
"""

class CashBox:

    #Constructor
    def __init__(self):

        #Initializing total money inserted in the vending machine
        self.total_cash = 0.00

        #Initializing total change left in the vending machine
        self.total_change = 2600.00

    #function for computing total cash inserted
    def get_total_cash(self, inserted_cash):
        self.total_cash += inserted_cash
        return self.total_cash
    
    #function for computing total change left
    def get_total_change(self, inserted_cash, price):
        self.total_change -= inserted_cash - price
        return self.total_change
