from_filename = input("Enter your source file name: ")
to_filename = input("Enter your destination file name: ")

with open(from_filename, "r") as from_file:
    content = from_file.readlines()
    with open(to_filename, "w") as to_file:
        to_file.writelines(content)

print("Done....")
