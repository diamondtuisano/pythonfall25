"""
    Write the program "99 Bottles of Beer on the Wall" using a while loop. 
    Be mindful to change the word 'bottles' to 'bottle' when down to the last one. 
    You must do the full 99 bottles; the sample shows the last 3 verses.

"""

#define bottles
bottles = 99
while bottles > 2:
    print(f"{bottles} bottles of beer on the wall")
    print(f"{bottles} bottles of beer")
    print(f"Take one down, pass it around")
    #increment the loop
    bottles = bottles - 1
    print(f"{bottles} bottles of beer on the wall!\n")

while bottles == 2: #once bottles are 2, 1 is singular
    print(f"{bottles} bottles of beer on the wall")
    print(f"{bottles} bottles of beer")
    print(f"Take one down, pass it around")
    #increment the loop
    bottles = bottles - 1
    print(f"{bottles} bottle of beer on the wall!\n")

#after 1 bottle is left, there are none left
print(f"{bottles} bottle of beer on the wall")
print(f"{bottles} bottle of beer")
print(f"Take it down, pass it around")
print("No bottles of beer on the wall!")