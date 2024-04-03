import requests
apikey='c4c551a1026bba06d9893f65a1fef1c3'
print("********************** WELCOME TO WEATHER APP **********************")
print(" ")
input_city = input("Enter the city name: ")
url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={input_city}&appid={apikey}')
data = url.json()
if(data['cod']=='404'):
    print("city not found")
    exit()
else:
    weather = data['weather'][0]['main']
    celsius_temp =data['main']['temp']-273.15
    far_temp=data['main']['temp']
    min_temp = data['main']['temp_min']-273.15
    max_temp = data['main']['temp_max']-273.15
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    windspeed = data['wind']['speed']
print("---------------------------------------------------------------------")
print(f"The temperature in {input_city} is: {celsius_temp:.2f}°c. or {far_temp:.2f}°f.")
print(f"The weather in {input_city} is: {weather}.")
print(f"The minimum temperature in {input_city} is: {min_temp:.2f}°c.") 
print(f"The maximum temperature in {input_city} is: {max_temp:.2f}°c.")
print(f"The humidity in {input_city} is: {humidity}%.")
print(f"The pressure in {input_city} is: {pressure}hPa.")
print(f"The wind speed in {input_city} is: {windspeed}m/s.")