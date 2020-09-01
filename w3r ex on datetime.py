# Write a Python script to display the various Date Time formats
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
# import datetime
# print("Current date and time:",datetime.datetime.today())
# print('Current year:',datetime.date.today().year)
# print("Current month:",datetime.date.today().month)
# print('Week number:',datetime.date.today().strftime("%W"))
# print("Weekday of the week:",datetime.datetime.today().weekday())
# print("Day of the year:",datetime.datetime.today().strftime("%j"))
# print("Day of the month:",datetime.datetime.today().strftime("%d"))
# print("Day of week:",datetime.datetime.today().strftime("%A"))




# Write a Python program to determine whether a given year is a leap year
# def leap(y):
#     if y%400:
#         return True
#     elif y%100:
#         return False
#     elif y%4:
#         return True
# print(leap(2020))



# Write a Python program to convert a string to datetime
# Jan 1 2014 2:43PM
# def func(stra):
#     import datetime
#     print(datetime.datetime.strptime(stra,"%b %d %Y %I:%M%p"))
#
# func("Jan 1 2014 2:43PM")




# Write a Python program to get the current time in Python
# import datetime
# import time
# print(datetime.datetime.now().time())



# Write a Python program to subtract five days from current date
# import datetime
# print("Current date: ",datetime.date.today())
# print("Current date minus 5 days: ",datetime.date.today()-datetime.timedelta(5))



# Write a Python program to convert unix timestamp string to readable date.
# import datetime
# print(datetime.datetime.fromtimestamp(12033543435).strftime("%Y-%m-%d %H:%M:%S"))



# Write a Python program to print yesterday, today, tomorrow
# import datetime
# print("Yesterday: ",datetime.date.today()-datetime.timedelta(1))
# print("Today: ",datetime.date.today())
# print("Tomorrow: ",datetime.date.today()+datetime.timedelta(1))



# Write a Python program to convert the date to datetime (midnight of the date) in Python
# import datetime
# print(datetime.date.today(), datetime.time.min)



# Write a Python program to print next 5 days starting from today
# import datetime
# for i in range(0,6):
#     print(f"The {i+1} day: ",datetime.datetime.today()+datetime.timedelta(i))



# Write a Python program to add 5 seconds with the current time
# import datetime
# import time
# print("Current time:",datetime.datetime.now().time())
# print("After 5 secs:",(datetime.datetime.now()+datetime.timedelta(0,5)).time())



# convert day-month-year ot day of year
# import datetime
# print(datetime.date.today().strftime("%j"))


# Write a Python program to get current time in milliseconds in Python
# import datetime
# print(datetime.datetime.now().microsecond)


# Write a Python program to get week number
import datetime
# print("Enter a date:")
# a=input()
# b=a.split(",")
# print(datetime.date(int(b[0]),int(b[1]),int(b[2])).isocalendar()[1])


# Write a Python program to find the date of the first Monday of a given week
# import time
# print(time.asctime(time.strptime('2015 50 1',"%Y %W %w")))



# Write a Python program to select all the Sundays of a specified year.
# from datetime import date, timedelta
# def all_sundays(year):
#     # January 1st of the given year
#     dt = date(year, 1, 1)
#     # First Sunday of the given year
#     dt += timedelta(days=6 - dt.weekday())
#     while dt.year == year:
#         yield dt
#         dt += timedelta(days=7)
# for s in all_sundays(2020):
#     print(s)



# Write a Python program to add year(s) with a given date and display the new date.
# import datetime
# from datetime import date
# def addYears(d, years):
#     try:
# #Return same day of the current year
#         return d.replace(year = d.year + years)
#     except ValueError:
# #If not same day, it will return other, i.e.  February 29 to March 1 etc.
#         return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))
#
# print(addYears(datetime.date(2015,1,1), -1))
# print(addYears(datetime.date(2015,1,1), 0))
# print(addYears(datetime.date(2015,1,1), 2))
# print(addYears(datetime.date(2000,2,29),1))




# Write a Python program to get days between two dates
# from datetime import date
# def func(date1,date2):
#     return date1-date2
# print(func(date(2040,12,1),date(2020,12,1)))



# Write a Python program to get the date of the last Tuesday
# import datetime
# today=datetime.date.today()
# offset=(today.weekday()-1)%7
# last_tuesday=today-datetime.timedelta(days=offset)
# print(last_tuesday)


# Write a Python program to get the last day of a specified year and month
# import calendar
# year=2020
# month=12
# print(calendar.monthrange(year,month)[1])



# Write a Python program to get the number of days of a given month and year
# import calendar
# year=2020
# month=11
# print(calendar.monthrange(year,month)[1])


# Write a Python program to add a month with a specified date
# from datetime import date, timedelta
# import calendar
# start_date = date(2014, 12, 25)
# days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
# print(start_date + timedelta(days=days_in_month))



