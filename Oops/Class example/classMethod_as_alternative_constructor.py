class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    #method 2
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1 = Employee("Priyal", 15000)
print(e1.name)
print(e1.salary)

string = "John-12000"

#method 1 
#e2 = Employee(string.split("-")[0], string.split("-")[1])
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)