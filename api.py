import requests

def get_sport():
    url = f"https://www.thesportsdb.com/api/v2/json"
    response = requests.get(url)
    data = response.json()
    team = data["teams"][0]
    print(team)





def get_players(sport_name):
    url = f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?s={sport_name}"
    response = requests.get(url)
    data = response.json()
    players = data["player"]
    for player in players:
        print(player["strPlayer"])


# def get_all_sports():
#     url = "https://www.thesportsdb.com/api/v1/json/123/all_sports.php"
#     response = requests.get(url)
#     data = response.json()
    
#     sports_list = []
#     for sport in data["sports"]:
#         sports_list.append(sport["strSport"])
    
#     return sports_list


