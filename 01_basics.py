
# Data Types
# Python supports various data types such as int, float, str, list, tuple, set, and dict.

# Example: Different Data Types in Python
integer_example = 10  # Integer type
float_example = 10.5  # Float type
string_example = "Hello, Python!"  # String type
list_example = [1, 2, 3, 4, 5]  # List type
tuple_example = (1, 2, 3, 4, 5)  # Tuple type
set_example = {1, 2, 3, 4, 5}  # Set type
dict_example = {"name": "John", "age": 25}  # Dictionary type

# Operators
# Python includes arithmetic, comparison, logical, bitwise, assignment, identity, and membership operators.

# Example: Arithmetic Operators
sum_example = 10 + 5  # Addition
difference_example = 10 - 5  # Subtraction
product_example = 10 * 5  # Multiplication
division_example = 10 / 5  # Division

# Conditional Statement
# if, elif, else are used for decision-making based on conditions.

# Example: Conditional Statement
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Looping Statement
# Python supports loops like for and while for iterative execution.

# Example: For Loop
for i in range(5):
    print(f"Loop iteration {i}")

# Functions
# Functions are reusable blocks of code that perform a specific task.

# Example: Function Definition
def greet(name):
    """This function greets a person."""
    return f"Hello, {name}!"

print(greet("Alice"))

# Python OOPs (Object-Oriented Programming)
# Concepts like class, object, inheritance, polymorphism, encapsulation, and abstraction.

# Example: Class and Object
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

dog = Animal("Dog")
print(dog.speak())

# Global and Local Variables
# Global variables are accessible throughout the program, whereas local variables are confined to functions.

# Example: Global and Local Variables
x = 10  # Global variable

def function_example():
    x = 5  # Local variable
    print(f"Local x: {x}")

function_example()
print(f"Global x: {x}")

# Constructors
# Constructors are special methods used for initializing objects.

# Example: Constructor in Python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show_details(self):
        return f"Car: {self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.show_details())

# Tips/ Tricks
# Using list comprehensions, lambda functions, and other Pythonic techniques.

# Example: List Comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# Inheritance
# Inheritance allows a class to inherit attributes and methods from another class.

# Example: Inheritance
class Dog(Animal):  # Inheriting from Animal class
    def speak(self):
        return f"{self.name} barks."

dog = Dog("Bulldog")
print(dog.speak())

# Polymorphism
# Polymorphism allows objects to be treated as instances of their parent class.

# Example: Polymorphism
animals = [Dog("Bulldog"), Animal("Cat")]

for animal in animals:
    print(animal.speak())

# File Handling
# Opening, reading, writing, and closing files in Python.

# Example: Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, file handling in Python!")

# Exception Handling
# Handling runtime errors using try, except, else, and finally.

# Example: Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always executes.")

# Python *args and **kwargs
# Used for passing a variable number of arguments to a function.

# Example: *args and **kwargs
def demo_args(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

demo_args(1, 2, 3, name="Alice", age=30)

# Python Iterators
# Iterators are objects that can be iterated upon.

# Example: Creating an Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_iter = iter(MyNumbers())
for number in my_iter:
    print(number)

# Python Generators
# Generators are used to create iterators using the yield statement.

# Example: Generator Function
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
for value in gen:
    print(value)

# Python Decorators
# Decorators are functions that modify the functionality of other functions.

# Example: Function Decorator
def decorator_example(func):
    def wrapper():
        print("Function is about to be called.")
        func()
        print("Function has been called.")
    return wrapper

@decorator_example
def say_hello():
    print("Hello!")

say_hello()

# Python Pytest Fixtures
# Fixtures are used to setup preconditions for testing.

# Example: Pytest Fixture (not executable here, use in a test environment)
# import pytest
# @pytest.fixture
# def input_data():
#     return {"key": "value"}

# def test_example(input_data):
#     assert input_data["key"] == "value"

# Python with MySQL
# Connecting Python to MySQL database using a library like mysql-connector-python.

# Example: Connecting to MySQL (requires mysql-connector-python)
# import mysql.connector
# db = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword",
#     database="yourdatabase"
# )
# cursor = db.cursor()
# cursor.execute("SELECT * FROM yourtable")
# for row in cursor.fetchall():
#     print(row)
