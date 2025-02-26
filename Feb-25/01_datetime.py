import datetime

now = datetime.datetime.now()

'''
specifiers : 
%a : sort of day name 
%A : full day name
%b : 
%B : 
%c :
%C :
...........
'''
month =  now.strftime("%m")
print(month)