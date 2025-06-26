import requests

API_KEY = "e9e913f5518f1b107d596c23e3fd868e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    print(f"Weather in {city}:")
    print(f"Condition: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} km/hr")
else:
    print("City not found.")
