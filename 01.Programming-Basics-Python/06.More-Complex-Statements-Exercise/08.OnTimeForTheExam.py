examHour = int(input())
examMinutes = int(input())
studentHour = int(input())
studentMinutes = int(input())

examTimeInMinutes = examHour * 60 + examMinutes
studentTimeInMinutes = studentHour * 60 + studentMinutes

if examTimeInMinutes < studentTimeInMinutes:
    print("Late")
    minutesLate = studentTimeInMinutes - examTimeInMinutes
    if minutesLate < 60:
        print(f"{minutesLate} minutes after the start")
    else:
        hoursLate = minutesLate // 60
        minutesLate = minutesLate % 60
        if minutesLate < 10:
            print(f"{hoursLate}:0{minutesLate} hours after the start")
        else:
            print(f"{hoursLate}:{minutesLate} hours after the start")
else:
    minutesBefore = examTimeInMinutes - studentTimeInMinutes
    if minutesBefore == 0:
        print("On time")
    elif minutesBefore <= 30:
        print("On time")
        print(f"{minutesBefore} minutes before the start")
    else:
        print("Early")
        hoursBefore = minutesBefore // 60
        minutesBefore = minutesBefore % 60
        if hoursBefore == 0:
            print(f"{minutesBefore} minutes before the start")
        elif minutesBefore < 10:
            print(f"{hoursBefore}:0{minutesBefore} hours before the start")
        else:
            print(f"{hoursBefore}:{minutesBefore} hours before the start")
