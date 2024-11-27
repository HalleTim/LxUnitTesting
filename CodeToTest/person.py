class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def greet(self):
        return f"Hallo, mein Name ist {self.name}."

    def is_adult(self):
        return self.age >= 18