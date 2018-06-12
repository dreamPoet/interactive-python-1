#Calculate the number of seconds in a year. 
#Then use the current system time in seconds as well as today's date to compute the year of the Epoch.

import time
import simplegui

year_seconds = 365 * 24* 60 * 60
leap_year_seconds = 366 * 24* 60 * 60

current = time.time()
iteration = 0;
year = 2018


def leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def find_epoch():
    global year
    global current
    
    if current <= leap_year_seconds:
        print year
        timer.stop()
    else:
        if leap(year):
            current -= leap_year_seconds
            year -= 1
        else:
            current -= year_seconds
            year -= 1
            
            
timer = simplegui.create_timer(1, find_epoch)

timer.start()