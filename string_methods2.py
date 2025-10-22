"""
Step 1: Download the Exercise File
There is a Python file string_methods2.py Download string_methods2.pythat you need to download. 
This file contains several TODO comments, each indicating a small task for you to complete.

Step 2: Complete the Exercises
Open string_methods2.py in your favorite Python editor. For each TODO comment in the file, write 
the necessary Python code to complete the task. These tasks are designed to give you hands-on 
experience with different string methods.

Step 3: Test Your Code
After writing your code for each task, run the file to test your solutions. Make sure each part 
of the exercise works as expected. If you encounter errors, try to debug and fix them.

Step 4: Upload to GitHub
Once you are confident that your code works correctly, upload the string_methods2.py file to 
your existing GitHub repository. If you're new to GitHub, remember to 'commit' your changes 
and 'push' them to the repository.

Step 5: Submit Your Work
After uploading the file to GitHub, copy the URL of the file in your GitHub repository. Submit 
this link as your assignment. Make sure the link you submit goes directly to the string_methods2.py 
file in your GitHub repository.
"""
# Python String Methods Practice

def main(): #define main function

    # TODO: Use the capitalize() method to capitalize the first letter of the string
    # Example: "python" -> "Python"
    string1 = "python"
    print(string1.capitalize()) #my code

    # TODO: Use the center() method to center the string in a string of specified width
    # Example: "python" -> " python "
    string2 = "python"
    print(string2.center(10, '*')) #my code

    # TODO: Use the endswith() method to check if the string ends with a specified substring
    # Example: Check if "python" ends with "on"
    string3 = "python"
    print(string3.endswith('on')) #mycode

    # TODO: Use the find() method to find the first occurrence of a substring in the string
    # Example: Find the position of "th" in "python"
    string4 = "python"
    print(string4.find('th')) #my code

    # TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
    # Example: Check if "python3" is alphanumeric
    string5 = "python3"
    print(string5.isalnum()) #my code

    # TODO: Use the isalpha() method to check if all characters in the string are alphabetic
    # Example: Check if "python" is alphabetic
    string6 = "python"
    print(string6.isalpha()) #my code

    # TODO: Use the islower() method to check if all characters in the string are lowercase
    # Example: Check if "python" is in lowercase
    string7 = "python"
    print(string7.islower()) #my code

    # TODO: Use the isspace() method to check if all characters in the string are whitespaces
    # Example: Check if " " is all whitespace
    string8 = " "
    print(string8.isspace()) #my code

    # TODO: Use the isupper() method to check if all characters in the string are uppercase
    # Example: Check if "PYTHON" is in uppercase
    string9 = "PYTHON"
    print(string9.isupper()) #my code

    # TODO: Use the join() method to join elements of an iterable with the string as the separator
    # Example: Join ["Python", "is", "fun"] with "-" as separator
    iterable1 = ["Python", "is", "fun"]
    separator = "-"
    print("-".join(["Python","is","fun"])) #my code

main() #call main