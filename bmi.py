"""

Body Mass Index (BMI) is a simple screening measure calculated from height and weight. Use these 
ranges for adult classification; pediatric BMI uses age-/sex-specific percentiles.

✅ Quick reference: Standard adult BMI categories
BMI levels
BMI (kg/m²)	Category
Below 18.5	Underweight
18.5 – 24.9	Normal weight (Healthy range)
25.0 – 29.9	Overweight
30.0 – 34.9	Obesity class I (Moderate)
35.0 – 39.9	Obesity class II (Severe)
≥ 40.0	Obesity class III (Very severe)
Calculate BMI
# Metric
BMI = weight_kg / (height_m ** 2)
# US (pounds & inches)
BMI = (weight_lb / (height_in ** 2)) * 703
Screening tool only; does not distinguish muscle from fat or fat distribution.
Adults ≥ 20 years; use pediatric growth charts for children/teens.
Pair with other measures when available (e.g., waist circumference, body composition).
Requirements:
Global Variables:
Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
Main Function:
1. Prompt the user for their weight in pounds and height in inches.
2. Convert the inputs to metric units using global conversion constants.
3. Calculate BMI using the formula bmi = weight / (height * height).
4. Determine the BMI category based on standard ranges.
5. Display the BMI value and category.
Commenting:
!Include comments to explain key parts of the code.!
Sample Results:
Enter your weight in pounds: 154
Enter your height in inches: 68
Your BMI is: 23.43
You are in the normal weight category.

"""
print(f"BMI Calculator") #title

#conversion of global variables and defining function; used W3Schools
def myfunc():
    global lbs_to_kg
    lbs_to_kg = 0.453592
    global inches_to_m
    inches_to_m = 0.0254 

#define main that controls BMI calculator, categories, and prints results
def main():
    weight_lb = int(input(f"Enter your weight in pounds: ")) #user input weight lb
    height_in = int(input(f"Enter your height in inches: ")) #user input height in
    #conversion using global constants
    weight_kg = weight_lb * lbs_to_kg
    height_m = height_in * inches_to_m
    #Metric kg & meters BMI formula
    BMI = (weight_kg) / (height_m ** 2)

    if BMI < 18.5: #category 1 is less than 18.5
        category = "underweight"
    elif BMI < 25.0: #category 2 is greater than 18.5 AND < 25.0
        category = "normal weight"
    elif BMI < 30.0: #category 3 is greater than 25.0 AND < 30.0
        category = "overweight"
    elif BMI < 35.0: #category 4 is greater than 30.0 AND < 35.0
        category = "obesity class I (moderate)"
    elif BMI < 40.0: #category 5 is greater than 35.0 AND < 40.0
        category = "obesity class II (severe)"
    else: #category 6 is greater than 40
        category = "obesity class III (very severe)"

    #print is in main and prints BMI info to nearest hundredth like in example, along with category
    print(f"Your BMI is: {BMI:.2f}.")
    print(f"You are in the {category} category.")

myfunc() #global variables
main() #allows code to run