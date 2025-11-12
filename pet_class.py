"""
Define a Pet Class:

1. Create private properties: owner_first_name, owner_last_name, 
pet_id, pet_name, and pet_type.

2. Set a default value for pet_type as "Dog".

3. Implement getter and setter methods for all properties.

4. Include a class variable vet_name set to the name of your veterinary office.

5. Add a method display_pet_info to print all details of the pet and owner.

Create Pet Objects:

1. Instantiate at least three pet objects with different details.
2. Show the use of setter methods for at least one pet object.

Implement Property Existence Check:

1. Write a function check_property that uses hasattr() to verify if a 
property exists in a pet object.

Display Information:
1. Use display_pet_info to print details for each pet.
2. Show three examples of check_property being used on various properties 
and pets.
3. Show two examples of display_pet_info on different instances of pet 
that you create.
"""

""" define a pet class w/private properties: OFN, OLN, PID, PN, & PT,
    default value for PT=Dog, getters & setters, CV name, + method to print all details"""

class Pet: #def pet class
    
    #class variable
    vet_name = "Dr. Airbud"

    #private properties
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"): #default value as Dog
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    #getters
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type
    
    #setters
    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value
    
    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value
    
    def set_pet_type(self, Dog):
        self.__pet_type = Dog

    #method to print all details of pet and owner
    def display_pet_info(self):
        print("Owner and pet details:", vars(self))

    #method to print basic info
    def print_info(self):
        print(self.__owner_first_name + "" + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)

#use of Pet class
def main():
    #instance, at least three objects
    pet1 = Pet("Danny","Hoover", '0233', "Thunder","Dog")
    pet1.print_info()

    #setter method to update pet1 new info
    print("\nSetter Method\n:")
    pet1.set_owner_first_name("Andrew")
    pet1.set_owner_last_name("Jackson")
    pet1.set_pet_id('0234')
    pet1.set_pet_name("Lightning")
    pet1.set_pet_type("Parrot")

    pet2 = Pet("Benny","Hana", '0244', "Star", "Iguana")
    pet3 = Pet("Billy", "Holiday", '0255', "Love", "Hamster")

    #at least two examples of display pet info
    pet2.display_pet_info()
    pet1.display_pet_info() #after update
    pet3.display_pet_info

    #three examples of check property and use hasattr()
    print(hasattr(pet1, "_Pet__pet_id"))
    print(hasattr(pet2,"get_owner_last_name"))
    print(hasattr(pet3,"favorite_food")) #does not exist and will return False

main() #call main