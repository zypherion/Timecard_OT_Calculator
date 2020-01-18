11#import math module to enable splitting ints and decimal values:
import math
import datetime

#Query user for decimal formatted hours worked:
arrivalTime = input("What time did you arrive today? (ex: 9:00, AM is assumed): ")
timeWorked = float(input("How many hours have you already worked in ADP? (ex: 34.67): "))

#Set colors for fonts:
gColor = '\033[32m'
rColor = '\033[31m'
dColor = '\033[m'

#Verify that it's a calculation we can actually work with:
if timeWorked < 17 or timeWorked > 40:
    #clear screen:
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

    print("Sorry, I can't help you.. You've worked too much already this week or too little..")

#If we can work with it:
else:
    #split and then store arrival time using datetime module:
    arrivalHours, arrivalMinutes = arrivalTime.split(":")
    arrivalHours = int(arrivalHours)
    arrivalMinutes = int(arrivalMinutes)
    arrivalTime = datetime.datetime(2000, 1, 1, arrivalHours, arrivalMinutes, 0)


    #clear screen:
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

    #split decimal formatted hours worked into int holding hours and int holding minutes:
    minutesWorked, hoursWorked = math.modf(timeWorked)

    #Covert the stored decimal value of minutes to an int, and round up:
    minutesWorked = math.ceil(minutesWorked * 60)

    #Convert total time worked into minutes, then subtract from full 40hr week:
    timeWorked = timeWorked * 60 
    timeLeft = 2400 - timeWorked

    #Split timeLeft into minutes/hours left and QC the minutes:
    minutesLeft, hoursLeft = math.modf((timeLeft / 60))
    if minutesWorked > 0:
        minutesLeft = 60 - minutesWorked
    else:
        minutesLeft = 0
    hoursLeft = int(hoursLeft)

    #Calculate the time the user can leave:
    leftTime = datetime.datetime(2000, 1, 1, hoursLeft, minutesLeft, 0)
    leaveTime = arrivalTime + datetime.timedelta(hours=hoursLeft,minutes=minutesLeft)
    leaveTime = format(leaveTime, '%H:%M')
    
    #Give the user the computed results:
    print ("You've worked %s%d hours and %d%s minutes so far this week."% (gColor, hoursWorked, minutesWorked, dColor))
    print ("You still need to work %s%d hours and %d%s minutes to reach 40hrs." % (rColor, hoursLeft, minutesLeft, dColor))
    lTime = str(leaveTime)
    print ("You can leave at: %s%s%s" % (gColor,lTime,dColor))