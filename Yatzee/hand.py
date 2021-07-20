from die import Die


class Hand:
    def __init__(self, size=5) -> None:
        if size > 0:
            self.hand_size = size
        else:
            raise IndexError("Can't have negative handsize")

        self.hand = []
        for _ in range(1, size+1):
            self.hand.append(Die(6))

    def roll_hand(self):
        for die in self.hand:
            die.roll()
