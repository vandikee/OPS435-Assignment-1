#!/usr/bin/env python3
"""
PS435 Assignment 1 - Winter 2020
Program: a1_amalekzadeh2.py (replace student_id with your Seneca User name)
Author: "arshia malekzadeh"
The python code in this file (a1_amalekzadeh2.py) is original work written by
"arshia malekzadeh". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
"""

import os
import sys
global step1
step1 = ""
i=1
# Defines usage function to refer to later
def usage():
	"""
	Prints how to use the script  
	"""
	use = """
	Usage: a1_amalekzadeh2.py [--step] YYYY-MM-DD + or -n
    Takes a date (date) and a number of days (num_of_days) as arguments
    and returns a precise number of days mentioned.
    Positional Arguments:
    --step - Verbosely prints each day to the result
    date - date in YYYY-MM-DD format
    num_of_days - number of days forward or backward (backward is shown with negative sign (-) )
    EX   a1_amalekzadeh2.py 20170501 4
         a1_amalekzadeh2.py --step 20000507 -5
         a1_amalekzadeh2.py 20150722 -10
         a1_amalekzadeh2.py --step 20150501 2 
        """
	print (use)
	exit()

def is_valid_date(date1):
           
        """
	is_valid_date(date) -> str
		valid_date() takes a date string in 'YYYY-MM-DD' format and checks if it is a valid date or not, then it will return either true or false  
		EX:      is_valid_date('20200131') -> 'true'
                         is_valid_date('20110515') -> 'true'
			 is_valid_date('1234567898') -> 'false'
			 is_valid_date('abcdsferg') -> 'false'
	"""
	#check if the entered argument has a real date properties
        date1 = str(sys.argv[i])
        if len(date1) != 10 or date1.isdigit():
                print("error:the argument entered does not have a valid date format")
                return("False")



        #the purpose of the lines below is to split the received date argument into year, month and day as long as the correct fomrat is entered.
        year1 = int(date1[0:4])
         
        month1 =int(date1[5:7])

        day1 = int(date1[8:10])
        
	#then we check to see if each object(year1, month1, day1) has the right properties 
        if   int(day1) > 31:
                print ("error: the value for the day is not valid")
                return("False")
        elif int(month1) > 12:
                print("error: the value for the month is not valid")
                return("False")
        else:
                return("True")



def leap_year(year1):
        """
        leap_year(year1) -> str
                leap_year() is used to deretmine if the given year is a leap year or not.
                EX:      leap_year('2019') -> 'false'
                         leap_year('1601') -> 'false'
                         leap_year('2156') -> 'true'
                         leap_year('2020') -> 'true'
        
                In the Gregorian calendar, three criteria must be taken into account to identify leap years:
                1-The year can be evenly divided by 4;
                2-If the year can be evenly divided by 100, it is NOT a leap year, unless;
                3-The year is also evenly divisible by 400. Then it is a leap year.
          """
#lets check to see if the given year is a leap year or not
        leapyear=year1 % 4
        if leapyear == 0:
                isleapyear = "True"
        else:
                isleapyear = "False"
        leapyear == year1 % 100
        #leapyear2 = year1 % 400  
        if leapyear == 0 :
                isleapyear = "True"
        #else:
        #       isleapyear = "false"
        leapyear = year1 % 400
        if leapyear == 0:
                isleapyear = "True"
        return(isleapyear)
                                 


