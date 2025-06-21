class Employee:
    def __init__(self):
       self.__name = "Priyal"

a = Employee()
#print(a.__name)  #can't be accessed directly

print(a._Employee__name)   # can be accessed indirectly