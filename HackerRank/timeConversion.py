#HackerRank - Time Conversion

def timeConversion(s):
    am_or_pm = s[8:10]

    if am_or_pm == "PM":
        hour = int(s[0:2])
        if hour == 12:
            hour = '12'
            s = hour + s[2:8]
        else:
            hour += 12
            hour = str(hour)
            s = hour + s[2:8]

    else:
        hour = int(s[0:2])
        if hour == 12:
            hour = '00'
            s = hour + s[2:8]
        else:
            s = s[0:8]

    return s


#Testing

s = ["12:30:00AM", "11:33:45AM", "10:30:00AM", "09:45:23AM", 
    "12:59:00PM", "05:30:00PM", "07:30:00PM", "12:45:54PM"]

for time in s:

    print(f'{time} AM/PM -----> {timeConversion(time)} 24h\n\n')

