with open("abc.txt", 'r') as file:
    #tell() returns the current cursor position
    print(file.tell())

    #seek()
    file.seek(7)
    print(file.tell())
    print(file.readline())