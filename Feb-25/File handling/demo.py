from os import *

if path.exists("student.txt") :
    print("file is already creted ")

else:
    with open("student.txt","w") as file :
        print("new file created successfully")