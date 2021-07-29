def convert_time(minutes):
    hours = 0
    while minutes > 59:
        minutes = minutes - 60
        hours = hours + 1
    if hours <= 1 and minutes <= 1:
        print(str(hours)+ " hour, " +str(minutes)+ " minute")
    elif hours > 1 and minutes <= 1:
        print(str(hours)+ " hours, " +str(minutes)+ " minute")
    elif hours <= 1 and minutes > 1:
        print(str(hours)+ " hour, " +str(minutes)+ " minutes")
    else:
        print(str(hours)+ " hours, " +str(minutes)+ " minutes ")

