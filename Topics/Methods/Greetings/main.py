class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print("Hello, I am " + self.name.strip() + "!")


name_in = input()
person = Person(name_in)
person.greet()
