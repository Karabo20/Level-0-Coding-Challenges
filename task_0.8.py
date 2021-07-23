# Task 0.8

def convert_time(minutes):
    hours = 0
    while minutes > 60:
        minutes = minutes - 60
        hours = hours + 1
    print(str(hours)+ " hour, " +str(minutes)+ " minutes ")
convert_time(170)
