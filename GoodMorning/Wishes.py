import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if hour<12 and hour>0:
    print("Good Morning sir")
elif hour>18 and hour<0:
    print("Good Evening!")
else:
    print("Good Afternoon!")