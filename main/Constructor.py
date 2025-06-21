class Person:

    def __init__(self, name, o):
        print("Hey, I am a person")
        self.name = name
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Priyal", ("developer"))
b = Person("Priy", ("developer"))

a.info()
b.info()