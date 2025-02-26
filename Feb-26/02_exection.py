'''
try
except
finally 
else 
'''
try:
    num1 = int(input("Enter the value of number 1 : "))
    num2 = int(input("Enter the value of number 2 : "))
    result = num1 / num2
    print(result)
except:
    print("some error found")
finally:
    print("this is finally block of code ")