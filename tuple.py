"""

Now, let's practice using tuples. Imagine you're planning the classes for a programming 
certificate. You need to list out six classes. Here's what you need to do:

1. Create a tuple named programming_classes with these classes: 'Intro to Python', 
'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures 
in Python', 'Web Design Fundamentals'.
2. Write a program that uses a for loop to print each class in the tuple.
3. Use the len function to print how many courses are in the tuple.
4. Make sure to use a main function for this program.

"""

def main(): #define main function 
    #tuple
    programming_classes = ("Intro to Python","Advanced Python", "Database Essentials",
    "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals" )
    #for loop; items returns the items in the tuple defined
    for item in programming_classes:
        print(item) #prints the classes listed in tuple
    #prints the length of the items in the tuple, still in main but not directly
    #in the for loop so it doesn't print 6 times
    print(f"There are {len(programming_classes)} programming courses in this tuple.")

main() #call main