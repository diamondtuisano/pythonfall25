"""
Objective:
-Ask the user to input their birthday.
-Calculate the user's age in years, months, days, hours, and minutes.
-Provide detailed comments to all of the code, explaining what each line that has to do with time calculation does.
-Display the results in a user-friendly format.
-Implement the solution inside a main() function.

Instructions:
1.Create a Python script that performs the following steps:
2.Define a main() function where your program logic will reside.
3. Use my start program from GitHub: startprogramLinks to an external site.
4. You can view the classroom demonstration of how we got to the code at the top of the page.
5. Comment explaining each line of the code
6. Finish the code to get and display:
    months
    weeks
days (done)
years (done)
7. Format and print the results in a clear, understandable manner.
"""
from datetime import datetime #import datetime module

def main():
   """ ask user for birthday, calculate age in years, months, days, hours, mins"""
print("\n\n") #print blank line
try: #catch errors
        """variables and user input"""
        today = datetime.today()
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        delta = today - birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425
       
        delta_months - delta.days // 365.2425 // 7 #months
        print(f'Difference is {delta_months}')

        #weeks
        #months

        print(f'{delta_years} years old.')
        print(f'{delta_months} months')
        print(f'{delta_weeks} weeks')
        print(f'{delta_days} days')
       
except Exception as e:
    print(f"ooooops!!!:  {e}") 
    main()
main()
