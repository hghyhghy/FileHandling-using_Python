

# readline operation in python 

f=open("src/PythonBasics4/m1.txt" ,"r")

# continuing the while  loop until the file line ends 

# also checking marks of students 

i=0

while True:

       i=i+1

       line =f.readline()

       if not line:

              break


       # splitting the marks by using split method 
       

       m1=line.split(",")[0]

       m2=line.split(",")[1]

       m3=line.split(",")[2]

       # now printing the marks of te students as a f string

       print(f"Marks of student {i} in maths is:{m1}")


       print(f"Marks of student {i} in English is:{m2}")


       print(f"Marks of student {i} in CSE is:{m3}")

       print(line )









      
      

