try:
    no1= 10
    no2= 0 
    print(no1/no2)

except ArithmeticError as e:
    print("arithmetic error")

except:
    print("error ")