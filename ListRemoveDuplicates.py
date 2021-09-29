# LIST REMOVE DUPLICATES

a = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
b = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]

a = set(a)
print(a)
a=list(a)
print(a)

b = []
for elem in a:
    if elem not in b:
        b.append(elem)
print(b)


# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
