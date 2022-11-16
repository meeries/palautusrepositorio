from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.url = url
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"

    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['assists'],
            player_dict['goals']
        )
        players.append(player)
