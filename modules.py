"""

In this assignment, you will create a Python program that generates a random number 
between 1 and 100. Your program should allow the user to guess the number, and 
provide feedback on how close their guess is to the actual number.

Assignment Objectives:
Use the random module to generate a random number.
Implement a while loop to allow continuous guessing until the correct number is 
guessed.
Use the abs() function to determine the difference between the guess and the actual 
number.
Provide feedback based on the proximity of the guess to the actual number:
If the difference is within 5, print "Very Hot".
If the difference is within 15, print "Hot".
If the difference is within 25, print "Cool".
If the difference is more than 25, print "Cold".
Make sure to call the main function!
After completing the program, upload it to your GitHub repository.
Submit the link to your GitHub repository in Canvas.
Task Details:
Import the random module and use it to generate a random number between 1 and 100.
Write a while loop that allows the user to enter a guess for the number.
Inside the loop, use the abs() function to calculate the absolute difference between 
the guess and the actual number.
Provide feedback based on the computed difference (e.g., "Very Hot" for close 
guesses).
The loop should continue until the user guesses the correct number.
Uses the Random Module.

"""
#like global, first thing to include
import random 

def generate():
    """
        called by main
        generates and returns a random number b/w 1-100
    """
    my_random = random.randint(1,100) #module.makes it a random integer
    return my_random #returns the random number

def main():
    """
        call generate function to return a random number between 1 and 100
        ask user to input a number between 1 and 100
        use a while loop to allow continuous guessing until correct number has been guessed.
        displays results on absolute proximity
    """
    #get user input
    num_1 = int(input(f"Guess a number between 1-100: "))
    num_2 = generate()
    if num_1 == num_2:
        print(f"Correct!")
    else:
        #evaluate distance between them
        difference = abs(num_1 - num_2)
    if difference <= 5:
        print(f"Very Hot")
    elif difference <= 15:
        print(f"Hot")
    elif difference <= 25:
        print(f"Cool")
    elif difference > 25:
        print(f"Cold")

    print(f"Number 1: {num_1}")
    print(f"Number 2: {num_2}")


main()