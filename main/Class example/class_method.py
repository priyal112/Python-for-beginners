class Employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    @classmethod  #first argument as a class
    def changeCompany(cls, newCompany):
        cls.company = newCompany    

e1 = Employee()
e1.name = "Priyal"
e1.show()

e1.changeCompany("Apple")
e1.show()
print(Employee.company)
