class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        #self.name = name
        #self.id = id
        super().__init__(name, id)
        self.lang = lang

ram = Employee("ram", "34")
Jay = Programmer("jay", "56", "Python")

print(ram.name)
print(Jay.name)
print(Jay.lang)