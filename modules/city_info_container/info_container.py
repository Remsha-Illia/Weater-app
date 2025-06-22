import customtkinter as ctk
from ..mainframe import screen

class Info_Container(ctk.CTkFrame):
    def __init__(self, child_master, width, height, x, y):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width = width,
            height = height,
            fg_color = "#91bdc7"   
        )
        self.place(x = x, y = y)

        self.grid_propagate(False)

        self.grid_rowconfigure(0, weight=1)
          
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

info_cont = Info_Container(screen, 865, 455, 369, 25)