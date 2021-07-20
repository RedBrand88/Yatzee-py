class Score:
    def __init__(self) -> None:
        self.aces = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0
        self.th_of_a_kind = 0
        self.fo_of_a_kind = 0
        self.full_house = 0
        self.sm_straight = 0
        self.lg_straight = 0
        self.yatzee = 0
        self.chance = 0

    def top_total(self):
        return self.aces + self.twos + self.threes + self.fours + self.fives + self.sixes

    def bottom_total(self):
        return self.th_of_a_kind + self.fo_of_a_kind + self.full_house + self.sm_straight + self.lg_straight + self.yatzee + self.chance

    def grand_total(self):
        return self.top_total() + self.bottom_total()