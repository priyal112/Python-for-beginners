# prime number check

def isPrime(n):
    f=0
    for i in range(1, n+1):
        if n%i==0:
            f = f+1
    if f == 2:
        return True
    else:
        return False
    
print(isPrime(9))

# print 1 to 100 prime numbers
for i in range(1,101):
    if isPrime(i):
         print(i, end=" ")