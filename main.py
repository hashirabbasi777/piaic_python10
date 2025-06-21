class Person:
    """A simple class to represent a person."""
    def __init__(self , name):
        self.name = name
    def __repr__(self):
        pass

person1 = Person("Alice")
print(person1.name)  # This will raise an AttributeError
print(dir(person1))  # This will show the attributes of the person1 object
print(type(person1))  # This will show the type of the person1 object

print(person1.__dict__)  # This will show the __dict__ attribute of the person1 object
print(person1.__class__)  # This will show the __class__ attribute
print(person1.__class__.__name__)  # This will show the name of the class
print(person1.__class__.__module__)  # This will show the module of the class
print(person1.__class__.__qualname__)  # This will show the qualified name of the class
print(person1.__class__.__bases__)  # This will show the base classes of the class
print(person1.__class__.__doc__)  # This will show the docstring of the class
print(person1.__class__.__eq__)