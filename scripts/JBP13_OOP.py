class Person:
    rank = "No Rank Yet"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender


student1 = Student("AkaruiYami", 17, "male")
student1.greeting()
