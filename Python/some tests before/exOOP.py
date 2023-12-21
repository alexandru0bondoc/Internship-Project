class Dog:
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

my_dog = Dog("Rex", 4)
print(my_dog.description())
print(my_dog.speak("Woof"))