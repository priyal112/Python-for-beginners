# lambda example

def sq(x):
    return x*x

sq1 = lambda x:x*x

print(sq(3))
print(sq1(9))

# function within a function

def fun1(fun2, x):
    return fun2(x)
     
r = fun1(lambda x:x*6, 5)
print(r)