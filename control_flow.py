# COMPARISON OPERATORS

print(1 == 1, 1 != 1, 2 < 1, 2 > 1, 1 <= 1, 1 >= 1)


# BOOLEAN OPERATORS

print(True and False, True or False, not False)


# IF STATEMENTS

name = 'Alan'

if name == 'Alan':
    print('He is Alan')
elif name == 'Steve':
    print('Steve!!')
else:
    print('IDK')


# TERNARY CONDITIONAL OPERATOR

name = 'Jimbo'
print('Jojo' if name != 'Jimbo' else name)
print('Jojo' if name == 'Jojo' else 'Jim' if name == 'Jim' else 'Jimbo')


# SWITCH_CASE STATEMENT

code = 201
match code:
    case 200:
        print('OK')
    case 201:
        print('Created')
    case 300 | 307: # with the or pattern
        print('Redirect')
    case 404 | 401:
        print('Not Found')
    case _:
        print('IDK')

days = ['Monday', 'Friday', 'Saturday']
match days:
    case [a]:
        print(f'The day is {a}')
    case [a, b]:
        print(f'Two days {a} and {b}')
    case [a, b, c]:
        print(f'My favorites days are {c}, {b}, and {a}')

match code:
    case int():
        print('The code is an int')
    case str():
        print('The code is a str')

match code: # Guarding match-case statement
    case int():
        if code > 99 and code < 500:
            print('The code is valid')
    case _:
        print('Code invalid!')


# WHILE LOOP STATEMENT

spam = 0
while spam < 3:
    print("Hi Jon")
    spam += 1

message = 'Do you want a cookie (y/n)?'
while True:
    cookie = input(message)
    message = 'Sure (y/n)?'
    if cookie == 'y':
        break

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


# FOR LOOP

pets = ['Bella', 'Millo', 'Loki']
for pet in pets:
    print(pet)

for i in range(3):
    print(i)

for i in range(0, 15, 3):
    print(i)

for i in [1, 3, 6, 8]:
    if i == 3:
        break
    print('yes', i)
else:
    print('I dont get it') # This will execute if the break is not executed
