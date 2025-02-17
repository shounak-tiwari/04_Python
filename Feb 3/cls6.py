#recursion : it is a call by itself 

#wap for print fact OF number using recursion 
def Sum(x:int):
    if x== 0:
        return x
    return x+Sum(x-1)


print(Sum(100))
