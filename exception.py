"""

Objective: Enhance a basic Python program by implementing try and except statements to handle 
errors in user input, focusing on data type errors.

Starting Code

# Simple Python program to calculate the square of a number

def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}.")

square_number()
    
Instructions
1. Understand the Code: Review the provided Python script. It calculates the square of a 
user-input number.
2. Identify Potential Errors: Consider errors that might occur with non-numeric input.
3. Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle 
incorrect data types with an error message.
4. Test Your Code: Ensure the exception handling works correctly with various inputs.
5. GitHub Upload: Upload your py file to GitHub and hand in the link

"""

def square_number(): #define square function
    while True: #creates infinite loop
        try: #try contains the code that might fail
            number = input("Enter a number to square: ") #user input stored as a number
            squared_number = int(number) ** 2 #squared number formula
            print(f"The square of {number} is {squared_number}.") #if arriving here, no errors
            break #exits loop after a successful valid input is made

        except ValueError: #in case of an improper value input
            print(f"That is not a valid input. Please enter a number: ") #prints error message

def main(): #define main function
    square_number() #calls squared number

main() #calls main