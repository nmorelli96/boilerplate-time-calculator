#libraries not allowed on this project
def add_time(start, duration, day=None):
#start checks
    try:
        startList = start.split()
        startMeridien = startList[1].lower()
    except:
        return ("Error: start time must be in format '##:## PM' or '#:## AM'")
    if len(startList) != 2 or startMeridien not in ['am', 'pm']:
        return("Error: start time must be in format '##:## PM' or '#:## AM'")
    try:
        startHours = startList[0].split(':')[0]
        startMinutes = startList[0].split(':')[1]
        if len(startMinutes) != 2:
            return ("Error: minutes in start time must have 2 digits")
        if int(startHours) > 12:
            return ("Error: hours in start time can't be greater than 12")
        if int(startMinutes) > 59:
            return ("Error: minutes in start time can't be greater than 59")
    except:
        return ("Error: start time must be in format '##:## PM' or '#:## AM'")
#duration checks
    try:
        if len(duration.split(':')) != 2:
            return ("Error: duration must be in format '##:##' or '#:##'")
        durationHours = duration.split(':')[0]
        durationMinutes = duration.split(':')[1]
        if int(durationHours) < 0 or int(durationMinutes) < 0:
            return ("Error: duration must be in format '##:##' or '#:##'")
        if len(durationMinutes) != 2:
            return ("Error: minutes in duration must have 2 digits'")
        if int(durationMinutes) > 59:
            return ("Error: minutes in duration can't be greater than 59")
    except:
        return ("Error: duration must be in format '##:##' or '#:##'")
#day checks
    if day != None:
        try:
            daysOfWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            dayLow = day.lower()
            if dayLow not in daysOfWeek:
                return ("Error: if you specify a day, it must be a day of the week with no typos")
        except:
            return ("Error: if you specify a day, it must be a day of the week with no typos'")
#time logic
    daysElapsed = 0
    if startMeridien == 'pm':
        convertedStart = [int(startHours) + 12, int(startMinutes)]
    else:
        convertedStart = [int(startHours), int(startMinutes)]
    n = int(durationHours)
    while n > 0:
        convertedStart[0] += 1
        if convertedStart[0] == 24:
            daysElapsed += 1
            convertedStart[0] = 0
        n -= 1
    n = int(durationMinutes)
    while n > 0:
        convertedStart[1] += 1
        if convertedStart[1] == 60:
            convertedStart[0] += 1
            convertedStart[1] = 0
            if convertedStart[0] == 24:
                daysElapsed += 1
                convertedStart[0] = 0
        n -= 1
#formatting for output
    if len(str(convertedStart[1])) == 1:
        convertedStart[1] = '0' + str(convertedStart[1])
    else: convertedStart[1] = str(convertedStart[1])
    if convertedStart[0] >= 11:
        outputMeridien = 'PM'
        convertedStart[0] = str(convertedStart[0] - 12)
        if convertedStart[0] == '0':
            convertedStart[0] = '12'
    else:
        outputMeridien = 'AM'
        convertedStart[0] = str(convertedStart[0])
        if convertedStart[0] == '0':
            convertedStart[0] = '12'
    finalString = convertedStart[0] + ':' + convertedStart[1] + ' ' + outputMeridien
    if day != None:
        dayIndex = daysOfWeek.index(day.lower())
        n = daysElapsed
        while n > 0:
            dayIndex += 1
            if dayIndex == 7:
                dayIndex = 0
            n -= 1
        finalString = finalString + ', ' + daysOfWeek[dayIndex].capitalize()
    if daysElapsed == 0:
        return finalString
    elif daysElapsed == 1:
        return finalString + ' (next day)'
    else:
        return finalString + ' (' + str(daysElapsed) + ' days later)'

#print(add_time("3:19 PM", "3:10"))
#print(add_time("11:30 AM", "2:32", "Monday"))
#print(add_time("11:43 AM", "00:20"))
#print(add_time("10:10 PM", "3:30"))
#print(add_time("11:43 PM", "24:20", "tueSday"))
#print(add_time("6:30 PM", "205:12"))
#print(add_time("2:59 AM", "24:00", "saturDay"))
#print(add_time("11:59 PM", "21:35", "Wednesday"))
