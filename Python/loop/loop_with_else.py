#loop with else

#print 1 to 10 (normally loop end)
for i in range(1,11):
    print(i)
else:
    print("Loop ends")

print("--------------------------------")

#With break 
for i in range(1,11):
    print(i)
    if i == 5:
        break
else:
    print("Loop ends")

print("--------------------------------")

#Loop not executed
for i in range(1,1):
    print(i)
else:
    print("Loop ends")

print("--------------------------------")

#With while loop

i = 1
while i<=5:
    print(i)
    i= i+1
else:
    print("End loop")