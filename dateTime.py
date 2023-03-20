# dateTime
# python provides date time module where date,time,,timedelta classes

import datetime

# prompt user for values

hour = eval(input("enter hours: "))
minutes = eval(input("enter minutes: "))
seconds = eval(input("enter seconds: "))
milliseconds = eval(input("enter milliseconds: "))

time = datetime.time(hour=hour,minute=minutes,second=seconds,microsecond=milliseconds)
print("time is ",time)

print("hours : ",time.hour)


# getting realtime 
t = datetime.datetime.now()
print(t.hour, ":" ,t.minute)

# give time object, format and display time in 24h 
# to format time object, use strftime() - format object to string
print(t.strftime("%H : %M  %S")) 

print(t.strftime("%I : %M  %p")) # 12 hour system

# date
# can be created using date() whose parameters are year,month,day

years = eval(input("enter year: "))
month = eval(input("enter month: "))
day = eval(input("enter date: "))

siku = datetime.date(year=years, month=month,day=day)
print("the date",siku)
print(siku.year)
print(siku.month)
print(siku.strftime("%a"))

siku = datetime.datetime.now()
print(siku.strftime("%Y/ %b / %d"))

# datetime 
# can be create using datetime()
# parameters are year, month,day,minute,second,microsecond
# given datetime

tarehe = datetime.datetime.now()
print(tarehe.strftime("%y /%B /%m"))


# a program that prompts the user to enter datetime value as string, 
# then convert it into datetime object and display
from datetime import *
datetimeString = str(input("enter datetime in the format  d-m-y H:M "))
datetimeObject = datetime.strptime(datetimeString,"%d-%B-%y %H:%M ")
print("datetime : ",datetimeObject)
print("hour :",datetimeObject.hour)

# prompt the user to enter their date of birth then calculate and display their age
birthMonth = eval(input("enter the month of birth: "))
birthDay = eval(input("enter the day of birth: "))
birthYear = eval(input("enter the year of birth: "))

DOB = datetime.date(year=birthYear,month=birthMonth,day=birthDay)
currentTime = datetime.datetime.today()
age = currentTime.year - DOB.year
print("your age :",age)

# timedelta 
# - rep duration
# created using timedelta()
# parameter are days,hours,minutes,seconds,weeks

deltaTime = datetime.timedelta(days=321,hours=22)
currentTime = datetime.datetime.today()
dd = currentTime - deltaTime
print("the date was ",dd)

# timestamp() 