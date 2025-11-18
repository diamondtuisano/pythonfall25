"""
Option 1 – Personal Diary:
1. Create a program named personal_diary.py.
2. Ask the user for date, time, and a diary entry.
3. Append the entry to diary.txt (do not overwrite).
4. Separate each entry with a blank line for readability.
5. Run your program at least three times to confirm new entries are saved properly.
"""
#ask user for date, time, and a diary entry

date = input("Enter a date: ")
time = input("Enter a time: ")
entry = input("\nDiary entry:\n")

#append entry to diary.txt
with open("diary.txt", 'a') as file:
    file.write(date + ',' + time + ',' + entry + '\n') #separate each line w/blank space \n