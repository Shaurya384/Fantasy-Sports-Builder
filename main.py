# Imports
import customtkinter
from tkinter import messagebox
from api import get_teams
import subprocess
import sys


# Setting up Window-screen
app = customtkinter.CTk()
app.geometry("600x780")
app.title("Fantasy-App-Sports")


# Variables
valid_sports = ["Soccer", "Ice Hockey", "Basketball", "Tennis", "Baseball", "Rugby"]
chosen_sport = None

# Title Code
app_title = customtkinter.CTkLabel(app, text="FANTASY SPORTS BUILDER", fg_color="transparent", text_color="white")
app_title.pack()

pick_Sport = customtkinter.CTkLabel(app, text="Pick a Sport: ")
pick_Sport.pack()

# Choose sport
get_input = customtkinter.CTkEntry(app, placeholder_text="Enter Sport")
get_input.pack()

# Function for enter button
def enter_button():
    sport = get_input.get().strip()
    if not sport:
        messagebox.showerror("Error", "Please enter a sport.")
        return
    if sport in valid_sports:
        global chosen_sport
        chosen_sport = sport 
        messagebox.showinfo("Success", f"Chosen Sport is {sport}")
        app.destroy()
        subprocess.Popen([sys.executable, "team_builder.py"])
    else:
        messagebox.showerror("Error", f"'{sport}' is not a valid sport. Valid sports: {', '.join(valid_sports)}")

enter_btn = customtkinter.CTkButton(app, text="Enter", command=enter_button)
enter_btn.pack()

# Running the app
app.mainloop()
