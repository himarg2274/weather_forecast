
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

API_KEY = "e9e913f5518f1b107d596c23e3fd868e"
BASE_URL_CURRENT = "http://api.openweathermap.org/data/2.5/weather"
BASE_URL_FORECAST = "http://api.openweathermap.org/data/2.5/forecast"

st.set_page_config(page_title="Weather Forecast", page_icon="🌦️")
st.title("🌤️ Weather Forecast App")
st.subheader("Get current and today's future weather in 3-hour intervals")

city = st.text_input("Enter City Name")

if st.button("Check Weather"):
    if city:
       
        current_url = f"{BASE_URL_CURRENT}?q={city}&appid={API_KEY}&units=metric"
        current_response = requests.get(current_url)

        forecast_url = f"{BASE_URL_FORECAST}?q={city}&appid={API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)

        if current_response.status_code == 200 and forecast_response.status_code == 200:
            current_data = current_response.json()
            forecast_data = forecast_response.json()

            
            weather = current_data['weather'][0]['description'].title()
            temp = current_data['main']['temp']
            humidity = current_data['main']['humidity']
            wind = current_data['wind']['speed']

            st.success(f"Weather in {city.title()}")
            st.write(f"**Condition:** {weather}")
            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind} km/hr")

            st.markdown("---")
            st.subheader("🌡️ Forecast (3-hour intervals for Today)")

            forecast_list = forecast_data['list']

            today = datetime.now().date()
            rows = []

            for entry in forecast_list:
                time = datetime.fromtimestamp(entry['dt'])
                if time.date() == today:
                    temp = entry['main']['temp']
                    desc = entry['weather'][0]['description'].title()
                    rows.append({
                        "Time": time.strftime('%I:%M %p'),
                        "Temperature (°C)": temp,
                        "Condition": desc
                    })

            if rows:
                df = pd.DataFrame(rows)
                st.table(df)
            else:
                st.warning("No forecast data found for today.")

        else:
            st.error("❌ City not found or API issue.")
    else:
        st.warning("⚠️ Please enter a city name.")
