text = "Hello, Python is object oritented programming language"

filename = "abc.txt"
#write
file = open(filename, "w")
file.write(text)
file.close()

print("Writing done")