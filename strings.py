"""
In this assignment, you will practice using various string functions in Python. Complete the tasks 
listed in the TODO comments within the provided code.

Instructions:
1. Setting Up Your Environment:
a. Open Visual Studio Code (VS Code) on your computer.
b. Create a new Python file named strings.py.

2. Download the Starting Code: string_practice-2.py
a. Download string_practice-2.py

3. Complete the Code:
a. Follow the directions in each TODO section.
b. Write the necessary Python code to accomplish the tasks in the comments.
c. Ensure your code runs without errors.

4. Upload to GitHub:
a. Upload the completed strings.py file to a new repository in your GitHub account.
b. If new to GitHub, create a repository and upload your file.

5. Submit Your Assignment:
a. Copy the URL to your strings.py file on GitHub.
b. Submit this link to your instructor or through your course submission portal.
"""

def main(): #define main function
    example_string = "Hello, Python programmers!" #defines greeting as variable 'example string'
    #TODO: Iterate through the string and print each character
    print("\nIterating through the string:") #print first prompt
    for char in example_string: #goes through the characters in 'hello, python programmers!' and 
        print(char) #prints each character in example_string as a separate line

    #TODO: Find and print the character with the minimum ASCII value in the string
    min_char = min(example_string) #variable min_char returns lowest ASCII value w/ min()function
    print("\nCharacter with the minimum ASCII value:") #print second prompt
    print(min_char) #prints lowest ASCII value in example_string [will show up as a blank space]

    #TODO: Find and print the character with the maximum ASCII value in the string
    max_char = max(example_string) #variable max_char returns highest ASCII value w/max()function
    print("\nCharacter with the maximum ASCII value:") #print third prompt
    print(max_char) #prints highest ASCII value in example_string [will be 'y']

    #TODO: Find and print the index of the first occurrence of 'o' in the string
    try: #account for errors
        index_of_o = example_string.index('o') #stored as variable index_of_o 
        print("\nIndex of 'o':") #print fourth prompt
        print(index_of_o) #prints index of the first occurring value of 'o' in example_string [#4 in list]
    except ValueError: #if 'o' not found
        print("\n'o' was not found in the string.") #print ValueError message

    #TODO: Convert the string into a list of characters and print the list
    char_list = list(example_string) #stored as variable char_list
    print("\nConverting string to a list of characters:") #print fifth prompt
    print(char_list) #prints each separate charcter as a list

    #TODO: Count and print the number of occurrences of 'o' in the string
    count_of_o = example_string.count('o') #stored as variable count_of_o
    print("\nCount of 'o' in the string:") #print sixth and final prompt
    print(count_of_o) #prints the count of how many 'o's there are

main() #calls main
