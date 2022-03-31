from posixpath import split
from turtle import st


def timeConversion(arr):
    splited = arr.split(":")
    time_period = splited[2][2:]
    hour = splited[0]
    minute = splited[1]
    second = splited[2][0:2]


    if time_period == "AM":
        if time_period == "AM" and int(hour)==12:
            hour="00"
    elif time_period == "PM":
        if time_period == "PM" and int(hour)==12:
            hour="12"
        else:
            hour=str(int(hour)+12)


    return(hour+":"+minute+":"+second)




s = '12:45:54PM'


time = timeConversion(s)
print(time)

