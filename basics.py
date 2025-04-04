# MATH OPERATORS

res = (2 + 3 * 6) / (4 - 2)
print(res)

res = 4 ** 2 # Exponent
print(res)

res = 10 // 3 # Integer division
print(res)

res = 10 % 3 # Modulus/Remainder
print(res) 


# AUGMENTED ASSIGNMENT OPERATORS

character = 'Jon'
character += ' Wick'
print(character)

number = 100
number -= 1
print(number)

some_list = ['item']
some_list *= 5
print(some_list)


# WALRUS OPERATOR
# It allows assignment of variables within an expression while returning
# the value of the variable

print(my_var:='Mon Laferte')


# DATA TYPES
 
print(10) # Integers
print(9.9) # Floating-point numbers
print('Hi') # Strings


# CONCATENATION AND REPLICATION
 
print('Peso' 'Pluma') # Concatenation
print('Peso' * 3) # Replication


# PRINT

print('You can print more than', 1, 'value')

lyrics = ['You', 'are', 'all', 'I', 'need']
for word in lyrics:
    print(word, end='_') # end changes the newline of the output for the provide string
print()
print('We', 'can', 'separate', 'the', 'different', 'objects', sep=' <> ')


# INPUT

print("What's your name")
name = input() # takes the input and converts it into a string
print('Hi, {}'.format(name))

country = input('Where are you from? ') # default message
print(f'{country}? Wow!!')


# LENGTH

print(len(name))
print(len(some_list))

if some_list:
    print('the list is not empty') # This is the preferred approach to check emptiness


# CHANGE THE TYPE

a = str(33) # change to string
b = str(1.1)

x = int('10')
y = float('3.1416')

print(a, b, x, y, sep=' - ')
