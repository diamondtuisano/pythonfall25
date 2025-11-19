"""
Create a Python program that uses a generator function to produce all possible 
two-letter combinations from a given list of characters. 
For example, if the list is ['a', 'b', 'c'], 
the program should generate 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'.

Instructions:
1. Define a generator function two_letter_combinations that takes a list of characters as an argument.
2. Use nested loops within the generator function to iterate over the list of characters. 
In each iteration, concatenate two characters and use the yield statement to yield the 
two-letter combination.
3. In the main method, call the generator function with a list of characters and iterate over 
the generator to print each combination. Create an original  5-letter list.
4. Include comments in your code to explain the logic behind the generator function and 
the use of the yield statement.
"""

#def generator function w/ list of characters as an argument, nested loop; char2
def two_letter_combos(characters):
    for char1 in characters: #select first letter in pair
        for char2 in characters: #select second letter in pair
            combo = char1 + char2 #combo variable created

            yield combo #sends combination back and pauses the 'gen function'
            #'gen function' is saved until next value is requested
            #if return was used, the for loop would have stopped executing after first combo

def main():
    """create an original 5-letter list, call generator function, iterate over generator object"""
    my_characters = ['h','t','m','l','s']

    combo_generator = two_letter_combos(my_characters) #combo generator variable created
    print("My two-letter combos: ") #print title
    for combo in combo_generator: #for loop that goes through each 'combo' in two letter combo gen function
        print(combo) #prints yielded value by generator, one by one
    
main() #call main