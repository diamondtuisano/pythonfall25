"""
Hangman Start - Week 10 Strings Demo

This program begins a simple version of Hangman. You will finish it by:
- Adding a list to keep track of guessed letters
- Checking if the letter was already guessed BEFORE checking if it is in the word
- Changing the word list to 15 words on a subject of your choice
- Display how many incorrect guesses they have left 

1. Change the WORD_LIST to include 15 different words on a subject of your 
choice (e.g., animals, food, movies, sports, etc.).
2. Finish the guessed_letters logic:
a. Before checking if the guessed letter is in the word, check if it is already in 
guessed_letters.
b. If it is, print a message like You already guessed that letter! and skip the rest 
of the loop using continue.
c. If it is not in the list, add it to guessed_letters and proceed with checking if 
it's in the word.
d. Display how many incorrect guesses they have left.

"""
#get random 
import random

#all caps for available words
WORD_LIST = ("DOG", "CAT", "MONKEY", "GOAT","LIZARD","PIG","BIRD",
             "SNAKE","BEAR","SPIDER","FISH","HAMSTER","TURTLE","CHICKEN","HORSE")

def game(answer, display): #define game function; track guess counts
    wrong = 0 
    right = 0

    #print welcome message with rules of game
    print("Welcome to Hangman, the topic is pets.")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")

    guessed_letters = [] #list of guessed letters

    while True: #game loop continues until player wins or loses
        for item in display: #display current state of word
            print(item, end=" ") #prints letter or underscore followed by a space

        print("\n\n") #print breaks
        guess = input("Please enter a letter: ").upper() #get user input convert to uppercase

        #check if already guessed in list
        if guess in guessed_letters:
            print("You already guessed that letter!") #print already guessed message
            continue #skips current loop and goes to game loop, asking for another guess
        else:
            guessed_letters.append(guess) #add new letters to list of guesses

        bad_guess = True #if it's a bad guess...
        for i in range(len(answer)): #loops through length of hangman word
            if guess == answer[i]:
                display[i] = guess 
                right += 1 #right guesses increase by one
                bad_guess = False #letter was found so mark as correct

        if bad_guess: #assumes guess is wrong until proven correct
            print("Wrong!") #prints incorrect guess message
            wrong += 1 #wrong guesses increase by one
            print(f"You have {5 - wrong} guesses left!") #print number of guesses left

        if wrong >= 5: #if the number of wrong guesses are greater than or equal to 5
            print("You Lose!") #prints losing message
            print("The correct word was:", answer) #prints correct answer
            break #ends loop after wrong guesses max is met

        if right == len(answer): #if the right length of the answer
            print("You Win!") #prints end of game winning message
            print("The word was:", answer) #prints the answer
            break #ends game loop


def main(): #define main function
    answer = random.choice(WORD_LIST) #answer as variable as a random word from the word list
    display = ["_"] * len(answer) #displays hangman based on length of word
    game(answer, display) #calls the answer and display

main() #call main