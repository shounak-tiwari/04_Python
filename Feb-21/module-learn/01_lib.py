# datetime library 
import datetime

# now print current date and time 
current_datetime = datetime.datetime.now()
print(f"the current time and date is : {current_datetime}")

# printing date 
current_date =  datetime.date.today()
print("today's date : ",current_date)

# current month 

current_date  =  datetime.date.today()
current_month  =  current_date.month
current_day  = current_date.day
current_year =  current_date.year



print("running month : ",current_month,current_day,current_year)