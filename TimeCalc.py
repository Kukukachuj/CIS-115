seconds = 0
days = 0
hours = 0 
minutes = 0
sec = int(input("Enter the number of seconds you want to convert"))
if sec >= 0 and sec < 60:
    seconds = sec % 60
    print(f'Seconds: ', seconds)
elif sec >= 60 and sec < 3600:
    minutes = sec // 60
    seconds = sec % 60
    print(f'Minutes: ', seconds)
    print(f'Seconds: ', seconds)
elif sec >= 3600 and sec  < 86400:
    hours = sec // 3600
    minutes = (sec % 3600) // 60
    seconds = (sec % 3600) % 60
    print(f'hours: ', hours)
    print(f'Minutes: ', minutes)
    print(f'Seconds: ', seconds)
elif sec >= 86400:
    days = sec // 86400
    hours = (sec % 86400) // 3600
    minutes = ((sec % 86400) % 3600) // 60
    seconds = ((sec % 86400) % 3600) % 60
    print(f'Days: ', days)
    print(f'Hours: ', hours)
    print(f'Minutes: ', minutes)
    print(f'Seconds: ', seconds)
     