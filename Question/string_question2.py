#WAP to reverse every word of string in proper manner.
#I/O: this is my book
#O/P: siht si ym koob

c = input("Enter your string:")
li = c.split(" ")
for w in li:
    print(w[-1: : -1], end=" ")