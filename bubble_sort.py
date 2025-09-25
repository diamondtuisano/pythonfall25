"""

Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.

"""

#prompt the user to enter five names
str(print(input(f"Enter five names: ")))

for range i in names



#empty list
names = [input]
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) -1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names [i +1], names[i]
            swapped = True
print(names)
