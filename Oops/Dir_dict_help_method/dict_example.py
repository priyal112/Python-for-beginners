class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p1 = Person("Priyal", 24)
print(p1.__dict__)