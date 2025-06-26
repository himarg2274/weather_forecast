# weather_app.py

import streamlit as st
import requests

# OpenWeatherMap API details
API_KEY = "e9e913f5518f1b107d596c23e3fd868e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Streamlit page configuration
st.set_page_config(page_title="Weather Forecast", page_icon="🌦️")

# App title
st.title("🌤️ Weather Forecast App")
st.subheader("Get real-time weather updates by city name")

# Input from user
city = st.text_input("Enter City Name")

# Check button
if st.button("Check Weather"):
    if city:
        request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description'].title()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            # Display results
            st.success(f"Weather in {city.title()}")
            st.write(f"**Condition:** {weather}")
            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind} km/hr")
        else:
            st.error("❌ City not found. Please try again.")
    else:
        st.warning("⚠️ Please enter a city name.")
