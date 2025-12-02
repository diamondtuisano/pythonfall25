"""
In this assignment, you will write a Python program that generates a custom calendar 
for a user's birth month in the current year. This task will help you understand how 
to use Python's Calendar module, interact with users, and display data in a structured format.

Objective
Your program should ask the user for their birth month and then display the calendar 
for that month in the current year.

Requirements
Your program must be contained within a main() function.
Use the Python input() function to ask the user for their birth month (as an integer).
Ensure your program can handle invalid inputs gracefully.
Use Python's datetime module to find the current year.
Generate and display the calendar for the user's birth month in the current year.
Format the calendar output so it is easy to read and understand.
 
Steps
Start by importing the necessary modules: calendar and datetime.
Create a main() function where your program's logic will reside.
Inside main(), get the current year using datetime.datetime.now().year.
Ask the user to enter their birth month and store it in a variable.
Validate the user input to ensure it's an integer between 1 and 12.
Use the Calendar module to generate the calendar for the given month and year.
Print the calendar to the console in a readable format.
Don't forget to call the main() function at the end of your script.
"""
import calendar  #import cal module
from datetime import datetime #import datetime from datetime module

def main():

    """ user input for birth month as integer (1-12), create custom calendar, print custom calendar """
    while True:
        try: #catch errors
            birth_month = int(input(f"Enter your birth month as an integer, 1 for Jan: ")) #user input

            if birth_month < 1 or birth_month > 12: #if input is not between 1-12
                print(f"That is not a valid month. Please enter a number between 1-12. ")
                break #ends program
            
            cal = calendar.TextCalendar(calendar.SUNDAY) #create a text calendar starting w/sunday
            current_year = datetime.now().year #uses this year
            month_calendar = cal.formatmonth(current_year,birth_month) #formats the current calendar

        except Exception as e: #print errors
            print(e) 

        print(f"\n---Here is your custom calendar for your birth month--\n") #print title
        print(month_calendar) #prints this month's calendar from current year
        break #ends program after one custom calendar is created
            
main() #call main at end of script