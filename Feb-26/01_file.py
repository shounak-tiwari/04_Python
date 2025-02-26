# create files if not exist 
# file is created with the help of two modes only 
# 1. append mode 
# 2. writting mode 
# 3. read mode if exists then reading is possible 
import os
if os.path.exists("student.txt"):
    print("file is already created")
    choseoption = input("for write data press 'W'  and if read then press 'R' : ")
    file = open("student.txt","a")
    if choseoption=='W' or  choseoption== 'w':
        file.write("this is write again and again ")
    else:
        print(file.read())    
else:
    with open("student.txt","a") as file :
        file.write("this is demo file")
        print("file is created as well as stored data successfully")