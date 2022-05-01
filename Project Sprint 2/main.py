"""
Program: main.py
Created by Richelle Louise Tobias/Kevin Rayne B. Samonte(GROUP 6)
Main Function for Ice Cream Vending Machine Project
"""

import InventoryClass 
import VendingMachineClass


#MAIN FUNCTION FOR USER INPUT

def main():

    #Declaring the VendingMachine Class from VendingMachineClass.py to a variable
    vending_machine = VendingMachineClass.VendingMachine()

    #Calling the display_items() function under the VendingMachine Class
    vending_machine.display_ice_cream()
    ctr = "1"
    #Declaring the Inventory Class from InventoryClass.py to a variable
    inventory = InventoryClass.Inventory() 
    while True:
        while True:
            try:
                user_input_item = int(input("\nPlease enter the item code #: "))
            except ValueError:
                continue
            if user_input_item in range(1, len(inventory.items)+1):
                break

        #Declaration of variable "ice_cream" using items variable list during user input - 1
        ice_cream = inventory.items[user_input_item-1]

        if inventory.isEmpty(ice_cream.quantity):
            continue
        
        #decrements the bought ice cream, needs to be renovated to update the original quantity in the inventory list
        ice_cream.quantity -= 1

        # "ice_cream.name" --> gets the chosen flavor of icecream
        print(f"\nYou've selected: {ice_cream.name} ")


        # "ice_cream.price : .2f" --> gets the price of the chosen icecream with 2 digits of precision 
        print(f"== Price: Php {ice_cream.price:.2f} == \n")
   
        while vending_machine.money_inserted < ice_cream.price:

            print(f"Current Inserted Cash: Php {vending_machine.money_inserted:.2f}")
        
            #When money inserted by the user is less than the chosen icecream price, user is asked to insert amount in machine. 
            while True:
                try:
                    #Variable converts user input of str or int into a float
                    user_money = float(input("Please enter the amount of money you'd like to insert (20 or 50): "))
                
                    #Calls the receive_money function in VendingMachine Class in VendingMachineClass.py using user input
                    vending_machine.receive_money(user_money)
                except ValueError:
                    continue
                else:
                    break
    
        #Message outputted by machine after successful purchase
        print("\nThank you for purchasing!")

        print(f"Please take your change: Php {vending_machine.money_inserted - ice_cream.price:.2f}")
        
        ctr = input("Do you want to have another oder? Please enter 1 if YES and 2 if NO: ")
        if ctr == "1":
            vending_machine.display_ice_cream() #Need to update since the decremention does not apply, the inventory resets
            continue
        else:
            break
            
        
    print("THANK YOU FOR USING THE ICE CREAM VENDING MACHINE")        
    return 0


if __name__ == "__main__":
    main()