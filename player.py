#Import's
import customtkinter
from tkinter import messagebox
from api import get_players
from PIL import Image
import requests
from io import BytesIO


#Setting up Window-screen
app = customtkinter.CTk()
app.geometry("600x780")
app.title("Player Builder")


def enter_btn():
    name = player_entry.get()
    results = get_players(name)
    for player in results:
        response = requests.get(player["photo"])
        img = Image.open(BytesIO(response.content))
        img = img.resize((50, 50))
        photo = customtkinter.CTkImage(img)
    
        # Show image + name together
        label = customtkinter.CTkLabel(app, text=player["name"], image=photo, compound="left")
        label.pack()



player_entry = customtkinter.CTkEntry(app, placeholder_text="Enter Player: ")
player_entry.pack()


player_enter_btn = customtkinter.CTkButton(app, text="Search", command=enter_btn)
player_enter_btn.pack()

#Running the app
app.mainloop()