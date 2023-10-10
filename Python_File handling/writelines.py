# using write line we can create line  in a file

# first of all opening a file in "W"  format

f = open("src/PythonBasics4/m2.txt", "w")

lines = ["Lines 1\n", "Lines 2\n", "Lines 3\n"]

f.writelines(lines)

f.close()
