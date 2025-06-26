import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "e9e913f5518f1b107d596c23e3fd868e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        result = (
            f"Weather in {city.title()}:\n"
            f"Condition: {weather}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} km/hr"
        )
        result_label.config(text=result)
    else:
        messagebox.showerror("Error", "City not found!")

# GUI setup
window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")
window.config(bg="#f2e6d9")

# Entry
city_entry = tk.Entry(window, width=25, font=("Arial", 14))
city_entry.pack(pady=20)

# Button
get_button = tk.Button(window, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#d4a373", fg="white")
get_button.pack()

# Result
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f2e6d9", justify="left")
result_label.pack(pady=20)

# Run the app
window.mainloop()
