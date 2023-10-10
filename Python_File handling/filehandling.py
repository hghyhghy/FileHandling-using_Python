# opening a file in python using python inbuild modules

# by using open()  method and read mode

f = open("src/PythonBasics4/read.txt", "r")

print(f)


# now extracting the contents from that particular file by  using .read() method

text = f.read()


print(text)

# closing the file

f.close()

# creating a new file by using open()  method  and creating it in write mode

f = open("readme1.txt", "w")

print(f)


# if e want to open the file in binary format we may use  rb 


f = open("src/PythonBasics4/read.txt", "rb")

print(f)

text = f.read()

print(text)

f.close()

# WRITTING A FILE

f = open("src/PythonBasics4/file.txt", "w")

f.write("Hello! Python I would like to learn you")

# if we want to add elements from last in file we may use append method


f = open("src/PythonBasics4/file.txt", "a")

f.write("   Plese Support Me!")

# now by using WITH keyword we can append it by using two lines 

with open("src/PythonBasics4/file.txt","a") as f:

       f.write("   I so I will be grateful to you")
