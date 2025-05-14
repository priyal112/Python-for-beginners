#Methods are called in objects

set1 = {34, 67, 54, 21}

#add
set1.add(88)
print(set1)

#update - more than one element
set1.update([45, 11, 22])
print(set1)

#Discard- no error, remove - error given
#set1.discard(2)
set1.remove(67)
print(set1)

#union
set2 = {34, 3, 7}
un = set1.union(set2)
print(un)

#intersection
inter = set1.intersection(set2)
print(inter)