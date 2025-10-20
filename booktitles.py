"""

In this assignment, you will create a Python program that collects book titles 
from a user. Your program should use a while loop to prompt the user to enter 
a total of 10 book titles. Follow these steps to complete your assignment:

1. Set Up the Main Function: Write your program inside a main function. This is 
where your while loop will be implemented.

2. Collect Book Titles: Use a while loop to ask the customer to enter 10 book 
titles. Store these titles in a list.

3. Ensure proper capitalization: Use the title function to ensure that the 
first letter is capitalized before storing it in the list.

4. Create a Sorted List: Once all titles are collected, save them to a new list 
named books_sorted. This list should contain the titles in alphabetical order.

5. Display the Titles: Use a for loop to print each title from the sorted list 
on a separate line.

6. Test Your Program: Ensure your program runs correctly and meets all the 
requirements.

7. Upload to GitHub: Once tested, upload your program to GitHub.

8. Submit Your Work: Submit the link to your GitHub repository on Canvas.

"""

def main(): #define main
    """
        collect 10 book titles, capitalize, sort, and then print the sorted list
    """
    book_titles = [] #empty list of book titles

    print(f"Please enter 10 book titles one at a time\n") #instructions w/each line having a break

    while len(book_titles) < 10: #while loop; while length of the book titles are less than ten:
        books_needed = 10 - len(book_titles) #books needed is 10 minus each book title; counts down
        book_input = input(f"Enter book title #{len(book_titles) + 1} ({books_needed} more to go): ") #input for book titles w/number for user to keep track what number they're on
        capitalized_title = book_input.title() #capitalized book variable with the title method so input is capitalized
        book_titles.append(capitalized_title) #adds the user's input in list and capitalizes them

    books_sorted = sorted(book_titles) #variable defined after sorting book titles
    
    print(f"\nYour Collected Book Titles (sorted):\n") #print sorted titles with breaks
    
    for book in books_sorted: #print - before each book in the sorted books variable
        print(f"- {book}")

main() #call main