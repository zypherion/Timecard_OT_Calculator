#import math module to enable splitting ints and decimal values:
import math

#Query user for decimal formatted hours worked:
timeWorked = float(input("How many hours have you already worked: "))

#clear screen:
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
wColor = '\033[32m'
lColor = '\033[31m'
dColor = '\033[m'

#split decimal formatted hours worked into int holding hours and int holding minutes
minutesWorked, hoursWorked = math.modf(timeWorked)
minutesWorked = math.ceil(minutesWorked * 60)

#Convert all time worked into minutes, then subtract from full week:
timeWorked = timeWorked * 60 
timeLeft = 2400 - timeWorked

#divide timeleft by sixty to convert back into 
minutesLeft, hoursLeft = math.modf((timeLeft / 60))
if minutesWorked > 0:
    minutesLeft = 60 - minutesWorked
else:
    minutesLeft = 0

print ("You've worked %s%d hours and %d%s minutes so far."% (wColor, hoursWorked, minutesWorked, dColor))
print ("You still need to work %s%d hours and %d%s minutes to reach 40hrs." % (lColor, hoursLeft, minutesLeft, dColor))