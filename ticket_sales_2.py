"""

Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.

"""
#range representing seats numbered 1-20
seats = list(range(1,21)) 

#while loop keeps asking until user enters 0
while True:
    print(f"Available seats:", seats) #display list of available seats

    #select seat by entering #1-20, if 0; end process
    select = int(input(f"Enter a seat number between 1-20 (0 ends the process): "))
    if select == 0: #ends process
        print(f"You have opted to end the process. Thanks for visiting!") #displays message
        break #ends loop so the user isn't asked to select seats again

    if select < 1 or select > 20: #added line; if someone chooses an invalid seat number
        print(f"This seat is invalid. Please choose a seat between 1-20.") #displays 'invalid seat' message
        
    elif select in seats: #if selection is within range and available
        seats.remove(select) #removes it from current seat selection
        print(f"You have purchased seat #{select}.") #displays purchased seat
        print(f"Updated seats:", seats) #displays updated seats available for purchasing
        if seats == []: #added line; checks if no/0 seats are left; if seats = 0
            print(f"All seats are sold out. Thank you, and please come again!") #prints message that we're sold out
            break  #added line; ends loop after all seats are sold
    else: #if seat is already sold
        print(f"That seat is unavailable. Please try again.") #displays message when not in range