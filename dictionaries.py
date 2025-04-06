# DICTIONARIES

dog = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}
print(dog)


# SET KEY

dog['age_years'] = 6
print(dog)


# GET VALUE

print(dog['color'])


# VALUES

for value in dog.values():
    print(value)


# KEYS

for key in dog.keys():
    print(key)

for key in dog: # There is not need to use keys() since it is the default
    print(key)


# ITEMS
# Get both key and value

for key, value in dog.items():
    print(key, value)


# GET
# Get the value, if the key doesnt exist the returns 'None'

print(dog.get('color'))
print(dog.get('name'))
# print(dog['name']) # This throws


# SET DEFAULT

dog.setdefault('name', 'Firulais')
print(dog)


# POP, POPITEM, DEL, CLEAR

print(dog.pop('disposition')) # removes and return an item based on a given key
print(dog.popitem()) # removes and return the last item
del dog['size'] # removes an item based on a given key
print(dog)

dog.clear() # removes all the items
print(dog)


# CHECKING KESY AND VALUES

person = {'name': 'Jon', 'age': 27}

print('name' in person.keys())
print('name' in person) # Keys is default

print(27 in person.values())


# MERGE TWO DICTIONARIES

a = {'x': 5, 'y': 10}
b = {'x': 1, 'z': 15}
c = {**a, **b}
print(c)
