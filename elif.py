"""

Accept a numeric grade from the user and display a letter grade. The  grading scale is  
90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F

Check to see if the number given is between 0 and 100.  

"""

#define a function to calculate the grade
#get the student's grade
grade = int(input("What is their grade? "))

#check if grade is less than 0 or more than 100
if grade < 0 or grade > 100
    print("Invalid. Please enter a grade between 0 and 100.")

#grade breakdown based on grading scale in chunks of 10
elif grade >= 90:
   print("The letter grade is A.")
elif grade >= 80:
   print("The letter grade is B.")
elif grade >= 70:
   print("The letter grade is C.")
elif grade >= 60:
   print("The letter grade is D.")

#failing grade
else:
   print("The letter grade is F."

#final words
print("Their grade is", str(grade))
