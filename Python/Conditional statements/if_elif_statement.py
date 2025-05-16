#if- elif... else statement

print("Program started")

# take a input from user
n = int(input("Enter number : "))
print("Your number is: ", n)

if n>0:
    print("This is positive number")

elif n<0:
    print("This is negative number")

else:
    print("This is zero")

#+ve value = true
#-ve value = true
#0 = false