# Methods always call on list

list1 = [34, 67, 58]
list2 = [57, 43, 78]

#append
list1.append(67)
print(list1)

#count
print(list1.count(67))

#index
print(list1.index(58))

#clear
list2.clear()
print(list2)

#insert
list1.insert(0, 230)
print(list1)

#remove
list1.remove(67)
print(list1)

#pop
list1.pop()
print(list1)

#sort
list1.sort()
print(list1)

#reverse
list1.reverse()
print(list1)

#copy
list3 = list1.copy()
print(list3)
