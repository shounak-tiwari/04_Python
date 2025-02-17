# create list 
l1 = []
# one more function of list class 
l1.append("Universal")
l1.append("Informatics")
l1.append("indore")
l1.append("vijay nagar")
l1.append("bhawarkua")
l1.append("Abhay prashal")
# original list 
print(l1)
# clear the items of list not desctory 
l1.clear()
# for destroy any reference of list class using del 
del(l1)
# after delete the print process return some error because it is not in memory 
# so it return list is not declare inside the enviroment 
print(l1)