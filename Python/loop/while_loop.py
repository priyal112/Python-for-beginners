# while loop

i = 1
while i<=5:
    print(i)
    i= i+1

print("--------------------------------")

# digit count

n = int(input("Enter number: "))
dcount = 0

while n>0:
    n = n//10
    dcount = dcount+1

print("Count is: ", dcount)
