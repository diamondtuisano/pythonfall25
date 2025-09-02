"""
Create a Python program that converts kilograms to pounds. 
Use at least four different samples to convert. A sample of 
the math is provided below; do not use the same example in 
your program.

Kilograms to Pounds Conversion:
To convert kilograms (kg) to pounds (lb), use the formula:
Pounds (lb) = Kilograms (kg) * 2.20462
Example: 5 kg * 2.20462 = 11.0231 lb

"""

#define variables
kilogram = 8
difference = 2.20462
pound = kilogram * difference 

#program output
print(kilogram, "kilograms", "converts to", pound, "pounds")

#four different samples using relatively the same formula
kg_sample_1 = 7
kg_sample_2 = 3
kg_sample_3 = 9
kg_sample_4 = 10
difference = 2.20462
lb_conversion_1 = kg_sample_1 * difference
lb_conversion_2 = kg_sample_2 * difference
lb_conversion_3 = kg_sample_3 * difference
lb_conversion_4 = kg_sample_4 * difference

#program output
print(f"{kg_sample_1} kilograms converts to {lb_conversion_1} pounds.")
print(f"{kg_sample_2} kilograms converts to {lb_conversion_2} pounds.")
print(f"{kg_sample_3} kilograms converts to {lb_conversion_3} pounds.")
print(f"{kg_sample_4} kilograms converts to {lb_conversion_4} pounds.")