# Write a Python program to count the number of Monday of the 1st day of the month from 2015 to 2016.
# import datetime
# count=0
# for i in range(1,13):
#     a=datetime.date(2015, i, 1)
#     b=datetime.date(2016, i, 1)
#     if (a.weekday()==0 or b.weekday()==0):
#         count+=1
# print(count)



# Write a Python program to print a string five times, delay three seconds
# import time
# for i in range(5):
#     time.sleep(3)
#     print("Ansh is a good boy")



# Write a Python program to get the GMT and local current time
# import time
# print("GMT:",time.strftime("%a, %d %b %Y %I:%M:%S %p %Z",time.gmtime()))
# print("Local current time:",time.strftime("%a, %d %b %Y %I:%M:%S %p %Z"))


# Write a Python program to convert a date to the timestamp
# import datetime
# b=datetime.datetime(2020,12,1)
# print(datetime.datetime.timestamp(b))


# convert to unix timestamp
# import datetime
# import time
# d=datetime.datetime(2020,12,1,23,23)
# unix=time.mktime(d.timetuple())
# print("Time:",unix)



# Write a Python program to calculate two date difference in seconds
# from datetime import datetime, time
# def date_diff_in_Seconds(dt2, dt1):
#   timedelta = dt2 - dt1
#   return timedelta.days * 24 * 3600 + timedelta.seconds
# #Specified date
# date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
# #Current date
# date2 = datetime.now()
# print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
# print()



# Write a Python program to get last modified information of a file
# import datetime
# import os,time
# filestat=os.stat(".")
# date=time.localtime(filestat.st_mtime)
# year=date[0]
# month=date[1]
# day=date[2]
# hour=date[3]
# minute=date[4]
# second=date[5]
# strYear=str(year)[0:]
#
# if (month <=9):
# 	strMonth = '0' + str(month)
# else:
# 	strMonth = str(month)
#
# if (day <=9):
# 	strDay = '0' + str(day)
# else:
# 	strDay = str(day)
#
# print(strYear+"-"+strMonth+"-"+strDay+" "+str(hour)+":"+str(minute)+":"+str(second))



# Write a Python program to calculate an age in year
# from datetime import date
# def func(dob):
#     today=date.today()
#     return today.year-dob.year-((today.month,today.day)<(dob.month,dob.day))
# print(func(date(2002,12,1)))



# Write a Python program to display formatted text output of a month and start weeks on Sunday
# import calendar
# cal=calendar.TextCalendar(calendar.SUNDAY)
# print("First month-2022")
# print(cal.prmonth(2022,1))



# Write a Python program to print a 3-column calendar for an entire year
# import calendar
# cal=calendar.TextCalendar(calendar.SUNDAY)
# print(cal.pryear(2020,3,2))



# Write a Python program to display a calendar for a locale.
# import calendar
# cal=calendar.LocaleTextCalendar(locale='en_DK.utf8')
# print(cal.prmonth(2020,12))



# Write a Python program to get the current week
# import datetime
# Jan1st = datetime.date(2017,10,12)
# year,week_num,day_of_week = Jan1st.isocalendar() # DOW = day of week
# print()
# print("Year %d, Week Number %d, Day of the Week %d" %(year,week_num, day_of_week))
# print()



# Write a Python program to create an HTML calendar with data for a specific year and month
# import calendar
# cal=calendar.HTMLCalendar(calendar.MONDAY)
# print(cal.formatmonth(2020,12))



# Write a Python program display a list of the dates for the 2nd Saturday of every month for a given year
# import calendar
# for month in range(1,13):
#     cal=calendar.monthcalendar(2020,month)
#     first_week=cal[0]
#     second_week=cal[1]
#     third_week=cal[2]
#     if first_week[calendar.SATURDAY]:
#         holi_day = second_week[calendar.SATURDAY]
#     else:
#         holi_day = third_week[calendar.SATURDAY]
#
#     print('%3s: %2s' % (calendar.month_abbr[month], holi_day))



# Write a Python program to get a list of dates between two dates
# from datetime import timedelta, date
#
#
# def daterange(date1, date2):
#     for n in range(int((date2 - date1).days) + 1):
#         yield date1 + timedelta(n)
#
#
# start_dt = date(2015, 12, 20)
# end_dt = date(2016, 1, 11)
# for dt in daterange(start_dt, end_dt):
#     print(dt.strftime("%Y-%m-%d"))




# Write a Python program to generate RFC 3339 timestamp
# from datetime import datetime, timezone
# local_time = datetime.now(timezone.utc).astimezone()
# print()
# print(local_time.isoformat())
# print()



# Write a Python program to validate a Gregorian date
# import datetime
# def check_date(m, d, y):
#     try:
#         m, d, y = map(int, (m, d, y))
#         datetime.date(y, m, d)
#         return True
#     except ValueError:
#         return False
#
# print(check_date(11, 11, 2002))
# print(check_date('11', '11', '2002'))
# print(check_date(13, 11, 2002))

