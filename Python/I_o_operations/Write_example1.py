filename = input("Enter your file name: ")
lines = []
print("Enter content and press any time to \"exit \" to write")

while True:
    line = input()
    if line == "exit":
        break
    else:
        lines.append(line + '\n')
print(lines)

#open
file = open(filename, "w")

#write
file.writelines(lines)

#close
file.close()

print("Your content is ready")