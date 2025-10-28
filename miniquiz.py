"""
Write a short interactive Python program of your choice that uses try and except 
to catch and respond to at least two specific exceptions. Your program should:

1. Include a main() function.
2. Use try and except to catch specific errors like ValueError or ZeroDivisionError.
3. Provide helpful messages when errors occur.
4. Do something meaningful or fun—be creative! You could build a number guessing game, 
a basic calculator, or even a simple quiz with input validation.
5. Make sure to comment your code and upload it to GitHub when complete. Submit your 
link on Canvas.
"""
def main(): #define main function
    print(f"\nDetermine which generation you are (according to Google)!\n")
    
    try: #account for errors
    
        user_year = (int(input(f"Enter, in 4 digits, your birth year: "))) #user input

        user_gen = ["GI Generation (1901-1927)", 
                    "Silent Generation (1928-1945)",
                    "Baby Boom Generation (1946-1964)", 
                    "Generation X (1965-1980)",
                    "Millenial/Gen Y (1981-1996)", 
                    "Gen Z/iGen (1997-2009)", 
                    "Gen Alpha (2010-2024)", 
                    "Gen Beta (2025-2039)"] #list of user generations
    
        if user_year == 0: #in case they input 0
            print(100/user_year) #purposefully check for a ZeroDivisionError

        if user_year >= 2025 and user_year <= 2039: #Gen Beta
            print(user_gen[7]) #index numer 7 for item in list

        elif user_year >= 2010 and user_year <= 2024: #Gen Alpha
            print(user_gen[6]) #index numer 6 for item in list

        elif user_year >= 1997 and user_year <= 2009: #Gen Z/iGen
            print(user_gen[5]) #index numer 5 for item in list

        elif user_year >= 1981 and user_year <= 1996: #Millenial/Gen Y
            print(user_gen[4]) #index numer 4 for item in list

        elif user_year >= 1965 and user_year <= 1980: #Generation X
            print(user_gen[3]) #index numer 3 for item in list

        elif user_year >= 1946 and user_year <= 1964: #Baby Boom Generation
            print(user_gen[2]) #index numer 2 for item in list
        
        elif user_year >= 1928 and user_year <= 1945: #Silent Generation
            print(user_gen[1]) #index numer 1 for item in list

        elif user_year >= 1901 and user_year <= 1927: #GI Generation
            print(user_gen[0]) #index numer 0 for item in list

        else:
            print(f"{user_year} does not fall between 1901 and 2039.") #catch years outside of available list

    except ValueError: #potentional value error if input is not a number
        print(f"Invalid input. Please input a 4-digit number!")

    except ZeroDivisionError: #potential zerodivion error if input is 0
        print(f"Please enter a birth year greater than 0.")

    except Exception as e: #define specifically what is in the error
        print(f"An unexpected error occurred {e}.") 

main() #call main