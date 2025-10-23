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
    user_year = print(int(input(f"Enter, in 4 digits, your birth year: ")))
    user_gen = ("GI Generation (1901-1927)", "Silent Generation (1928-1945)", 
                "Baby Boom Generation (1946-1964)", "Generation X (1965-1980)",
                "Millenial/Gen Y (1981-1996)", "Gen Z/iGen (1997-2010)", 
                "Gen Alpha (2010-2024)", "Gen Beta (2025-2039)")

    
    
    if user_year < 2040:
        print(f"You're a baby, or just a thought, depending what end of the specturm.")
        print(user_gen.index(7))

    elif user_year < 2025:
        print(f"You're basically an infant.")
        print(user_gen.index(6))

    elif user_year < 2011:
        print(f"You're probably cool.")
        print(user_gen.index(5))

    elif user_year < 1997:
        print(f"You're probably a little old.")
        print(user_gen.index(4))

    elif user_year < 1981:
        print(f"You're pretty old.")
        print(user_gen.index(3))

    elif user_year < 1965:
        print(f"Someone call the museum. They're missing a dinosaur!")
        print(user_gen.index(2))
        
    elif user_year < 1946:
        print(f"Shhh...")
        print(user_gen.index(1))

    elif user_year < 1928:
        print(f"Somebody call the army.")
        print(user_gen.index(0))

    else:
        print(f"Invalid input.")

    try: #account for errors
        if len(user_year) == 4:
            print(user_gen)
    except ValueError: #potentional value error if input is not a number
        print(f"Input invalid. Please input a 4-digit number!")

main() #call main