import customtkinter as ctk
from .info_container import info_cont
import json 
import os

class Right_Subcontainer(ctk.CTkFrame):
    def __init__(self, child_master, week_day, time, date):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            fg_color = "#91bdc7"
        )
        self.grid(row=0, column=2)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.current_week_day = ctk.CTkLabel(
            master = self,
            text = week_day,
            font = ("Arial", 30, "bold"),
            text_color = "white"
        )        
        self.current_week_day.grid(row = 0, column = 0)

        self.current_time = ctk.CTkLabel(
            master = self,
            text = time,
            font = ("Arial", 24, "bold"),
            text_color = "white"
        )        
        self.current_time.grid(row = 1, column = 0, pady = 10)

        self.current_date = ctk.CTkLabel(
            master = self,
            text = date,
            font = ("Arial", 18, "bold"),
            text_color = "white"
        )        
        self.current_date.grid(row = 2, column = 0)

my_path = os.path.abspath(__file__)
my_dir = os.path.dirname(my_path)
my_db = my_dir + "\\..\\..\\data_base.json"

with open(my_db, "r") as file:
    db_data = json.load(file)
    my_city = list(db_data.keys())[0]
    
    week_day = db_data[my_city]["day_week"]
    time = db_data[my_city]["time"]
    date = db_data[my_city]["date"]
     
right_subcont = Right_Subcontainer(info_cont, week_day, time, date)