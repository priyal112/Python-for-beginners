class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The name of the employee is {self.name}"
    
    def __repr__(self):
        return f"Employee'{self.name}'"
    
    def __call__(self):
        print("Hello")
    
#run emp 