def num_of_days_in_mon(year):
        if  isinstance(year, str):
                year = int(year)
        #cheking for the existense of the leap year before adding a day to the february 
        if leap_year(year) == "True":
                feb_days = 29
        else:
                feb_days = 28
        #monthdays is the number of days in a month ordered by month:days 
        monthdays = { 1:31, 2:feb_days, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        return(monthdays)






def tomorrow(date1):
	"""
	tomorrow(date1) -> str
		this funtion gets  date string in 'YYYY-MM-DD' format and returns 
		a date string for the next day in the same format.
             EX: tomorrow('20171229') -> '20171230'
	     	 tomorrow('20180331') -> '20180401'
	    	 tomorrow('20180520') -> '20180521'
	"""
	#returns tomorrow's date with the date1 argument given
#	if isinstance(date1, int):
#                date1 = str(date1)
	if is_valid_date(date1) == "True":
                year1  = int(date1[0:4])
                month1 = int(date1[5:7])
                day1   = int(date1[-2:])
                #gives us the next day
                rday = day1 + 1

                monthdays = num_of_days_in_mon(year1)

		#the script should change to a new month if the number accumulated for the month is more than what is allowed.

                if rday > monthdays[month1]:
                        nday = rday % monthdays[month1]
                        rmonth = month1 + 1
                else:
                        nday = rday
                        rmonth = month1
                if rmonth > 12:
                        nmonth = 1
                        nyear  = year1 + 1
                else:
                        nmonth = rmonth
                        nyear = year1
                newdate = str(nyear)+"-"+str(nmonth).zfill(2)+"-"+str(nday).zfill(2)
                return newdate
	else:
		exit()


def yesterday(date1):
	"""yesterday(argdate) -> str
        this funtion gets  date string in 'YYYY-MM-DD' format and returns 
        a date string for the day before in the same format.
   EX:  yesterday('20150520') -> '20150521'
	yesterday('20100101') -> '20091231'
	
	"""
	#returns yesterday's date with the date1 argument given
	if is_valid_date(date1) == "True":
                year1  = int(date1[0:4])
                month1 = int(date1[5:7])
                day1   = int(date1[-2:])
		#if the leap year is true , then 1 day will be added to the february 
                if leap_year(year1) == "True":
                        feb_days = 29
                else:
                        feb_days = 28
                rday = day1 - 1
                monthdays = num_of_days_in_mon(year1)
		#the script should change to the last month if the number in the rday is equal to 0.
                if rday < 1:
                        rmonth = month1 - 1
                        if rmonth < 1:
                                        nday = 31
                        else:
                                changement = monthdays[rmonth]
                                nday = changement
                else:
                       	nday = rday
                       	rmonth = month1
                if rmonth < 1:
                        nmonth = 12
                        nyear  = year1 - 1
                else:
                        nmonth = rmonth
                        nyear = year1
                newdate = str(nyear)+"-"+str(nmonth).zfill(2)+"-"+str(nday).zfill(2)
                return newdate
	else:
		exit()

def final(date1,days):
	"""
	final(date1,days) -> str
		this funtion takes a date string followed by the number of days, positive or negative and
                returns the desired dateaccordingly  
	
		EX:      final('20171021','1') -> '20171022'
			 final('20200131','-2') -> '20200129'
			 final('20150228','-7') -> '20150221'
	"""
		#since we always want an integer for the ouput , the numbers must be rounded to avoid any malfuction
	global step1
	if __name__ != "__main__":
                step1 = "False"
	days = round(int(days))
	#use tomorrow function for positive days
	if days > 0:
                if step1 == "True":
                        print(tomorrow(date1))
                tdate = tomorrow(date1)
                while days != 1:
                        tdate = tomorrow(tdate)
                        if step1 == "True":
                                print(str(tdate))
                        days = days - 1
                if step1 == "False":
                        print(str(tdate))
	#use yesterday function for negative days
	elif days < 0:
                if step1 == "True":
                        print (yesterday(date1))
                ydate = yesterday(date1)
                while days != -1:
                        ydate = yesterday(ydate)
                        if step1 == "True":
                                print(str(ydate))
                        days = days + 1
                if step1 == "False":
                        print(str(ydate))
	else:
                        days = 0
                        return date1

if __name__ == "__main__":
        if ((len(sys.argv) >= 5 or len(sys.argv) <= 2)):
                usage()
        if sys.argv[1] == "--step":
                step1 = "True"
                i = i + 1
                date1 = str(sys.argv[i])
                argopt = sys.argv[i+1 ]
                final(date1,argopt)
        else:
                step1 = "False"
                date1 = sys.argv[1]
                argopt = sys.argv[2]
                final(date1,argopt)
