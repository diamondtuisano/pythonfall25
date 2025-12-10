"""
Main program for Final Project

Cafe Ordering System
    Diamond Tuisano
    Programming Logic ADD-100-004L
    8/19/2025-12/13/2025
    Date: 12/09/2025

To earn an “A” on the final project, your program must meet all of the following:

Object-Oriented Design:
At least two custom classes with attributes and methods.
Objects are used to manage data and actions in your program (not just defined and ignored).
Program Structure & Logic:
Uses functions and classes to organize the program into logical sections.
Includes at least one loop for repeated actions (e.g., menu, multiple entries).
Includes conditional statements (if/elif/else) to handle choices and branches.
Error Handling & Validation:
Uses input validation for user entries (e.g., non-numeric values, out-of-range options).
Includes at least one meaningful try/except block for anticipated errors (e.g., file issues, bad input).
File Input/Output (Text Files):
Reads from at least one external text file (e.g., menu, configuration, data list).
Writes to at least one external text file (e.g., receipt, log, report).
Uses clear filenames and simple, readable text formats (CSV-style or line-by-line are both fine).
Calculations & Output:
Performs at least one non-trivial calculation (e.g., totals, tax, discounts, scores, averages).
Displays formatted output that is easy for a user to read in the console.
Documentation & Readability: :contentReference[oaicite:1]{index=1}
Includes a top-of-file header docstring in the main file with:
Full assignment prompt (copied in) as required in this course.
Student name, course, section, date, and a short description of the project.
AI use disclosure with link if applicable (see AI policy below).
Each class and function includes a docstring describing:
What it does.
Key parameters (if any).
Return value (or “None” if it just prints or updates state).
Inline comments mark each logical section of the program.
Consistent, readable naming (no single-letter names except for simple loop counters).
User Experience & Creativity:
Text-based interface is clear and easy to follow (menus, prompts, labels).
Shows effort in theme, story, or presentation (even with a simple console UI).

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
    customer_name = input("\nEnter your name: ").strip() #strips customer name
    order_number = 1 #gives order number 1
    current_order = Cafe_Order(customer_name, order_number) #stores current order for receipt using Cafe_Order Class

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
