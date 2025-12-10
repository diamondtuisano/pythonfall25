""" 
Single customer order transaction
Role: Tracks items ordered and calculates final cost
methods: __init__, add_item, calculate_total, print_receipt

CafeOrder.py

"""
from MenuItem import Menu_Item

class Cafe_Order:

    def __init__(self, customer_name, order_number):
        """ initializes new order w/customer and order details """
        self.__customer_name = customer_name.strip()
        self.__order_number = int(order_number)

        self.__items_ordered = []
        self.__total_cost = 0.0 #initialized at 0
    
    #methods: add_item, calculate_total, print_receipt

    def add_item(self, menu_item_object, size, quantity):
            """ adds a menu item to the order list and updates the total cost """
            try:
                quantity = int(quantity)
            except ValueError:
                print("Error: Quantity must be a whole number.")
                return

            size_item = size.strip().lower()
            price_per_item = 0.0 #initialized at 0

            #correct price based on size of item
            if size_item == 'small':
                price_per_item = menu_item_object.get_price_small()
            elif size_item == 'medium':
                price_per_item = menu_item_object.get_price_medium()
            elif size_item == 'large':
                price_per_item = menu_item_object.get_price_large()
            else:
                print(f"Error: Invalid size {size}.") #prints error message
                return #if size is valid

            item_cost = price_per_item * quantity #calculate item cost based on price item and amount

            item_data = {
                'item_object': menu_item_object,
                'name': menu_item_object.get_name(),
                'size': size_item,
                'quantity': quantity,
                'price_per_item': price_per_item,
                'item_total': item_cost
            }
            self.__items_ordered.append(item_data) #adds newly ordered item's details to master list

            #update total cost
            self.__total_cost += item_cost
            print(f"Added {quantity} x {size_item.capitalize()} {item_data['name']} = Total: ${self.__total_cost:.2f}")
    
    def calculate_total(self):
        """ returns calculated running total as a float """
        return self.__total_cost

    def print_receipt(self):
        """ creates a formatted receipt with items and final total """
        final_total = self.calculate_total()

        receipt_lines = [] #initializes receipt storage
        receipt_lines.append(f"\n Order # {self.__order_number} for: {self.__customer_name}\n") #adds receipt header

        #list items ordered
        #iterated loop for each item added
        for item in self.__items_ordered:
            item_line = (
                f"{item['quantity']} x {item['name']} ({item['size'].capitalize()})"
                f"${item['price_per_item']: .2f} for ${item['item_total']: .2f}"
            )
            receipt_lines.append(item_line) #adds each line to receipt
        
        #formats total line
        receipt_lines.append(f"\nTOTAL:{final_total: .2f}\n")
        receipt_lines.append(f"\nThank you! Have a great day! :) \n")

        #join receipt lines with a break on each line
        return "\n".join(receipt_lines)