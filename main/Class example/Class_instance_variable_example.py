class Employee:
    company_name = "Apple" #class variable
    noOfEmploye = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.36
        Employee.noOfEmploye +=1

    def showDetails(self):
        print(f"the name of eployee is {self.name} and the raise amount in {self.noOfEmploye} sized {self.company_name} is {self.raise_amount}")


emp1 = Employee("Priyal")
emp1.raise_amount = 0.76    # instance variable
emp1.company_name = "Apple india" # if instance variable available class variable will not show
emp1.showDetails()

Employee.company_name = "Google"
print(Employee.company_name)


emp2 = Employee("Ram") #instance variable is not available class variable will show
emp2.showDetails()