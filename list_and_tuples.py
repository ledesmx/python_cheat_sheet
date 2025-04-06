# LISTS
# They are one of the 4 typese in python to store collections of data

furniture = ['table', 'chair', 'rack', 'shelf']
print(furniture[0], furniture[3])
print(furniture[-1]) # Negative indexes


# GETTING SUBLIST WITH SLICES

print(furniture[1:3])

furniture2 = furniture[:] # Slicing the complete list (copy)
print(furniture2)

print(len(furniture2)) # Length

furniture2[1] = 'desk'
furniture2[2] = 'bed'
print(furniture2)


# CONCATENATION AND REPLICATION

print(furniture + furniture2) # Concatenation
print(furniture2 * 3) # Replication


# FOR WITH LISTS
 
for item in furniture:
    print(item)

for index, item in enumerate(furniture2):
    print(index, item)

price = [70, 99, 150, 110]
for item, amount in zip(furniture2, price): # Loop in multiple lists
    print(f'{item} ${amount}')


## 'IN' ADN 'NOT IN' OPERATORS

print('rack' in ['table', 'chair', 'rack'])
print('rack' not in ['table', 'chair', 'rack'])


# MULTIPLE ASSIGNMENT

table, chair, rack, shelf = furniture
print(table, chair, rack, shelf)


# INDEX METHOD

print(furniture.index('shelf'))


# ADDING VALUES AND REMOVING VALUES

furniture.append('bed')
furniture.insert(1, 'desk')
del furniture[0]
furniture.remove('chair')
print(furniture)
print(furniture.pop(), furniture)


# SORTING VALUES

numbers = [7, 2, 0, 6, 9, 8, 3, 6, 2, 7]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

letters = ['d', 'G', 'f', 'k', 'T', 'a']
letters.sort(key=str.lower)
print(letters)

print(sorted(furniture)) # sorted return a new list


# TUPLE
# Tuples are immutable, lists are mutable
# Tuples are more memory efficient than lists

bands = ('Los Angeles Azules', 'C. Tangana', 'El Mato a un Policia Motorizado', 'Junior H')
print(bands)
print(bands[2])


# CONVERTING BETWEEN LIST AND TUPLE

print(tuple(furniture))
print(list(bands))

