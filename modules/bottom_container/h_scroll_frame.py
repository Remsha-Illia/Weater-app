import customtkinter as ctk
from ..mainframe import screen

class Horizontal_Scroll(ctk.CTkScrollableFrame):
    def __init__(self, child_master, width, height, border_w, border_color, corner_radius, x, y):
        ctk.CTkScrollableFrame.__init__(
            self,
            master = child_master,
            width = width,
            height = height,
            border_width = border_w,
            border_color = border_color,
            corner_radius = corner_radius,
            fg_color = "#3c5e85",
            orientation = "horizontal"
        )
        self.place(x = x, y = y)
        self.grid_rowconfigure(0, weight=1)

h_s = Horizontal_Scroll(screen, 818, 240, 3, "white", 20, 369, 500) 