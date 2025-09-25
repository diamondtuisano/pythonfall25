"""

Create a List: Start by creating a list named days that includes all seven days of 
the week.
Initialize an Empty List: Create an empty list called steps to store the number of 
steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for 
each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps.

"""

#days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#empty list
my_steps = []

#range and input from user
for day in days:
   in_steps = int(input(f"How many steps did you take on {day}? "))
   my_steps.append(in_steps) #store steps

for i in range (0, 7):
    print(f"{days[i]} you walked {my_steps[i]} steps.")

total = sum(my_steps)

#pulls out of for loop
print(f"Total steps: {total}")

print(f"Average steps: {total / len(days): .2f}")