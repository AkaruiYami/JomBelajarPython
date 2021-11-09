# What is class, object and instance
# Class is a blueprint that we use to create an object
# Instance is an object of the class that we created

# How to create class and instance
class Person:
    # Creating Class Variable
    rank = "No Rank"
    def __init__(self, name, age):
        # Creating Intance Variable
        self.name = name
        self.age = age

    # Creating in class function
    def greetings(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create child class where it parent is class Person
# Child class will inherit class Person
class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender


student_a = Student("AkaruiYami", 18, "Male")
print(student_a.name)