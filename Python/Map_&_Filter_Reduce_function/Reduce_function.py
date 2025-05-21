# Reduce Function

import functools

def sum(x, y):
    return x + y

mylist = [34, 5, 6, 6]

ans = functools.reduce(sum, mylist)
print(ans)

#minimum

min = functools.reduce(lambda x,y : x if x<y else y, mylist)
print(min)

#Maximum

min = functools.reduce(lambda x,y : x if x>y else y, mylist)
print(min)