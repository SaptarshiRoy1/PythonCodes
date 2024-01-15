import requests

api_key ="1f53c7e1034b388ab1d4d64d544ee60f"

city = input("Enter city: ")

weather_data=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
# print(weather_data.json())

if weather_data.json()['cod'] == '404':
    print("No City Found")

else:
    weather= weather_data.json()["weather"][0]["main"]
    weather_des = weather_data.json()["weather"][0]["description"]
    temp = round(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']

    print(f"The weather in {city} is: {weather} -> {weather_des}")
    print(f"The temperature in {city} is: {temp}ºF")
    print(f"The humidity in {city} is: {humidity}")