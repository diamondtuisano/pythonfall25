"""

Calculate the area of shapes.
Create areas for at least three shapes

"""
#used past assignment I submitted for two of the shapes, added rectangle

PI = 3.14 #define pi as a global constant by capitalizing it

def main(): #define main, as an entry point
    area_square(7) #call square with side of 7
    area_circle(3) #call circle with radius of 3
    area_rectangle(4,8) #call rectangle with sides of 4 and 8

def area_square(side): #function area_square + argument 'side'
    area = side * side #calculate the area by multiplying side twice
    print(f"The area of the square is {area}.") #print result of square's area

def area_circle(radius): #function area_circle + argument 'radius'
    area = (radius * radius * PI) #calculate the area by multiplying radius twice times pi
    print(f"The area of the circle is {area:.1f}.") #print result of circle's area to the nearest tenth

def area_rectangle(side1,side2):
    area = side1 * side2
    print(f"The area of the rectangle is {area}.")

main() #returns main and allows function to run