"""Certainly! Let’s explore the topic of Python inheritance from the provided link.

Python Inheritance
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows us to define a class that inherits all the methods and properties from another class. Here are the key points about inheritance:

Parent Class (Base Class):
The class being inherited from is called the parent class or base class.
Any class can serve as a parent class.
For instance, consider a Person class with firstname and lastname properties and a printname method:"""
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Example usage:
x = Person("John", "Doe")
x.printname()

"""
Child Class (Derived Class):
The class that inherits from another class is called the child class or derived class.
To create a child class, pass the parent class as a parameter during its creation.
The Student class below inherits from the Person class:"""

class Student(Person):
    pass

# Example usage:
y = Student("Mike", "Olsen")
y.printname()

"""Adding Functionality to Child Class:
To add functionality to the child class, we can override the parent’s methods or add new properties and methods.
For instance, let’s add an __init__() function to the Student class:"""

class Student(Person):
    def __init__(self, fname, lname):
        # Add properties or other logic here
        super().__init__(fname, lname)  # Call parent's __init__()

# Example usage:
z = Student("Emma", "Smith")
z.printname()


"""
Using super():
The super() function automatically inherits all methods and properties from the parent class.
It eliminates the need to explicitly mention the parent class name.
Example:
"""
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# Example usage:
w = Student("Alice", "Johnson")
w.printname()


"""
Additional Properties:
You can add new properties to the child class. For instance, let’s add a graduationyear property to the Student class.
Remember, inheritance allows you to build upon existing classes, promoting code reusability and organization."""