import numpy as np

np.seterr(all='raise')

try:
    num1 = 2.469135797530864e308
    num2 = 2.469135797530864e308
    sum = num1+num2
    print(sum)

except FloatingPointError as e :
    print(e)