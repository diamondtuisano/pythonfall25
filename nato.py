"""

Your mission is to create a Python program that uses a dictionary to translate letters into 
the NATO Phonetic Alphabet. This program will ask users for a word and then spell it out using 
the NATO codes.

Steps to Follow:
Create the NATO Phonetic Alphabet Dictionary:
Construct a dictionary in Python named nato_alphabet, where each key is a letter, and its 
value is the corresponding NATO phonetic term.
Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter to find and 
print the NATO phonetic term.
Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.

Test Your Program:
Test the program with various inputs, ensuring it works as expected.
Reference Table: NATO Phonetic Alphabet
NATO Phonetic Alphabet
Letter	Code Word
A	Alpha
B	Bravo
C	Charlie
D	Delta
E	Echo
F	Foxtrot
G	Golf
H	Hotel
I	India
J	Juliett
K	Kilo
L	Lima
M	Mike
N	November
O	Oscar
P	Papa
Q	Quebec
R	Romeo
S	Sierra
T	Tango
U	Uniform
V	Victor
W	Whiskey
X	X-ray
Y	Yankee
Z	Zulu
Example Output:
If the user inputs "Hello":

Hotel
Echo
Lima
Lima
Oscar

"""
#database for nato alphabet
NATO = { #uppercase bc it is a constant, declare global dictionary
    "A": "Alpha", 
    "B": "Bravo", 
    "C": "Charlie", 
    "D": "Delta", 
    "E": "Echo",
    "F": "Foxtrot", 
    "G": "Golf", 
    "H": "Hotel", 
    "I": "India", 
    "J": "Juliett",
    "K": "Kilo", 
    "L": "Lima", 
    "M": "Mike", 
    "N": "November", 
    "O": "Oscar",
    "P": "Papa", 
    "Q": "Quebec", 
    "R": "Romeo", 
    "S": "Sierra", 
    "T": "Tango",
    "U": "Uniform", 
    "V": "Victor", 
    "W": "Whiskey", 
    "X": "X-ray", 
    "Y": "Yankee", 
    "Z": "Zulu"
}

#define main function to get word from user and print nato alphabet
def main():
    word = input("Enter a word: ").upper() #ask user for word input & convert to uppercase to match keys in dictionary
    for letter in word: #go through each letter in word
        if letter in NATO: #check if letter is in NATO dictionary
            print(NATO[letter]) #print corresponding nato code based on letter
        else: #handle non-letter characters
            print(f"{letter} is not a valid letter. Please choose between A-Z.") #print error message

main() #call main to run program