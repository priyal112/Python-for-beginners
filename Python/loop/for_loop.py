# for loop

# 1to 15 print
for i in range(1,16,1):
   print(i)

print("--------------------------------")

#step changed
for i in range(1,10,2):
   print(i)

print("--------------------------------")

#print 5 to 1
for x in range(5,0,-1):
   print(x)

print("--------------------------------")

#list in loop
list=[34, 5654, 5675, 345678, 3456]

for n in list:
   print(n)

print("--------------------------------")

#print sum of numbers
n = int(input("Enter your number: "))
sum = 0

for i in range(1, n+1):
   sum = sum + i

print("Sum is: ", sum)
