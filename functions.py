"""

Objective: Write a Python program that includes two functions - one to calculate the area of a square 
and another for the area of a circle.

Instructions:

Start with Function Definitions:
1. Define two functions: square and circle.
2. Each function should take one parameter (side for square, radius for circle).

Write the square Function:
1. Calculate the area as side * side and display the result: 
2. "The area of the square is [result] square units."

Write the circle Function:
1. Calculate the area using the formula: area = π * radius * radius. Use 3.14 for π.
2. Display the result: "The area of the circle is [result] square units."

Test Your Functions:
1. Call square and circle with sample values.

Sample Results:
The area of the square is 16 square units.
The area of the circle is 78.5 square units.

"""
PI = 3.14 #define pi as a global constant by capitalizing it

def main(): #define main, as an entry point
    area_square(7) #call square with side of 7
    area_circle(3) #call circle with radius of 3

def area_square(side): #function area_square + argument 'side'
    area = side * side #calculate the area by multiplying side twice
    print(f"The area of the square is {area}.") #print result of square's area

def area_circle(radius): #function area_circle + argument 'radius'
    area = (radius * radius * PI) #calculate the area by multiplying radius twice times pi
    print(f"The area of the circle is {area:.1f}.") #print result of circle's area to the nearest tenth

print(f"Sample results: ") #print sample results

main() #returns main and allows function to run