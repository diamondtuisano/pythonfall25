"""
In this exercise, you will practice using logical operators (and, or, not) in Python. 
Your task is to create a program that prompts the user for two integer inputs and then 
demonstrate the use of these operators.

User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers. 
Include two examples for each of the following operators:
and
or
not
Display Results: Print the logical statement and its result for each comparison.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input.
Sample Output: Here's an example of what your program's output might look like:
 

Enter an integer: 5
Enter another integer: 6
Both numbers greater than 0:  True
Both numbers greater than 100:  False
Either number is even?  True
Either number is less than 100?   True
num1 is not equal to num2:  True
num1 is not 0:  True

"""

#prompt users to input two numbers
num1 = int(input(f"Enter an integer: "))
num2 = int(input(f"Enter another integer: "))

#compare numbers are > 0 // if, else, and
print("Both numbers are greater than 0: ")
if num1 > 0 and num2 > 0: 
    print("True")
else:
    print("False")

#compare numbers are > 100 // if, else, and
print("Both numbers are greater than 100: ")
if num1 > 100 and num2 > 100:
    print("True")
else:
    print("False")

#compare if numbers are even // if, else, or
print("Either number is even: ")
if num1 % 2 == 0 or num2 % 2 == 0:
    print("True")
else:
    print("False")

#compare if numbers are < 100 // if, else, or
print("Either number is < 100: ")
if num1 < 100 or num2 < 100:
    print("True")
else:
    print("False")

#compare if numbers are equal // if, else, not
print("Numbers are the same: ")
if not num1 != num2:
    print("True")
else:
    print("False")

#if num1 is not 0 // if, else, or
print("num1 is not 0: ")
if num1 != 0:
    print("True")
else:
    print("False")