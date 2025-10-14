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

def main(): #define main
    try: #test the block of code for errors
        chr = input(f"Please enter a single character: ") #character input as a variable
        while len(chr) != 1: #loop w/while statement, if length of character input is not 1
            print(f"That is not a good input.") #print character error statement
            chr = input(f"Please enter a single character: ") #prompts user to enter a single character
        ascii_value = ord(chr) #convert to ascii value
        print(f"The value of {chr} is {ascii_value}.") #display result; print ascii value to the user

        i = int(input(f"Please enter an ASCII value between 32-127: ")) #prompt user to enter an ascii value
        i = range(32,128) #defines i as variable within the range 32-127
        while i in range: #loop for the values in range 32-127
            print(f"The value of {i} is {ascii_value}.") #print the value
        else: #otherwise 
            print(f"That is not a valid number.") #print int error value statement
            int = int(input(f"Please enter a number between 32-127: ")) #prompts user to enter an int 32-127

    except Exception as e:
        print(e)

main() #call main