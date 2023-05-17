week = {
    "sunday": 0,
    "monday": 1,
    "tuesday": 2,
    "wednesday":3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6
}

def add_time(start, duration, weekday = ""):
    weekday = str(weekday.lower())

    finalHour = ""
    finalMin = ""
    finalPeriod = ""
    addDay = 0
    dayCount = ""

    startingTime = start.split(" ")[0]
    startingPeriod = start.split(" ")[1]
    startingHour = int(startingTime.split(":")[0])
    startingMin = int(startingTime.split(":")[1])
    if startingPeriod == "PM":
        startingHour = startingHour+12
        
    durationHours = int(duration.split(":")[0])
    durationMins = int(duration.split(":")[1])

    finalHour = startingHour + durationHours
    finalMin = startingMin + durationMins

    if finalMin >= 60:
        finalMin = finalMin - 60
        finalHour = finalHour + 1
    
    while finalHour >= 24:
        addDay += 1
        finalHour = finalHour - 24
  

    if addDay == 1:
        dayCount = " (next day)"
    elif addDay > 1:
        dayCount = " (" + str(addDay) + " days later)"

    if finalHour == 0:
        finalPeriod = "AM"
        finalHour = int(finalHour) + 12
    elif finalHour < 12:
        finalPeriod = "AM"
    elif finalHour < 13:
        finalPeriod = "PM"  
    else:
        finalPeriod = "PM"
        finalHour = finalHour - 12  

    if weekday != "":
        finalPeriod = finalPeriod + ", "
        weekday = week[weekday]
        weekday = int(weekday) + addDay
        while weekday >= 7:
            weekday = weekday - 7   


        weekdays = week.items()
        for day in weekdays:
            if day[1] == weekday:
                weekday = str(day[0])                
                dayCount =  weekday.capitalize()+ str(dayCount)

    answer = str(finalHour) + ":" + str(finalMin).rjust(2, "0") + " " + str(finalPeriod)+ dayCount
    

    return answer


print(add_time("11:40 AM", "0:25"))



