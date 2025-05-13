#negative indexing

name = "Priyal"
print(name)
print(name[3])
print(name[-4])

#reverse string

print(name[-2:-5:-1])

#other methods

#lower method
print(name.lower())
#upper
print(name.upper())
#title
print(name.title())

y = "Hello, i am priyal"

#startswith
print(y.startswith("Hello"))
#endswith
print(y.endswith("priyal"))

#format method
a = 34
b = 45
sum = a+b
ans = "sum of {} and {} is {}"
print(ans.format(a,b,sum))