"""

Develop a Python-based Madlib based on a song of your choice. The program should collect at least 
8 different pieces of information from the user and incorporate them into the song using named arguments. 
The goal is to practice using functions, user input, and string manipulation in Python.

Important Note:
Choose any song you like for your madlib, but remember, no Rickrolling! Be creative and respectful in 
your song choice.

Task:
1. Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song 
with inappropriate or offensive content.

2. Identify Variables: Determine at least 8 different variables that the user will provide to customize 
the song. These could include names, adjectives, nouns, places, etc.

3. Write the Function:
a. Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
b. Use f-strings to incorporate these parameters into the song's lyrics.
c. Ensure the function prints the customized song lyrics.

4. Collect User Input:
a. Write code to collect user input for each of the 8 variables.
b. Use clear and descriptive prompts to guide the user.

5. Call the Function:
a. Call the custom_song function with the user inputs as named arguments.
b. Ensure the order of arguments matches the parameters in your function definition.

"""
print(f"Let's get started on your custom song!") #Greeting

#define song function with parameters
def custom_song(insect, bodypart1, noun, bodypart2, bodypart3plural, verb, direction, timeofday): 
        print(f"\n\n") #new line
        print(f"Wake Me Up Before You Go-Go: Madlibs Version") #print song title
        print(f"\n\n") #new line; I just like how the breaks look; saw it on the class example and Web
        print(f"Jitter{insect}, \n\n" * 4) #print insect four times with a new line in between
        print(f"You put the boom boom into my {bodypart1},") #print bodypart1
        print(f"You send my {noun} sky high when your lovin' starts,") #print noun
        print(f"Jitter{insect} into my {bodypart2},") #print insect again + bodypart2
        print(f"Goes bang-bang-bang 'til my {bodypart3plural} do the same,") #print bodypart3
        print(f"But something's {verb}ing me,") #print verb
        print(f"Something ain't {direction},") #print direcion
        print(f"My best friend told me what you did last {timeofday},") #print timeofday

def main(): #define main
    #collect user input
    input_insect = input(f"Enter an insect: ")
    input_bodypart1 = input(f"Enter a body part: ")
    input_noun = input(f"Enter a noun: ")
    input_bodypart2 = input(f"Enter another body part: ")
    input_bodypart3plural = input(f"Enter another body part and make it plural: ")
    input_verb = input(f"Enter a verb: ")
    input_direction = input(f"Enter a direction: ")
    input_timeofday = input(f"Enter a time of day: ")
    
    #call functions with inputs
    custom_song(
    insect=input_insect, 
    bodypart1=input_bodypart1, 
    noun=input_noun, 
    bodypart2=input_bodypart2,
    bodypart3plural=input_bodypart3plural, 
    verb=input_verb, 
    direction=input_direction, 
    timeofday=input_timeofday
    )

main() #calling main