"""
Your task is to design and implement a class in a programming language. 
This class will represent a person and hold personal data.

Assignment Steps:

1. Class Creation: 
Design a class named Person with the following data: name, address, age, and phone number.

2. Accessor and Mutator Methods: 
Write get and set methods for each piece of data.
These methods allow you to access and change the data safely.

3. Creating Instances: 
Write a program that creates three instances (objects) of the Person class. 
Use one instance for your made-up information and the other two for imaginary friends 
or family members.

4. Display Data: 
Print out the information stored in each instance. Ensure the output is formatted 
and easy to read. You need to print out all the data for each. You can create a method 
that prints everything or call each get function one at a time.
"""

class Person: #class named person
    
    """ design a class named person w/ name, address, age & phone number """

    def __init__(self, name, address, age, phone_number): #initializer w/private variables

        self.__name = name #private variable name
        self.__address = address #private variable address
        self.__age = age #private variable age
        self.__phone_number = phone_number #private variable phone number

    """ get & set methods for each piece of data"""

    def get_info(self): #get person's info as a formatted string
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, Phone number: {self.__phone_number}"

    def get_name(self): #getter for name
        return self.__name 
    
    def get_address(self): #getter for address
        return self.__address
    
    def get_age(self): #getter for age
        return self.__age
    
    def get_phone_number(self): #getter for phone number
        return self.__phone_number
    
    def set_name(self, name): #setter for name
        self.__name = name

    def set_address(self, address): #setter for address
        self.__address = address

    def set_age(self, age): #setter for age
        self.__age = age

    def set_phone_number(self, phone_number): #setter for phone number
        self.__phone_number = phone_number

""" write a program for 3 instances of the Person class. 
     1) your made up info
     2) 2 imaginary friends or family members """
    
person1 = Person("Diamond", "123 Mine Dr", 27, "123-456-789") #made up info for me
person2 = Person("Joe", "456 Desert St", 15, "234-567-891") #imaginary 1
person3 = Person("Mama", "789 River Ave", 50, "567-891-0111") #imaginary 2

#display
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())