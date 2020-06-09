tm_sec = int(input("Введите время в секундах: "))

hours = tm_sec // 3600
minutes = tm_sec % 3600 // 60
seconds = tm_sec % 60

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

if seconds < 10:
    seconds = '0' + str(seconds)

print(f"{hours}:{minutes}:{seconds}")
