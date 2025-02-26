import datetime
# currently time & date 
current = datetime.datetime.now()
print("Current time : ",current)
# name of day in full forms
day_name = current.strftime("%A")
print("Day Name of todays in local system : ",day_name)
# name of day in sort format 
day_name = current.strftime("%a")
print("Day name of todays in local system : ", day_name)
