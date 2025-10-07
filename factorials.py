"""

Assignment: Calculating Factorials
Objective: Write a Python program using a recursive function to calculate the factorial of a number. 
A recursive function is a function that calls itself to solve a problem.

Assignment Instructions:
1. Start by defining a function named factorial that takes one parameter, n, representing the number you're 
calculating the factorial for.
2. In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
3. For the recursive step, return n * factorial(n-1) if n > 1.
4. Prompt the user for a non-negative integer and call factorial, printing the result.

"""
def factorial(n): #defined factorial function with the parameter 'n'
    #base case of factorial, where factorial is 1
    if n == 1 or n ==0:
        return 1
    else: #recursive step
        return n * factorial(n-1) 
    
#define main function    
def main():
    #user input
    number = int(input(f"Enter a non-negative integer: ")) #stores non-negative integer as 'number'

    #calculates factorial using factorial function on 'number' and stores it as 'result'
    result = factorial(number)

    print(f"The factorial of {number} is {result}.") #prints the result

main() #calls main