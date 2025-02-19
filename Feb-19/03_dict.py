import random  as ran
student = dict()

while True:
    enrollment_number = f"pm4unipy{ran.randint(250101,253112)}"
    add_more = input("press Y for add new and terminate N : ")
    if add_more=="Y" or add_more =="y":
        Name = input("Enter the name of student : ")
        Contact =  input("Enter the Contact of student : ")
        Email = input("Enter the Email of student : ")
        Address = input("Enter the Address of student : ")

        student[enrollment_number] = {"Name" : Name,"Contact" : Contact,"Email":Email,"Address":Address}
    
    else:
        print("-----Thanks----visit again------")
        break
    



print(student)
