DAYS = 86400
HOURS = 3600 
MINUTES = 60

sec = int(input("Enter the number of seconds you want to convert: "))   

if sec >= 0 and sec < 60:
    seconds = sec % MINUTES
    print(f'Seconds: ', seconds)
    
elif sec >= MINUTES and sec < HOURS:
    minutes = sec // MINUTES
    seconds = sec % MINUTES
    print(f'Minutes: ', minutes)
    print(f'Seconds: ', seconds)
    
elif sec >= HOURS and sec  < DAYS:
    hours = sec // HOURS
    minutes = (sec % HOURS) // MINUTES
    seconds = (sec % HOURS) % MINUTES
    print(f'hours: ', hours)
    print(f'Minutes: ', minutes)
    print(f'Seconds: ', seconds)
    
elif sec >= DAYS:
    days = sec // DAYS
    hours = (sec % DAYS) // HOURS
    minutes = ((sec % DAYS) % HOURS) // MINUTES
    seconds = ((sec % DAYS) % HOURS) % MINUTES
    print(f'Days: ', days)
    print(f'Hours: ', hours)
    print(f'Minutes: ', minutes)
    print(f'Seconds: ', seconds)

     
