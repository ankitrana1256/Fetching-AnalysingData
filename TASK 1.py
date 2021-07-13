import requests
import json

response = requests.get('https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22')
dta = response.json()

class DateAndTime:
        
    def filterdata(d,t):
        for i in dta["list"]:
            if i["dt_txt"].split(" ")[0] == d and i["dt_txt"].split(" ")[1] == t:
                DateAndTime.a = i
                return True
                
            if i["dt_txt"].split(" ")[0] != d and i["dt_txt"].split(" ")[1] != t:
                print("Data out of range...")
                print("Program exited without error...")
                return False
    
    
    def weather():
        data = DateAndTime.a
        result = data["weather"][0]["description"].upper()
        return result
    
    
    def wind():
        data = DateAndTime.a
        result = data["wind"]['speed']
        return result
    

    def pressure():
        data = DateAndTime.a
        result = data["main"]['pressure']
        return result
    

date, time = input("Enter Date and Time: ").split()

flag = DateAndTime.filterdata(date,time) 

while flag:
    user_input = int(input("Enter you choice : "))
    if user_input == 1:
        weather = DateAndTime.weather()
        print(weather)
    elif user_input == 2:
        wind = DateAndTime.wind()
        print(wind)
    elif user_input == 3:
        temp = DateAndTime.pressure()
        print(temp)
    else:
        print("Program exited")
        flag = False