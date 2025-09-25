"""

Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.

"""

#prompt user to enter five names and store it in a list
names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

#bubble sort
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True

#print sorted list
print(f"Sorted list: ", names)

#reverse sorted list
names.reverse()
print(f"Reversed list: ", names)

