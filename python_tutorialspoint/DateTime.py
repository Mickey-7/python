import time

# What is Tick?
# Time intervals are floating-point numbers in units of seconds.
# Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).

# There is a popular time module available in Python which provides functions
# for working with times,and for converting between representations.
# The function time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970 : ", ticks)
# Number of ticks since 12:00am, January 1, 1970 :  1588908152.7388477

# ------------------------------------------------------------------------------------------------------------------------

# Getting current time

localtime = time.localtime(time.time())
print("Local current time : ", localtime)
# Local current time :  time.struct_time(tm_year=2020, tm_mon=5, tm_mday=8, tm_hour=11, tm_min=22, tm_sec=32,
# tm_wday=4, tm_yday=129, tm_isdst=0)

# ------------------------------------------------------------------------------------------------------------------------

# Getting formatted time

localtime = time.asctime(time.localtime(time.time()))
print("Local current time : ", localtime)
# Local current time :  Fri May  8 11:27:23 2020

# ------------------------------------------------------------------------------------------------------------------------

# Getting calendar for a month
# no need to install calendar package
import calendar

cal = calendar.month(2017, 5)
print("here is calendar")
print(cal)
# here is calendar
# May 2017
# Mo Tu We Th Fr Sa Su
# 1  2  3  4  5  6  7
# 8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31
