# FUNCTION ARGUMENTS, RETURN VALUES

def say_hi(first_name, last_name):
    return f'Hi {first_name} {last_name}'

print(say_hi('Jon', 'Snow'))


# KEYWORD ARGUMENTS

print(say_hi(first_name='Julian', last_name='Ortiz'))


# LOCAL AND GLOBAL SCOPE
# global variables can be read but not modified from local scopes
# unless you use the 'global' statement

global_var = 'Radiohead'

def favorite_band():
    global_var = 'The Smiths' # Declares a new variable in local scope
    print(global_var)

def favorite_band2():
    global global_var # Declare global variable in the scope to modify it
    global_var = 'Beach House'
    print(global_var)

favorite_band()
print(global_var)

favorite_band2()
print(global_var)


# LAMBDA FUNCTIONS
# It can have any number of arguments, but only one expression

add = lambda x, y: x + y
print(add(9, 4))

def make_adder(n):
    return lambda x: x + n # lambda functions work as lexical closures

plus_7 = make_adder(7)
print(plus_7(1))
print(plus_7(4))
print(plus_7(9))
