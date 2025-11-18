"""
Part1
1) File 1: Write an Employee class with the following attributes:
a. Employee name
b. Employee number

2) Create a subclass named ProductionWorker that inherits from Employee. 
This subclass should include additional attributes:

a. Shift number (integer: 1 for day, 2 for night)
b. Hourly pay rate

3) Implement accessor and mutator methods (getters and setters) 
for each class.

Part2 Write a script to:
1. Create an instance of ProductionWorker.
2. Prompt the user for each attribute's data.
3. Store and then display the data using the object's methods.
"""
class Employee:
    """employee class w/employee name & number"""
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    """get & set + print employee info"""
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
    def set_name(self, value):
        self.__name = value
    
    def set_number(self, value):
        self.__number = value

    def print_employee_info(self):
        print(f"Employee name: {self.__name}")
        print(f"Employee number: {self.__number}")

class ProductionWorker(Employee):
    """subclass ProductionWorker w/shift number & pay rate"""
    def __init__(self, name, number, shift_number, pay_rate):
        super().__init__(name, number) #already in Employee
        #new additions
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    """get & set + shift number & pay rate"""
    def get_shift_number(self):
        return self.__shift_number
    
    def get_pay_rate(self):
        return self.__pay_rate
    
    def set_shift_number(self, value):
        self.__shift_number = value
    
    def set_pay_rate(self, value):
        self.__pay_rate = value

    def get_shift_name(self):
        """converts integer to shift name, used if/elif/else"""
        if self.__shift_number == 1:
            return "Day"
        elif self.__shift_number == 2:
            return "Night"
        else:
            return "Invalid shift number"

def main():
    """user input w/employee info"""
    print(f"\nEnter the following information for the Employee\n")
    
    name_input = str(input("Enter Employee Name: "))
    number_input = int(input("Enter Employee Number: "))
    pay_rate_input = float(input("Enter Pay Rate: ")) 
    shift_input = int(input("Enter Shift Number (1 for Days, 2 for Nights): ")) 
    
    worker = ProductionWorker(name_input, number_input, shift_input, pay_rate_input)

    """ create an instance of ProductionWorker w/all data;
    display the data using the object's methods; get"""
    
    print(f"-------------------------------------------")
    print(f"Employee Details: ")
    print(f"-------------------------------------------")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    print(f"Pay Rate: {worker.get_pay_rate(): .2f}") 
    print(f"Shift: {worker.get_shift_name()}")

if __name__ == "__main__": #code only runs when executed
    main()
