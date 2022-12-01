class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0
        self.tied = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All"
        }

        self.update_points = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def tie(self):
        if self.score1 in self.tied:
            return self.tied[self.score1]
        else:
            return "Deuce"

    def get_score(self):
        if self.score1 == self.score2:
            return self.tie()
        elif self.score1 >= 4 or self.score2 >= 4:
            return self.more_than_four()
        else:
            return self.score_under_four()

    def more_than_four(self):
        minus_result = self.score1 - self. score2
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def score_under_four(self):
        return self.update(self.score1) + "-" + self.update(self.score2)

    def update(self, new):
        return self.update_points[new]
