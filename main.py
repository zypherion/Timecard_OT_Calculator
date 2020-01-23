911#import math module to enable splitting ints and decimal values:
import math
import datetime

#Set colors for fonts:
green = '\033[32m'
red = '\033[31m'
dColor = '\033[m'

#Print the welcome banner:
print("\033[32m")
print("/-------------------------------------\\")
print("|Tim's Wonderful Time Card Calculator!|")
print("\\-------------------------------------/")
print("\033[m")


#Query user for decimal formatted hours worked:
fridayCheck = input("Is it Friday (y/n)?:")
while fridayCheck != "y":
    print("This tool only works on Fridays, work some more and then come back.")
    fridayCheck = input("Is it Friday (y/n)?:")

arrivalTime = input("Phew.. What time did you arrive today? (ex: 9:00, AM is assumed): ")
timeWorked = float(input("How many hours have you already worked in ADP? (ex: 34.67): "))



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

    #Start calculating the time the user can leave:
    leftTime = datetime.datetime(2000, 1, 1, hoursLeft, minutesLeft, 0)
    leaveTime = arrivalTime + datetime.timedelta(hours=hoursLeft,minutes=minutesLeft)
    leaveTime = format(leaveTime, '%H:%M')
    leaveHour, leaveMinute = leaveTime.split(":")
    leaveHour = int(leaveHour)
    
    #adjust hours to 12hr format
    if leaveHour > 12:
        leaveHour -= 12
    if leaveHour == 12 or leaveHour < 7:
        amPm = "pm"
    else:
        amPm = "am"
    if leaveHour == 0:
        amPm ="am"
    leaveHour = str(leaveHour)
    #leaveMinute = str(leaveMinute)
    leaveList = leaveHour, leaveMinute
    leaveTime = ":".join(leaveList)
    
    #Give the user the computed results:
    print ("You've worked %s%d hours and %d%s minutes so far this week."% (green, hoursWorked, minutesWorked, dColor))
    print ("You still need to work %s%d hours and %d%s minutes to reach 40hrs." % (red, hoursLeft, minutesLeft, dColor))
    lTime = str(leaveTime)
    print ("You can leave at: %s%s%s%s" % (green,lTime,amPm,dColor))