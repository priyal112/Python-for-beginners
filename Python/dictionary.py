# Example

#create
d1 = {
    'name':'priyal',
    'city':'jabalpur',
    'number':34567
}

print(d1)
print(type(d1))

d2 = dict() #blank dictionary
print(d2)

#access

print(d1['name'])
print(d1['city'])

#update
d1['name'] = "abc"
print(d1['name'])

#Delete
del d1['number']
print(d1)

#traverse
for key in d1:
    print(key, "==", d1[key])

print("---------------") 

for key,value in d1.items():
    print(key, ":", value)
