#import math module to enable splitting ints and decimal values:
import math

#Query user for decimal formatted hours worked:
timeWorked = float(input("How many hours have you already worked: "))

#split decimal formatted hours worked into int holding hours and int holding minutes
minutesWorked, hoursWorked = math.modf(timeWorked)
minutesWorked = int(minutesWorked * 60)

#Convert all time worked into minutes, then subtract from full week:
timeWorked = timeWorked * 60 
timeLeft = 2400 - timeWorked

#divide timeleft by sixty to convert back into 
minutesLeft, hoursLeft = math.modf((timeLeft / 60))
minutesLeft = int(minutesLeft * 60 + 1)
print ("You've worked %d hours and %d minutes so far."% (hoursWorked, minutesWorked))
print ("You still need to work %d hours and %d minutes to reach 40hrs." % (hoursLeft, minutesLeft))