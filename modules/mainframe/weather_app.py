import customtkinter 

w = 1280
h = 800

screen = customtkinter.CTk(fg_color = "#91bdc7") 
screen.title("Weather App")

x = screen.winfo_screenwidth() // 2 - w // 2
y = screen.winfo_screenheight() // 2 - h // 2

screen.geometry(f"{w}x{h}+{x}+{y}")
