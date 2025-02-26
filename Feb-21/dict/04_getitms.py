dct1 ={"Name" : "Nehal","Contact" : "9893949596","E-mail" : "nehal@gmail.com","Address" : "Navlakha indore" }


'''
x = dct1.get("Name")
print(x)
y = dct1.get("E-mail")
print(y)
'''

# x = dct1.items()
# print(x)

dct1.setdefault("percentage","77.56%")
print(dct1)

value = dct1.values()
print(value)