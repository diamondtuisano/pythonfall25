"""
Main program for Final Project

Cafe Ordering System
    Diamond Tuisano
    Programming Logic ADD-100-004L
    8/19/2025-12/13/2025
    Date: 12/09/2025

Program flow:

    imports menu, menu items, and order classes
    
    functions:
    1. Loads menu data.
    2. Takes customer information.
    3. Prompts user to add items to their order until they type 'done'.
    4. Prints their receipt including quantity, price of each item, and total. 

main.py

"""

from MenuItem import Menu_Item
from Menu import Menu
from CafeOrder import Cafe_Order

def main():
    """ functions:
    1. Loads menu.
    2. Takes cusomter info.
    3. Prompts user to add items to their order until they type 'done'.
    4. Prints their receipt. 
    """

    #initialize menu and load data + display offical menu
    #defines file_path and stores it as variable for where to load file
    cafe_menu_official = Menu()
    file_path = "final_project/data/menu_data.txt" 
    cafe_menu_official.load_file(file_path)
    cafe_menu_official.display_menu()

    #order setup details + create a CafeOrder object
    customer_name = input("\nEnter your name: ").strip()
    order_number = 1
    current_order = Cafe_Order(customer_name, order_number)

    #order loop
    print("\nStart your order")
    print("Type 'done' to finish your order and checkout!")
    
    while True:
        user_input = input("\nEnter item name (or type 'done' after ordering): ").strip() #cleans up any white space

        if user_input.lower() == 'done':
            break #exits order loop and proceeds to checkout

        menu_item = cafe_menu_official.get_item(user_input)

        #check if item exists in menu
        if menu_item is None:
            print(f"Error: {user_input} is not found in Cafe Menu. Please try again.")
            continue #allows person to continue ordering even if they mistyped

        #get size and quantity
        print(f"\nItem selected: {menu_item.get_name()}\n")
        print(f"\nSmall: ${menu_item.get_price_small(): .2f} | Medium: ${menu_item.get_price_medium(): .2f} | Large: ${menu_item.get_price_large(): .2f}\n")

        size = input("Enter size (Small, Medium, or Large): ").strip() #cleans up any white space

        #monitor errors
        try:
            quantity_input = input("Enter quantity (default is 1): ") #prompts user for quantity of item(s)
            
            quantity = 0 #initalizes quantity
            if not quantity_input: #checks for empty output
                quantity = 1 #if input is empty e.g. someone just presses 'enter', quantity is set to 1
            else: #if user inputs a number
                quantity = int(quantity_input) #converts quantity input into an integer
            
            if quantity < 1: #invalid for ordering from a cafe
                raise ValueError #triggers ValueError
            
        except ValueError: #catches errors e.g. someone typed 'two' or -2
            print("Invalid quantity. Please enter a number > 0.")
            continue #restarts loop

        #add item to the order
        current_order.add_item(menu_item, size, quantity)
            
    #calculate final total
    print("\n----------Final Checkout----------\n")
    if current_order.calculate_total() > 0:
    #display final receipt runs after 'done' is entered
        print(current_order.print_receipt())
    else: #if they just typed 'done' instead of ordering something
        print("\n No items were ordered! :( Goodbye!")

if __name__ == '__main__': #allow main to run
    main()