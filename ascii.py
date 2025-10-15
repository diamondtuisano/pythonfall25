"""

Step-by-Step Instructions
1. Start Your Python Script:
a. Open your Python environment and start a new script.
b. Use a main() function to organize your code.

2. Prompt for User Input:
a. Ask the user to enter a single character using input().

3. Validate the Input:
a. Ensure the user enters precisely one character.
b. Use len() to check input length.

4. Convert to ASCII Value:
a. Use the built-in function ord() to get the ASCII value.
    Example:
    ascii_value = ord(user_input)

5. Display the Result:
a. Print the ASCII value to the user.

6. Reverse Lookup:
a. Prompt the user to enter an ASCII value.
b. Ensure that the value is between 32 and 127.
c. Use a try-except block to handle invalid inputs.
d. Use the built-in function chr() to get the corresponding character.
    Example:
    character = chr(ascii_input)
7. Test Your Program:
a. Run your script and try various characters and ASCII values.

8. Submit Your Work:
a. Upload your script to GitHub.
b. Submit a link to your repository.

"""
def chr_ascii(): #define the single character ascii function
    while True: #while loop
        try: #account for errors within loop
            user_input1 = input(f"Please enter a single character: ") #user input1 variable defined
            
            if len(user_input1) == 1: #if user inputs a character length equal to 1
                ascii_value = ord(user_input1) #converts user's single-character input to ascii integer
                print(f"The ASCII integer value of {user_input1} is: {ascii_value}.") #prints correct message
                return #exits function and loop after valid input
            else: #if user doesn't input only one character
                print(f"Invalid. Please enter a single character: ") #print error message

        except TypeError as e: #if user input does not match the ability of the function
            print(f"A TypeError has occurred: {e}.") #print TypeError 
        
def int_ascii(): #define the integer value with corresponding ascii function
    while True: #while loop
        userinput2 = input(f"Please enter an ASCII integer value between 32-127: ") #user input2 variable defined

        try: #account for errors within loop
            ascii_value = int(userinput2) #converts user's integer input to ascii character

            if 32 <= ascii_value <= 127: #userinput2 ascii_value range between 32-127
                character = chr(ascii_value) #character function 'chr' gets ascii's corresponding character value
                print(f"The character for ASCII value {ascii_value} is {character}.") #print character value
                return #exits function and loop after valid input
            else: #otherwise
                print(f"Invalid. Please enter a value between 32-127: ") #print error message
        
        except ValueError as e: #if user input has correct data type but inappropriate value
            print(f"A ValueError occurred: {e}.") #prints ValueError

def main(): #define main
    print(f"[Convert ASCII single-charcter value to integer] ") #print first step of assignment
    chr_ascii() #returns 'ascii_value'; single character as a number

    print(f"[Convert integer ASCII value to character]") #print second step of assignment
    int_ascii() #returns 'character'; integer as a single character

    print(f"Thanks for using the ASCII converter!") #print exit message

main() #call main