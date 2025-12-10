""" 
    single dish or drink available
        role: stores details about items available
        attributes: name(string), category(string), price_small(float), price_medium(float), price_large(float)
        methods: __init__, get_details, getters and setters for all attributes
        self.__name, self.__category, self.__price_small, self.__price_medium, self.__price_large

Menu Item.py 
"""

class Menu_Item:
    """ represents single item on menu with category and prices for small, medium, and large"""
    #class attribute for defining and storing following categories
    CATEGORIES = ['Drinks', 'Bakery', 'Food'] 

    def __init__(self,category, name, price_small, price_medium, price_large):
        self.__category = category.strip().lower()
        self.__name = name
        self.__price_small = float(price_small)
        self.__price_medium = float(price_medium)
        self.__price_large = float(price_large)

    #getters

    def get_category(self):
        """returns category of item"""
        return self.__category
    
    def get_name(self):
        """returns name of item"""
        return self.__name
    
    def get_price_small(self):
        """returns price for size small"""
        return self.__price_small
    
    def get_price_medium(self):
        """returns price for size medium"""
        return self.__price_medium
    
    def get_price_large(self):
        """returns price for size large"""
        return self.__price_large
    
    #setters

    def set_category(self, category):
        """sets item's category, strips whitespace"""
        self.__category = category.strip()

    def set_name(self, name):
        """sets item's name, strips whitespace"""
        self.__name = name.strip()

    def set_price_small(self, price):
        """sets small item's price, create float"""
        self.__price_small = float(price)

    def set_price_medium(self, price):
        """sets medium item's price, create float"""
        self.__price_medium = float(price)
    
    def set_price_large(self, price):
        """sets large item's price, create float"""
        self.__price_large = float(price)

   #gets details

    def get_details(self):

        details = (
            f"\n-----Item Details-----\n"
            f"Category: {self.get_category()}\n"
            f"Name: {self.get_name()}\n"
            f"Price (S): {self.get_price_small():.2f}\n"
            f"Price (M): {self.get_price_medium():.2f}\n"
            f"Price (L): {self.get_price_large():.2f}\n"
        )
        return details #returns details
