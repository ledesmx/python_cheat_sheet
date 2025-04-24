# Encapsulation
# It can be achieved by using access modifiers: public, private, and protected.
# Python uses a convention of using underscore prefixes to indicate the acces level

class MyClass:

    # Constructor
    def __init__(self):

        # A single underscore indicates protected access
        self._x = 10

        # Two undersocres indicate private access
        self.__y = 5

        # This is not an attribute
        w = 20

obj = MyClass()

# The protected variable can be accessed outside the class but it is intended
# to be used within the class or its subclasses
print(obj._x)

# The private variable cannot be accessed outside the clas, even by its subclasses
# This will raise an error
# print(obj.__y)

# It cannot be accessed
# print(obj.w)

