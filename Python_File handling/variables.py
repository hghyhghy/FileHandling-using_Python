# global variable

# it is a variable  which we can create outside of the the function and use it inside the function

x = 5

print(x)

# now creating a function and printing that variable inside it


def hello():
    print(x)

    print("Hello  Subham")


# calling the function

hello()

# now let us take another example

# taking global variable
x = 9

print(x)

# creating a function


def ofYes():
    # taking local variable

    x = 8

    print(f"The global x is {x}")

    print("Virat Kohli Is a chase master")


# calling the function

ofYes()

print(f"The global variable is {x}")

# taking another example 

x=10 # global variable can be accessed anywhere

# creating a function 

# to change the global   variable inside a function we use global keyword 

def my_function():
    
    global x

    x=8
    
    y=5 # local variable 

    print(y)

# calling the function 

my_function()

# calling the global variable x 

print(x)

# But  if  we want to  call the y it return error as it is a local variable and only accessed inside the function 

