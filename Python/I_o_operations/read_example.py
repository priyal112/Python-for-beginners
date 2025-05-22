# open
file = open("abc.txt", "r")

#read

#ans = file.read(2)  #2 character
#print(ans)

#result = file.readline()  # one line
#print(result)

answer = file.readlines()  # multiple lines
#print(answer)

for l in answer:
    print(l, end="")

#close
file.close()