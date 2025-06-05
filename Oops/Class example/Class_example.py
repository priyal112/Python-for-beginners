class Person:
    name = "Priyal"
    age = 24
    occupation = "developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()

a.name = "Priy"
a.age = 23

b.name = "Ram"
print(a.name, b.name)

a.info()
b.info()
c.info()
