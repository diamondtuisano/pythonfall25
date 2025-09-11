"""

Accept a numeric grade from the user and display a letter grade. The  grading scale is  
90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F

Check to see if the number given is between 0 and 100.  

"""

# Define a function to calculate buffet price based on age
# Get the customer's age
age = int(input("How old is the customer?  "))
# Check if age is less than 1
if age < 1:
    price = 0.00  # Buffet is free for children under 1
# Check if age is between 1 and 12
elif age < 12:
    price = age * 1.00  # Charge $1 for each year of age
# Check if age is 12 or older but less than 65
elif age < 65:
    price = 16.95  # Standard adult price
# Age is 65 or older
else:
    price = 12.95  # Senior discount price

print("The cost will be:  $", str(price))