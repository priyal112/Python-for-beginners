#function for checking even number

def isEven(n):
    if n%2==0:
        return True
    else:
        return False

#**************** Calling function ******************
answer = isEven(2)
print(answer)

#second method
n = int(input("Enter number: "))
if isEven(n): #function called
    print("Given number is even")
else:
    print("Given number is not even")


#************** Number in range *********************
for i in range(1, 101):
    if isEven(i):
        print(i, end=" ")