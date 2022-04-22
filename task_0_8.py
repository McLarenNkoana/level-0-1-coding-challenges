def time(number):
    mins = number%60
    hours = number//60

    if hours > 1 or hours == 0:
        print(hours,"hours,", end = ' ')
    else:
        print(hours, "hour,", end = ' ')
    if mins > 1 or mins == 0:
        print(mins, "minutes")
    else:
        print(mins, "minute")

time(0)
