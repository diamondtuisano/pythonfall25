"""
1. Modify Artist List: 
a. Write a function to replace an artist in the top_artists list. 
b. The function should ask the user for an index and a new artist name. 
c. Ensure your function catches and handles ValueError for invalid number conversion 
and IndexError for out-of-range indices.

2. General Error Handling: 
a. Modify your function to catch both ValueError and IndexError using a single except block. 
b. Provide a general error message like "An input error occurred."

Hints:
- Use input() to get user input for the index and new artist name.
- Convert the index input to an integer using int(). This might raise a 
ValueError if the input is not a valid integer.
- When replacing an artist in the list, accessing an invalid index will raise an IndexError.
- Use a try...except block to catch and handle these exceptions.
- Remember that you can catch multiple exceptions in a single block by using a tuple 
for general error handling.

Example User Interaction:
Enter the index of the artist to replace: 2
Enter the new artist name: Taylor Swift
Updated list: ['The Beatles', 'Madonna', 'Taylor Swift', 'Elvis Presley', ...]

Note to Students: 
This assignment is designed to test your understanding of exception handling in Python. 
Focus on how you can make your program robust against invalid user inputs and how to 
provide informative error messages. Good luck!
"""
def main(): 

    """ 1) user inputs an index value, new artist's name to replace one in list
        2) handle ValueError and IndexError in a single block """
    
    #original list
    artists = ["The Beatles", 
               "Madonna", 
               "Elton John", 
               "Elvis Presley", 
               "Mariah Carey", 
               "Stevie Wonder", 
               "Janet Jackson", 
               "Michael Jackson", 
               "Whitney Houston", 
               "Rihanna"] 
    print(f"\nHere is a list of artists: {artists}") #list of artists w/break

    try: #account for errors

        #user input index as a string
        index_input = (input(f"\nEnter the index of the artist to replace (0-9): ")) 
        #valueerror if not an integer
        index_new = int(index_input)
        #user input new artist
        new_artist = input(f"Enter a new artist name: ") 
        artists[index_new] = new_artist #catches indexerror if outside of 0-9, change list cited

        print(f"Updated list: {artists}") #prints updated list
        
    except (ValueError, IndexError): #except block w/valueerror and indexerror
        print(f"\n An error occurred.")
        print(f"Please enter a whole number between 0-9.")

main() #call main