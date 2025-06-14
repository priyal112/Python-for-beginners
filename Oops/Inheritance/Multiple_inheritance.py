class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer): # if we change employee and dancer position, output will be changed
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

de = DancerEmployee("Priyal", "Free style")
print(de.name)
print(de.dance)

de.show()

print(DancerEmployee.mro())

