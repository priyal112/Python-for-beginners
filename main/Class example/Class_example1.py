class Employee:

    #method 1 
    def __init__(self, name):
        self.name = name

    def showDetails(self):
        print(f"the name of eployee is {self.name}")

    #method 2 
    def showDetails(self):  # remove self
        print(f"the name of eployee is {self.name}")

#method 1 
emp1 = Employee("Priyal")
emp1.showDetails()

#method 2
Employee.showDetails(emp1)