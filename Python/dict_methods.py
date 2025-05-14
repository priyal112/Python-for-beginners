d1 = {
    'name':'priyal',
    'city':'jabalpur',
    'number':34567
}

#copy
d2 = d1.copy()
print(d2)

#items
#print(d1.items())  --- key value of tuple

for t in d1.items():
    print(t)

keys = d1.keys()
print(keys)    

v = d1.values()
print(v)

#get
print(d1.get('name'))

#clear

d1.clear()
print(d1)