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


# Inheritance

class Animal:
    def __init__(self, name):
        # This is a public attribute
        self.name = name
        
    def speak(self):
        print(f'... {self.name}')

# Subclass Dog that inherits from Animal
class Dog(Animal):

    # Override the speak method
    def speak(self):
        print(f'Woof! ... {self.name}')

anm = Animal("Georgie")
dog = Dog("Goofy")

anm.speak()
dog.speak()


# Polymorphism
# Allows you to write code that can work with objects of different classes in a
# uniform way.
# In python it is achieved by using method overriding and overloading
#
# Method overriding is when a subclass provides its own implementation of a method
# defined in the parent class
#
# Method overloading is when multiple methods have the same name but different parameters.
# Python does not support it directly, but it can be achieved using default arguments

class Shape:
    # Area is an abstract method, it is intended tobe overrriden
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(8), Rectangle(9, 1) , Circle(2), Rectangle(3, 3)]
for shape in shapes:
    print(shape.area())
