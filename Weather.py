import requests
import tkinter as tk
from tkinter import ttk

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metrimport requests
import tkinter as tk
from tkinter import ttk

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)  # Use `requests.get` here
    data = response.json()

    if data.get("cod") != 200:
        return f"Error: {data.get('message')}"

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    city_name = data['name']

    return f"Weather in {city_name}: {weather_description.capitalize()}, Temperature: {temperature}°C"

def show_weather():
    api_key = '98ca81a112799f6837a5af6308a2421e'  # Replace with your API key
    city = city_entry.get()
    weather_info = get_weather(api_key, city)
    result_label.config(text=weather_info)

app = tk.Tk()
app.title("Weather App")

city_label = ttk.Label(app, text="Enter city:")
city_label.pack(padx=10, pady=5)

city_entry = ttk.Entry(app)
city_entry.pack(padx=10, pady=5)

get_weather_button = ttk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack(padx=10, pady=5)

result_label = ttk.Label(app, text="")
result_label.pack(padx=10, pady=20)

app.mainloop()
ic'
    }
    response = requests.get(base_url, params=params)  # Use `requests.get` here
    data = response.json()

    if data.get("cod") != 200:
        return f"Error: {data.get('message')}"

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    city_name = data['name']

    return f"Weather in {city_name}: {weather_description.capitalize()}, Temperature: {temperature}°C"

def show_weather():
    api_key = '98ca81a112799f6837a5af6308a2421e'  # Replace with your API key
    city = city_entry.get()
    weather_info = get_weather(api_key, city)
    result_label.config(text=weather_info)

app = tk.Tk()
app.title("Weather App")

city_label = ttk.Label(app, text="Enter city:")
city_label.pack(padx=10, pady=5)

city_entry = ttk.Entry(app)
city_entry.pack(padx=10, pady=5)

get_weather_button = ttk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack(padx=10, pady=5)

result_label = ttk.Label(app, text="")
result_label.pack(padx=10, pady=20)

app.mainloop()
