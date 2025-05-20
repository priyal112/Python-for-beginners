# Map function example

# long method
def fun1(x):
    return x + 1

mylist = [34, 67, 56, 455]

#map
ob = map(fun1, mylist)
print(ob)
print(list(ob))

#short method
print(list(map(lambda x: x*x, mylist)))

#multiple list
mylist1 = [45, 3, 2, 5]

newlist = list(map(lambda x, y: x+y, mylist, mylist1))
print(newlist)