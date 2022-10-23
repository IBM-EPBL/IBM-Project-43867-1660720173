#import the necessary package!
import requests
import random
import time
#input the city name
city = input('Enter the city name ')

#Display the message!
print('Displaying Weater report for: ' + city)

#fetch the weater details
url = 'https://wttr.in/{}'.format(city)
req = requests.get(url)

#display the result!
print(req.text)

# temprature and humidity RANDOM value
temp = random.random() 
hum = random.random()

if hum == 36.5:
    print("According to Temperature report you are in normal days")
if hum < 36:
        print("The Temperature is low compare to normal days")
if hum > 36:
            print("The Temperature is high compare to normal days")
if temp == 55:
    print("According to Humidity report you are in normal place")
if temp < 55:
        print("The Humidity is low compare to normal days")
if temp > 55:
            print("The Humidity is high compare to normal days")

