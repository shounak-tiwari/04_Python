# default parameterize constructor 
class Employee:
    def __init__(self,id=None,name ="Jhon",age="18+",salary=25000):
        self.id = id
        self.name = name 
        self.age = age
        self.salary  = salary
    
    def show(self):
        print(f"id of employee {self.id} , Name of employee : {self.name} , age of employee : {self.age} and salary of employee : {self.salary}")


E1 = Employee(1001,"Ashwin","21",35000)
E2 = Employee(1002,"Piyush","19",15000)
E3 = Employee(1003,"shree","26",25000)
E4 = Employee(1004,"krishna","24",20000)
E5=  Employee()

E1.show()
E2.show()
E3.show()
E4.show()

E5.show()
