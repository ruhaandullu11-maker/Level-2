import datetime as dt
import time

print('Welcome to the bday countdown')


year = int(input('What year were you born in?\n'))
month = int(input('What month (1 for January, 2 for Febuary,etc...)?\n'))
day = int(input('What day in that month?\n'))

dateofbirth = dt.datetime(year, month, day)

weekdaynames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdaynum = dateofbirth.weekday()
print('I am pretty sure have forgotwhat day of the week it was ...')
print('It was a...let me think...', = ' ')
print('Oh yeah it was a ',weekdaynaweekdaynum])

timern = dt.datetime.now()
thisyear = timern.year
thisbday = dt.datetime(thisyear, mo day)



if thisbday > timern:
    nextbday = thisbday
else:
    nextbday = dt.datetime(thisyear+1, month, day)

print('Your next bday will be on the...', end = ' ')
print(nextbday)
print()
print('Which will be a...', end = ' ')
weekdaynum = nextbday.weekday()
print(weekdaynames[weekdaynum])
print()

d = nextbday - timern

totsecleft = d.seconds
dysleft = d.days

secondsleft = totsecleft % 60
totminsleft = totsecleft //60
hoursleft = totminsleft //60
minsleft = totminsleft % 60


totminsleft, secondsleft  = divmod(totsecleft, 60)
hoursleft, minsleft  = divmod(totminsleft, 60)




while nextbday > timern:
    
    timern = dt.datetime.now()
    d = nextbday - timern
    dysleft = d.days
    totsecleft = d.seconds


    secondsleft = totsecleft % 60
    totminsleft = totsecleft //60
    hoursleft = totminsleft //60
    minsleft = totminsleft % 60

    print('Your next birthday will be in', dysleft, 'days', hoursleft, 'hrs', minsleft, 'mins', secondsleft, 'secs away.')

    time.sleep(1)