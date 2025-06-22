import customtkinter as ctk
from .info_container import info_cont
import os
import json
from PIL import Image

class Left_Subcontainer(ctk.CTkFrame):
    def __init__(self, child_master, condition):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            fg_color = "#91bdc7"
        )
        self.grid(row=0, column=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.condition = condition.lower().replace(" ", "")
        
        self.my_path = os.path.abspath(__file__)
        self.my_dir = os.path.dirname(self.my_path)
        self.my_icon = self.convert_condition()
        
        self.image = ctk.CTkImage(
            Image.open(self.my_icon),
            size = (170, 160)
        )

        self.image_text = ctk.CTkLabel(
            master = self,
            text = "",
            image = self.image
        )        
        self.image_text.grid(row = 0, column = 0)
        
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
    my_condition = my_city[my_city_name]["api_data"]["current_condition"][0]["weatherDesc"][0]["value"]

    
left_subcont = Left_Subcontainer(info_cont,my_condition)