import pandas as  pd
df = pd.read_excel('first.xlsx')
df = pd.concat([df[df.columns[0]]])
x = list(df) 
print("the type of x : ",type(x))
print("the value of x : ",x)