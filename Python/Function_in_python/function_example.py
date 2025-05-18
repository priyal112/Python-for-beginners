# hoe to create a function
# def keyword

def fun1():
    print("program 1")
    print("program 1")

print("start program")
fun1()

# sum of 2 number
def sum(x,y):
    c = x + y
    print("sum", c)

sum(3,6)
sum(45, 678)

# return use
def sum(x,y):
    c = x + y
    return c

s1 = sum(3,6)
print("sum is", s1)
s2 = sum(45, 678)
print("sum is", s2)