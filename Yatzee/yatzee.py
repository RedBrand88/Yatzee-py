from score import Score

class YatzeeGame:
    def __init__(self) -> None:
        self.rules = []

    def register_rules(self, rules: List):
        self.rules.extend(rules)

    def get_rule(self, selection: int):
        return self.rules[selection]

    def take_turn(self):
        pass

    def set_points(self, score: Score):
        pass

    def play(self):
        pass
