import requests

name = input("Search up team: ")

def get_team(team_name):
    url = f"https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={team_name}"
    respone = requests.get(url)
    data = respone.json()
    team = data["teams"][0]
    print(team)




# NHL = customtkinter.CTkLabel(app, text="NHL")
# NHL.pack()
# NHL = customtkinter.CTkLabel(app, text="NBA")
# NHL.pack()
# NHL = customtkinter.CTkLabel(app, text="Cricket")
# NHL.pack()
# NHL = customtkinter.CTkLabel(app, text="Soccer")
# NHL.pack()
# NHL = customtkinter.CTkLabel(app, text="American-Football")
# NHL.pack()
get_team(name)