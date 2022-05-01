"""
Program: CashBox.py
Created by Vien Rissy Santos (GROUP 6)
Class CashBox for Ice Cream Vending Machine Project
"""
import InventoryClass

class CashBox:

    #Constructor
    def __init__(self):

        #Initializing total money inserted in the vending machine
        self.total_inserted_cash = 0.00

        #Initializing total change left in the vending machine
        self.left_change = 2600.00

    #function for computing total cash inserted
    def get_total_inserted_cash(self, cash):
        self.total_inserted_cash += cash
        return self.total_inserted_cash 
    
    #function for computing total change left
    def get_total_left_change(self, cash, price):
        self.total_left_change = 2600 - (cash - price)
        return self.total_left_change
