from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, stat):
        self.stat = stat

    PlayerReader.players.sort(reverse=True)

    def top_scorers_by_nationality(self, nationality):
        for player in PlayerReader.players:
            if player.nationality == nationality:
                print(player)
