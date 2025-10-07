"""

Demonstrate using our calculator module

"""

from math_operations import calculator, geometry

def main():
    result = calculator.add(5, 3)
    print(f"Addition result: {result}")

    result = calculator.subtract(10, 4)
    print(f"Subtraction result: {result}")

    result = calculator.area_square(6)
    print(f"The area of a square result: {result}")

    result = calculator.area_circle(9)
    print(f"The area of a circle result: {result}")

    result = calculator.area_rectangle(3, 7)
    print(f"The area of a square result: {result}")

main()