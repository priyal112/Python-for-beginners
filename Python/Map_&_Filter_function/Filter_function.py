#filter function example

mylist = [34, 67, 46, 43, 0]

#check even
def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False
    
ob = filter(isEven, mylist)
print(list(ob))

#short method
ob1 = filter(lambda x: True if x%2==0 else False, mylist)
print(list(ob1))