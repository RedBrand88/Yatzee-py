from abc import ABC, abstractmethod
from hand import Hand


class Rule(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def points(self, hand: Hand):
        pass


class AddSameValue(Rule):
    def __init__(self, value: int, name: str) -> None:
        self.__value = value
        self.__name = name

    def name(self):
        return self.__name

    def points(self, hand):
        return hand.count(self.__value) * self.__value


class Aces(AddSameValue):
    def __init__(self) -> None:
        super().__init__(1, "Aces")


class Twos(AddSameValue):
    def __init__(self) -> None:
        super().__init__(2, "Twos")


class Threes(AddSameValue):
    def __init__(self) -> None:
        super().__init__(3, "Threes")


class Fours(AddSameValue):
    def __init__(self) -> None:
        super().__init__(4, "Fours")


class Fives(AddSameValue):
    def __init__(self) -> None:
        super().__init__(5, "Fives")


class Sixes(AddSameValue):
    def __init__(self) -> None:
        super().__init__(6, "Sixes")


class Rounds_13(Rule):
    pass


class Rerolls_3(Rule):
    pass


class Bonus_35(Rule):
    # if upper score >= 63 add 35 to grand score
    def name(self):
        return "Bonus 35"

    def points(self, hand):
        pass


class ThreeOfAKind(Rule):
    # if there are 3 dice with the same face sum the faces
    def name(self):
        return "Three of a Kind"

    def points(self, hand: Hand):
        for i in range(6):
            if hand.count(i) >= 3:
                return hand.sum()
        return 0


class FourOfAKind(Rule):
    # if there are 4 dice with the same face sum the faces
    def name(self):
        return "Four of a Kind"

    def points(self, hand: Hand):
        for i in range(6):
            if hand.count(i + 1) >= 4:
                return hand.sum()
        return 0


class Straight(Rule):

    def is_straight(self, hand_list):
        if len(list(set(hand_list))) != len(hand_list):
            return False
        consecutive_sum = (min(hand_list) + max(hand_list)) * \
            (max(hand_list) - min(hand_list) + 1) / 2
        return sum(hand_list) == consecutive_sum


class SmStraight(Straight):
    # if there are 4 consecutive dice add 30
    def name(self):
        return "Small Straight"

    def points(self, hand: Hand):
        sorted_hand = sorted(hand.get_hand())
        if len(sorted_hand) == 4 and self.is_straight(sorted_hand):
            return 30
        elif len(sorted_hand) == 5 and (self.is_straight(sorted_hand[1:]) or self.is_straight(sorted_hand[:-1])):
            return 30
        else:
            return 0

    def getIsStraight(self, hand: Hand):
        return self.is_straight(hand.get_hand())


class LgStraight(Straight):
    # if there are 5 consecutive dice add 40
    def name(self):
        return "Large Straight"

    def points(self, hand: Hand):
        if self.is_straight(hand.get_hand()):
            return 40
        else:
            return 0


class FullHouse(Rule):
    # if there is a pair and 3 of a kind add 25
    def name(self):
        return "FullHouse"

    def points(self, hand: Hand):
        counts = [hand.count(i + 1) for i in range(6)]
        if 2 in counts and 3 in counts:
            return 25
        else:
            return 0


class Yatzee(Rule):
    # five of a kind add 50
    def name(self):
        return "Yatzee"

    def points(self, hand: Hand):
        if len(set(hand.hand)) == 1:
            return 50
        else:
            return 0


class Chance(Rule):
    # sum hand
    def name(self):
        return "Chance"

    def points(self, hand: Hand):
        return hand.sum()