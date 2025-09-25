"""
Create a Python script to track heart rate readings and calculate the average heart rate.
Requirements:
Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it.
Sample Output:
Enter your heart rate (in BPM) in the Morning: 70
Enter your heart rate (in BPM) at Midday: 75
Enter your heart rate (in BPM) in the Afternoon: 72
Enter your heart rate (in BPM) in the Evening: 68
Average heart rate today: 71.25 BPM
"""

#variables
time_slots = ["Morning", "Midday", "Afternoon","Evening"] #time of day
total = 0 #starting point
heart_rate_with_times = [] #empty list

#get info from user
for time in time_slots: #specifies time of day
    heart_rate = int(input(f"Please enter your heart rate (in BPM) in the {time}: ")) #define heart_rate through user

    while heart_rate > 100 or heart_rate < 60: #normal heart rates
        correct_number = input( #ensure user is entering correct number for normal heart rates
            f"The level {heart_rate} is outside of normal ranges. Are you sure? (Y or N)")
        if correct_number == "Y" or correct_number == "y": #accepts user's unput
            break #ends if they select y or Y
        else:
            heart_rate = int(input(f"Please enter the {time} heart rate: ")) #prompts them to enter correct one
    #add to the list
    heart_rate_with_times.append([time, heart_rate])

#print results
for item in range(len(heart_rate_with_times)):
    print(f"In the {heart_rate_with_times[item][0]}, your heart rate was {heart_rate_with_times[item][1]}.")
    total += heart_rate_with_times[item][1]

#calculate average
average = total / len(heart_rate_with_times)
print(f"Your average heart rate today was: {average:.2f} BPM.")