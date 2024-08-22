import datetime

timenow = datetime.datetime.now()
hourcrnt = timenow.hour
urname = input('Please enter your name: ')
if 6 <= hourcrnt < 12:
    greeting = "Good morning"
elif 12<= hourcrnt < 18:
    greeting = "Good afternoon"
elif 18<= hourcrnt < 22:
    greeting = "Good evening"
elif hourcrnt < 6 or hourcrnt > 22:
    greeting = "Go to bed"
print(greeting , urname+'!')