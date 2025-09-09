"""
Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward 
and user-friendly.

Remember:

Comment your code to explain the functionality of each section.
Handle edge cases, such as ages, precisely at the thresholds.
"""

#ask for age
num = int(input("How old are you? "))

#driving
if(num >= 16):
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

#vote
if(num >= 18):
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

#alcohol
if(num >= 21):
    print("You are old enough to buy alcohol.")
else:
    print("You are not old enough to buy alcohol.")

#senior discount
if(num >= 65):
    print("You are eligible for a senior discount.")
else:
    print("You are not eligible for a senior discount.")