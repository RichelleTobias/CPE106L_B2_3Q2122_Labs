"""
Program: VendingMachineClass.py
Created by Richelle Louise Tobias (GROUP 6)
Class VendingMachine for Ice Cream Vending Machine Project
"""
import InventoryClass

class VendingMachine:

    #Constructor
    def __init__(self):

        #Money accepted by the machine (Php 20 and 50 peso bills)
        self.money = (20, 50)

        #Initializing total money inserted in the vending machine to float zero 
        self.money_inserted = 0.00


    #function for displaying items available in the ice cream vending machine
    def display_ice_cream(self):

        print("Welcome to the Ice Cream Vending Machine!")

        #Declaring the Inventory Class from InventoryClass.py to a variable
        inventory = InventoryClass.Inventory()
        
        #item_code variable lists pairs of values as declared in items list using enumerate method
        for item_code, item in enumerate(inventory.items, start = 1):
            #prints the pair values with the corresponding item code in the console for the vending machine program
            print(f"[{item_code}] {item.name} (Php {item.price:.2f}) Available: {item.quantity}")



    #function for analyzing user input for inserting money into the vending machine
    def receive_money(self, money):
        
        #if-else statement for invalid bills inserted in the vending machine
        if float(money) not in (self.money):
            # .format(self.money) ---> passes values from self.money to {} inside a string
           print ('We only accept cash in these denominations: {}. ' .format(self.money), '\n\n')
        else: 
            #addition assignment operator to return the total input values for the self.money_inserted variable
            self.money_inserted += money

