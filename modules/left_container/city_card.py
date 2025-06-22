import customtkinter as ctk
from .scroll_frame import vertical_scroll
import requests
import json
import os
import datetime
import zoneinfo
from timezonefinder import TimezoneFinder


class City_Frame(ctk.CTkFrame):
    def __init__(self, child_master, city_name, time, temp, condition, min_max):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width = 236,
            height = 100,
            border_width = 2,
            border_color = "#FFFFFF",
            fg_color = "#91bdc7"
        )
        self.pack(anchor = "center", pady = 7)
        
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.city_label = ctk.CTkLabel(
            master = self,
            text = city_name,
            font = ("Comic Sans MS", 25)
        )
        self.city_label.grid(row = 0, column = 0, sticky = "w", padx=(10,0), pady=(10,0))

        self.time_label = ctk.CTkLabel(
            master = self,
            text = time,
            font = ("Arial", 14)
        )
        self.time_label.grid(row = 1, column = 0, sticky = "w", padx=(10,0), pady=(0,10))

        self.temp_label = ctk.CTkLabel(
            master = self,
            text = temp,
            font = ("Arial", 35)
        )
        self.temp_label.grid(row = 0, column = 1, sticky = "e", padx=(0,10), pady=(10,0))

        self.condition_label = ctk.CTkLabel(
            master = self,
            text = condition,
            font = ("Arial", 16)
        )
        self.condition_label.grid(row = 2, column = 0, sticky = "w", padx=(10,0), pady=(10,10))

        self.min_max_label = ctk.CTkLabel(
            master = self,
            text = min_max,
            font = ("Arial", 14)
        )
        self.min_max_label.grid(row = 2, column = 1, sticky = "e", padx=(0,10), pady=(10,10))

cities = ["Kyiv", "Budapest", "Warsaw", "Vienna", "Prague", "Berlin", "Milan", "Paris", "London", "NewYork"] 

my_city_info = requests.get("https://ipinfo.io/json")
my_city_name = my_city_info.json()["city"]

if my_city_name in cities:
    cities.remove(my_city_name)

cities.insert(0, my_city_name)
    
db_data = {}

for city in cities:

    url = f"http://wttr.in/{city}?format=j1"
    result = requests.get(url).json()
    
    temp = result["current_condition"][0]["temp_C"] + "°"
    condition = result["current_condition"][0]["weatherDesc"][0]["value"]
    if len(condition) > 15:
        condition = condition[0:15] + "..."
    min_max = f"min:{result['weather'][0]['mintempC']} max:{result['weather'][0]['maxtempC']}"
    
    my_lat = result["nearest_area"][0]["latitude"]
    my_long = result["nearest_area"][0]["longitude"]
    
    timezona_name = TimezoneFinder().timezone_at(lat = float(my_lat), lng = float(my_long))
    zona = zoneinfo.ZoneInfo(timezona_name)
    my_time = datetime.datetime.now(zona)
    time = my_time.strftime("%H:%M")
    
    db_data[f"{city}"] = {
        "day_week": my_time.strftime("%A"),
        "date": my_time.strftime("%d.%m.%Y"),
        "time": time,
        "api_data": result
    }

    cf = City_Frame(vertical_scroll, city, time, temp, condition, min_max)

my_path = os.path.abspath(__file__)
my_dir = os.path.dirname(my_path)
my_db = my_dir + "\\..\\..\\data_base.json"

with open(my_db, "w") as file:
    json.dump(db_data, file, indent=4)