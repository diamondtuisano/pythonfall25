""" 
    role: has all available items through defining items
    attributes: items (list of different menu items)
    methods: __init__, add_item, get_item, display_menu, load_file

    import menu items
    
Menu.py 

"""

from MenuItem import Menu_Item

class Menu:

    """ all MenuItems
        role: has all available items
        attributes: items (list of different menu items)
        methods: __init__, add_item, get_item, display_menu, load_file
    """

    def __init__(self):
        """ initializes new menu"""
        self.__items = [] #private list holding MenuItem objects

    #methods

    def add_item(self, item_object):
        """ adds menu items"""
        self.__items.append(item_object)
       
    def get_item(self, name):
        """ gets menu item by name"""
        search_name = name.strip().lower()
        for item in self.__items:
            #compares item's name converted to lower case
            if item.get_name().lower() == search_name:
                return item #returns item

    def display_menu(self):
        """ creates formatted string of all available menu items
            returns formatted string of entire menu """
        
        print(f"\n---------------Cafe Menu---------------\n")

        #group items by category
        categories = {}
        for item in self.__items:
            category = item.get_category()
            if category not in categories:
                categories[category] = []
            categories[category].append(item)

        for category, item_list in categories.items():
            print(f"---{category.upper()}---")
            for item in item_list:
                print(f"{item.get_name()} S ${item.get_price_small(): .2f} | M ${item.get_price_medium(): .2f} | L ${item.get_price_large(): .2f} ")

    def load_file(self, file_path = "final_project/data/menu_data.txt"):
        """ reads menu data file """
        self.__items = []
        items_loaded = 0

        try: #checks for errors in opening and reading external file menu_data from variable file_path
            with open(file_path, 'r') as file:
                for line in file: #iterates line by line
                    line = line.strip() #cleans whitespace
                    if not line: #checks for blank lines
                        continue #skips to next line
                    
                    #split lines by comma, creating substrings
                    #iterates over each line in new list
                    #removes extra spaces
                    menu_items_by_line = [p.strip() for p in line.split(',')]

                    #checks that each line has 5 fields
                    if len(menu_items_by_line) == 5:

                        #extracts category, name, prices and assigns each element to an index
                        category = menu_items_by_line[0]
                        name = menu_items_by_line[1]
                        price_small = menu_items_by_line[2]
                        price_medium = menu_items_by_line[3]
                        price_large = menu_items_by_line[4]

                        #create new Menu_Item Object
                        new_item = Menu_Item(category, name, price_small, price_medium, price_large)

                        #adds to menu
                        self.add_item(new_item)
                        #tracks progress
                        items_loaded += 1
        
        except FileNotFoundError: #catches specific FileNotFound error
            print(f"Error: Menu not found at {file_path}.") #prints error message

        except Exception as e: #catches common error
            print(f"Error: {e}.") #prints error