"""
Objective:
-Ask the user to input their birthday.
-Calculate the user's age in years, months, days, hours, and minutes.
-Provide detailed comments to all of the code, explaining what each line that has to do 
with time calculation does.
-Display the results in a user-friendly format.
-Implement the solution inside a main() function.

Instructions:
1. Create a Python script that performs the following steps:
2. Define a main() function where your program logic will reside.
3. Use my start program from GitHub: startprogramLinks to an external site.
4. You can view the classroom demonstration of how we got to the code at the top of the 
page.
5. Comment explaining each line of the code.
6. Finish the code to get and display:
    months
    weeks
    days (done)
    years (done)
7. Format and print the results in a clear, understandable manner.
"""
from datetime import datetime, timedelta 
#import datetime module: creates datetime objects
#import timedelta: property of dateime module -> creates objects representing duration of time; difference b/w two datetimes

def main():
    """ ask user for birthday, calculate age in years, months, days, hours, mins. """
    print("\n\n") #print blank line

    try: #catch errors
            """ variables and user input """
            now = datetime.now() #establishes today
            print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}") #prints today formatted

            #user input, convert input to integer
            birth_year = int(input("What year were you born?  "))
            month = int(input("What Month were you born (as a number. May would be 5)  "))
            day = int(input("What day of the month were you born?  "))
            # just need datetime not datetime.date
            # because we imported datetime from datetime

            """ converts user input and strips it to years, months, day, hours, mins, secs. prints output """
            birthday = datetime(birth_year, month, day)
            print("\nYour birthday is: ")
            
            birthday_output = birthday.strftime("%Y-%m-%d %H:%M:%S")
            print(birthday_output) 

            """ calculate age by subtracting birth date from current date """
            delta = now - birthday
            
            total_days = delta.days #primary component of timedelta object

            total_seconds = delta.total_seconds() #method for converting entire duration into seconds

            age_years = total_days / 365.25 #years accounting for leap years

            age_months = total_days / 30.4375 #avg days in a month --> 365.25/12

            age_weeks = total_days / 7 #days in a week

            age_hours = (total_seconds / 3600) #hours = total seconds / (seconds per hour = 60 * 60 = 3600)

            age_minutes = (total_seconds / 60) #mins = total seconds / (seconds per min = 60)

            """ format and print the results in a clear, understandable manner. """
            print(f'\n---Age Calculator Results---\n')
            print(f'You are approximately: ')
            print(f'{age_years:.2f} years,') #convert to float to nearest hundredth
            print(f'{age_months:.2f} months,') #same as above
            print(f'{age_weeks:.2f} weeks,') #same as above
            print(f'{total_days:,} days,') #comma added for readability
            print(f'{int(age_hours):,} hours,') #convert to int w/ comma for cleaner output
            print(f'{int(age_minutes):,} minutes old.') #same as above line
        
    except Exception as e: #error handling for common errors, prints issue with 'e'
        print(f"ooooops!!!: {e}") 

main() #calls main, allows program to run