def time(number):
    mins = number%60
    hours = number//60

    if hours > 1:
        print(hours,"hours,", end = ' ')
    else:
        print(hours, "hour,", end = ' ')
    if mins > 1:
        print(mins, "minutes")
    else:
        print(mins, "minute")

time(71)

