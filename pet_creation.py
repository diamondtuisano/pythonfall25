"""
1. Create the Pet Class:
a. Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
b. Implement get and set methods for each of these attributes.
c. Add a method called print_details that prints the details of the pet.

2. Create Instances:
a. Create three objects of the Pet class with different kinds, breeds, and names.
b. Call the print_details method for each object that you created

3. Demonstrate a Special Method or Function:
a. Choose three of the following and demonstrate its use with the Pet class instances:
#1 __name__: Display the name of the class.
#2 type(): Show the class used to instantiate a pet object.
#3 __module__: Return the module name in which the Pet class is defined.
#4 __bases__: Display the base classes of the Pet class (if any).
#5 isinstance(): Check if an instance is of the Pet class.

Submission Requirements:
Submit the Python script containing the Pet class definition and instances by uploading 
it to your GitHub repository and submitting the link.
Include comments to demonstrate the usage of the chosen special method or function.
Ensure code follows Python best practices for readability and efficiency.
"""

class Pet: 
    """ 1a. pet class w/attributes"""

    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    #1.b getters
    def get_kind(self):
        return self.__kind

    def get_breed(self):
        return self.__breed

    def get_name(self):
        return self.__name

    #1.b setters
    def set_kind(self, value):
        self.__kind = value

    def set_breed(self, value):
        self.__breed = value

    def set_name(self, value):
        self.__name = value

    #1.c print details
    def print_details(self):
        print(self.__kind)
        print(self.__breed)
        print(self.__name)

def main():
    """ 2.a create instances of (3) objects w/different kinds, breeds, & names"""
    pet1 = Pet("Fish", "Goldfish", "Goldie")
    pet2 = Pet("Cat", "Siamese", "Lucky")
    pet3 = Pet("Bird", "Parrot", "Tweety")

    #2.b call print_details
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

    #3.a #2 type() special method/function w/instances
    print(type(pet1))
    print(type(pet2))
    print(type(pet3))

    #3.a #1 __name__ special method/function w/instances
    print(Pet.__name__)

    #3a. #5 isinstance() special method/function w/instances
    print(isinstance(pet1,Pet))
    print(isinstance(pet2,Pet))
    print(isinstance(pet3,Pet))

main()