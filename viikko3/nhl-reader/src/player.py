class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists

    def __str__(self):
        return f'{self.name} {self.team} {self.goals} + {self.assists} = {self.goals + self.assists}'

    def __lt__(self, other):
        return self.assists+self.goals < other.assists+other.goals
