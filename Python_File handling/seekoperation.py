# seek operation in python

# itneglects some numbers given in the argument and then reads the rest

# by using with keyword  and opening it in read mode

with open("src/Python_File handling/m3.txt", "r") as f:
    # printing the type of it

    print(type(f))

    # now moving to the 10th byte of the string by using seek()  method

    f.seek(10)

    # the tell() function returns the current position in the file

    print(f.tell())

    # now reading the next five  bytes

    data = f.read(5)

    print(data)


# truncate()  function

with open("src/Python_File handling/m4.txt", "w") as f:
    f.write("Hello Python")

    # if we want that our file  should contain not more than any given character length we may use truncate function

    f.truncate(5)

with open("src/Python_File handling/m4.txt", "r") as f:
    print(f.read())
