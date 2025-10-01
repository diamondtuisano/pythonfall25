"""

Objective:
Write a Python function named calculate_interest that computes and returns simple interest based 
on given parameters. (Note - you will call the function from the main() function, main is required!

Background
Simple interest is calculated using the formula:
_Simple Interest = (Principal Amount * Rate of Interest * Time) / 100

Function Requirements
A main function should control the logic of the program
Create and call a function should be named calculate_interest.
It should take three parameters that you get from the user:
principal - The initial amount.
rate - The annual interest rate (percentage).
time - The investment duration in years.
Use the return keyword to send back the computed interest to a variable in the main function.
Print the result using formatted strings in the main function.
Example
If you call calculate_interest(1000, 5, 2), the function should return 100 as the simple interest.

Task Instructions
Define the function calculate_interest with appropriate parameters.
In main request the three parameters from the user, then pass them as variable.
Apply the formula to calculate the simple interest.
Return the calculated interest.
Print the result using an f-string:
print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
Sample Output:
Enter the principal amount: 250000
Enter the interest rate: 7
Enter the time in years: 12
The simple interest for $250,000.00 at 7% over 12 years is $210,000.00.

"""
print(f"Simple Interest Calculator") #titles are nice

#defines the function calculate interest
def calculate_interest(principal,rate,time): #includes parameters
    interest = (principal * rate * time / 100) #function interest formula
    return interest #returns the result 'interest'

#defines main
def main(): #float for principal and rate since money and percents can have decimals
    principal = float(input(f"Enter the principal amount: ")) #user inputs principal
    rate = float(input(f"Enter the interest rate: ")) #user inputs interest
    time = int(input(f"Enter the time in years: ")) #user inputs time
    interest = calculate_interest(principal,rate,time) #calls function, passes values, returns result in variable interest

    #print the result
    print(f"The simple interest for ${principal:,.2f} at {rate:,.2f}% over {time} years is ${interest:,.2f}.")

main() #calls main and runs program