import streamlit as st
import requests
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Weather Forecast", page_icon="🌤️", layout="centered")

# Title and Description
st.title("🌤️ Weather Forecast App")
st.markdown("Get real-time weather info for any city around the world.")

# Input for city name
city = st.text_input("🔎 Enter city name", "")

# Replace with your OpenWeatherMap API key
API_KEY = "0d7b04f896b8c576b71a96b4f823d17d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Display weather data
if city:
    data = get_weather_data(city)

    if data.get("cod") != 200:
        st.error(f"❌ City not found: {data.get('message')}")
    else:
        weather = data['weather'][0]
        main = data['main']
        wind = data['wind']

        # Format datetime
        dt = datetime.utcfromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')

        # Display info
        st.subheader(f"📍 Weather in {city.title()}")
        st.image(f"http://openweathermap.org/img/wn/{weather['icon']}@2x.png")
        st.markdown(f"""
        - 🌡️ **Temperature**: {main['temp']} °C  
        - ☁️ **Condition**: {weather['description'].title()}  
        - 💧 **Humidity**: {main['humidity']}%  
        - 🌬️ **Wind Speed**: {wind['speed']} m/s  
        - 📆 **Date & Time** (UTC): {dt}
        """)
