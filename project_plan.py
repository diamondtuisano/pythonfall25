"""
1. Project API Skeleton: project_plan.py

2. Top-of-file header docstring with the full plan prompt and 
student info (name, course, section, date).

3. Class stubs: define class names; include a concise class docstring 
describing role, key attributes, and key methods (no implementation yet).

4. Function stubs: function names and parameter lists; bodies may be pass. 
Each function has a docstring for purpose, parameters, and return value.
No GUI/wireframe required.

5. Class Diagram: PDF or PNG (simple UML or labeled boxes/arrows) 
showing classes and relationships.

6. Text I/O Storyboard (one page): sample prompts → typical inputs → 
formatted outputs, plus a brief file-format spec with a 5–10 line example.

7. Rubric Mapping Checklist: show where each final-project rubric row 
will be satisfied (file + class/function).

Submission: Push these to GitHub and submit the repo URL in Canvas.

"""

#2
""" Cafe Ordering System
    Diamond Tuisano
    Programming Logic ADD-100-004L
    8/19/2025-12/13/2025
    Date: 11/11/2025
 """

#3 & 4
class MenuItem:
    """ single dish or drink available
        role: stores details about items available
        attributes: name(string), price(float), category(string)
        methods: __init__, get_details"""

    def __init__(self, name, price, category):
        """ name of menu item: croissant
        price of item: $4.00
        category: drink or pastry, in this case pastry"""
        
    def get_details(self):
        """ formatted string w/item name, price, and category
            returns string with menu"""
        
class Menu:

    """ all MenuItems
        role: has all available items
        attributes: items (list of different menu items)
        methods: __init__, add_item, display_menu, get_item"""

    def __init__(self):
        """ initializes new menu"""

    def add_item(self, MenuItem, quantity):
        """ adds menu items and quantity
        item: menu item being ordered
        quantity: number of times that item is added/multiplied to receipt"""

    def display_menu(self):
        """ creates formatted string of all available menu items
            returns formatted string of entire menu"""

    def get_item(self):
        """ gets menu item by name
            returns matching name"""

class Order:
    """ single transaction of customer order
        role: tracks items from customer, calculates final cost, creates receipt
        attributes: customer_name(string), order_number(integer), items_ordered (list),
        tip(float), total cost(float)
        methods: __init__, add_item, calculate_total, print_reciept"""

    def __init__(self, customer_name, order_number):
        """ gets order, customer details
            customer name: Jane
            order number: 001"""

    def add_item(self, item, quantity, tip): #is this the right place for tip?
        """ adds menu item, quantity, tip
        item: MenuItem being ordered
        quantity: amount of times that item is being ordered
        tip: optional tip percentage; none, 10%, 20%, 25% """

    def calculate_total(self):
        """ calculates total and tip
            returns final cost""" #should I include tax?
        
    def print_receipt(self):
        """complete formatted reciept with items, quantity of items, subtotal, tip, and 
            final total
            returns a formatted string"""