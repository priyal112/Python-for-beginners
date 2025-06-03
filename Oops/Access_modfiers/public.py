class Student:

    #constructor defined
    def __init__(self, name, age):
        self.name = name     #public variable
        self.age = age

obj = Student("priyal", 24)
print(obj.name)
print(obj.age)
