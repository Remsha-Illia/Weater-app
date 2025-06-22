import customtkinter as ctk
from .h_scroll_frame import h_s
from PIL import Image
import os
import json

class Time_Frame(ctk.CTkFrame):
    def __init__(self, child_master, n_column, time, temp, condition):
        ctk.CTkFrame.__init__(
            self,
            master=child_master,
            width=100,
            height=200,
            border_width=2,
            border_color="white",
            fg_color="#91bdc7"
        )
        self.condition = condition.lower().replace(" ", "")
        
        self.grid(row=0, column=n_column, padx = 10)
        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        #300 - 3:00, 600 - 6:00, 2100 - 21:00
        self.time_text = ctk.CTkLabel(
            master = self,
            text = str(int(time)//100) + ":00",
            font = ("Arial", 22)
        )       
        self.time_text.grid(row = 0, column = 0)
        
        self.my_path = os.path.abspath(__file__)
        self.my_dir = os.path.dirname(self.my_path)
        self.my_icon = self.convert_condition()

        self.image = ctk.CTkImage(
            Image.open(self.my_icon),
            size = (75, 75)
        )

        self.image_text = ctk.CTkLabel(
            master = self,
            text = "",
            font = ("Arial", 15),
            image = self.image
        )        
        self.image_text.grid(row = 1, column = 0)
        
        self.temp_text = ctk.CTkLabel(
            master = self,
            text = str(temp) + "°",
            font = ("Arial", 26)
        )        
        self.temp_text.grid(row = 2, column = 0)
    
    def convert_condition(self):
        dir = self.my_dir + "\\..\\..\\icons\\"
        if self.condition == "cloudy":
            icon = dir + "cloudy.png"
        elif self.condition == "rainy":
            icon = dir + "rainy.png"
        elif self.condition == "snowy":
            icon = dir + "snowy.png"
        elif self.condition == "sunny":
            icon = dir + "sunny.png"
        elif self.condition == "partlycloudy":
            icon = dir + "partlycloudy.png"      
        elif self.condition == "mist":
            icon = dir + "mist.png"
        elif self.condition == "overcast":
            icon = dir + "overcast.png"
        else:
            icon = dir + "question.png"
        return icon
        

my_path = os.path.abspath(__file__)
my_dir = os.path.dirname(my_path)
my_db = my_dir + "\\..\\..\\data_base.json"

with open(my_db, "r") as file:
    my_city = json.load(file)
    my_city_name = list(my_city.keys())[0]
    # my_hourly_data = my_city["weather"][-2]["hourly"] 
    my_hourly_data = my_city[my_city_name]['api_data']['weather'][0]['hourly']
    print(my_hourly_data)
n_column = 0

for my_hour in my_hourly_data:
    tf = Time_Frame(h_s, n_column, my_hour["time"], my_hour["tempC"], my_hour["weatherDesc"][0]["value"])
    n_column += 1