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

    def count(self, target: int):
        return self.get_hand().count(target)

    def get_hand(self):
        return [die.get_face() for die in self.hand]

    def sum(self):
        return sum(self.get_hand())
