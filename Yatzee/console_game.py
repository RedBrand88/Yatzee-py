from score import Score

class Console_Game:
    def __init__(self, score):
        self.score_sheet = f"------------\n      |score\n------------\nAces  |{score.aces}\nTwos  |{score.twos}\nThrees|{score.threes}\nFours |{score.fours}\nFives |{score.fives}\nSixes |{score.sixes}\n------------------\n            |score\n------------------\n3 of a kind |{score.th_of_a_kind}\n4 of a kind |{score.fo_of_a_kind}\nFull House  |{score.full_house}\nSm. Straight|{score.sm_straight}\nLg. Straight|{score.lg_straight}\nYATZEE      |{score.yatzee}\nChance      |{score.chance}\n------------------"
        self.greeting = ""

    def draw(self):
        print(self.score_sheet)