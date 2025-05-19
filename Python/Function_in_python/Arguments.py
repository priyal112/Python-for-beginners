#type of arguments

#requied arguments
def sayHello(name):
    print("Hello", name)
sayHello("Priyal")


#keywords arguments
def product(a, b):
    print("value of a", a)
    print("value of b", b)
    print("Product", (a*b))

product(34, 65)
product(a = 65, b = 34) #keyword


#default arguments
def sayHello(name = "priyal"):
    print("Hello", name)
sayHello()
sayHello("Priyal")


#variable length arguments
def sum(*vals):
    s = 0
    for i in vals:
        s= s+i
        print(i)
    print("sum is", s)

sum(2,4)