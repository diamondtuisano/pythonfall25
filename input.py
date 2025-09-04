"""
Create a Python application that allows users to input their total budget and the amount 
spent in various categories. The program will then calculate and display the percentage 
of the total budget each category represents.

Requirements:
Design a Python program that prompts users to enter their total budget (ask them for 
their net monthly income) and amounts for spending categories:
Housing (rent or mortgage)
Utilities
Groceries
Transportation
Health Care
Personal Care
Clothing
Debt

Calculate the percentage of the total budget spent in each category.
Tell the user how much the spent total, and how much money they have left. 
Display the results in a user-friendly format using f-strings.
Ensure your code is well-commented to explain the functionality of different sections.

"""

#print welcome message
print("Hello! This is your budget-friendly calculator. I'll be telling you how your monthly budget" \
" breaks down across different categories. Answer the following prompts as they appear on your " \
"screen, rounded to the nearest whole number.")

#define inputted variables
net_monthly_income = int(input("Please enter your net monthly income: "))
housing = int(input("Please enter your rent or mortgage: "))
utilities = int(input("Please enter how much you spend monthly on your utilities: "))
groceries = int(input("Please enter how much you spend monthly on groceries: "))
transportation = int(input("Please enter how  much you spend monthly on transportation: "))
health_care = int(input("Please enter how much you spend monthly on healthcare: "))
personal_care = int(input("Please enter how much you spend monthly on personal care: "))
clothing = int(input("Please enter how much you spend monthly on clothing: "))
debt = int(input("Please enter how much your minimum credit card debt is due each month: "))

#define and then print formula used for percentage of total budget spent in each category
print(f"{housing/net_monthly_income: .2%}", "is your housing percentage.")
print(f"{utilities/net_monthly_income: .2%}", "is your utilities percentage.")
print(f"{groceries/net_monthly_income: .2%}", "is your groceries percentage.")
print(f"{transportation/net_monthly_income: .2%}", "is your transportation percentage.")
print(f"{health_care/net_monthly_income: .2%}", "is your health care percentage.")
print(f"{personal_care/net_monthly_income: .2%}", "is your personal care percentage.")
print(f"{clothing/net_monthly_income: .2%}", "is your clothing percentage.")
print(f"{debt/net_monthly_income: .2%}", "is your debt percentage.")

#total spent formula 
total_spent = housing + utilities + groceries + transportation + health_care + personal_care + clothing + debt
print(f"${total_spent}", 
     " is the total amount spent per month.")

#how much money is left over
print(f"${net_monthly_income - total_spent}", "is how much money you have left over per month.")