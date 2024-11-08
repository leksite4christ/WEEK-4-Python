class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Creating an instance of the Person class
person = Person("Shawlly", 30, "female")
person.introduce()  # Output: Hello, my name is Shawlly. I am 30 years old and I am female.
