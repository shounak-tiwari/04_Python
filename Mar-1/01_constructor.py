'''
Python : Constructor __init__ / initilization
Constructor is a special method which call automatically when object is initilize with class


type of constructor : 
1. Default constructor 
2. parameterize constructor 
3. default paramter  constructor
4. private constructor 
5. constructor using inheritance 
6. cnostructor overloading using default arguments
7. constructor overloading using *args and **kwargs
8. static constructor using @static method 
'''


#default constructor 
class Record:
    def __init__(self):
        self.Name = input("Name of student : ")
        self.Contact = int(input("Enter the contact  : "))

    def Show(self):
        print("Name : ",self.Name)
        print("Contact : ",self.Contact)

    
Ashwin = Record()

Vishal =Record()

Lakhan = Record()

Piyush = Record()

Ashwin.Show()

