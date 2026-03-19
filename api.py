import requests

def get_sport():
    url = f"https://www.thesportsdb.com/api/v2/json"
    response = requests.get(url)
    data = response.json()
    team = data["teams"][0]
    print(team)





def get_players(player_name):
    url = f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={player_name}"
    response = requests.get(url)
    data = response.json()
    players = data["player"]
    all_players = []
    for player in players:
        all_players.append({
        "name": player["strPlayer"],
        "photo": player["strThumb"],
        "team": player["strTeam"],
        "position": player["strPosition"]})
    return all_players


def get_teams(sport_name):
    url = f"https://www.thesportsdb.com/api/v1/json/123/search_all_teams.php?l={sport_name}"
    response = requests.get(url)
    data = response.json()
    teams = data["teams"]
    all_teams = []
    for team in teams:
        all_teams.append(team["strTeam"])
    return all_teams
















# def get_all_sports():
#     url = "https://www.thesportsdb.com/api/v1/json/123/all_sports.php"
#     response = requests.get(url)
#     data = response.json()
    
#     sports_list = []
#     for sport in data["sports"]:
#         sports_list.append(sport["strSport"])
    
#     return sports_list


