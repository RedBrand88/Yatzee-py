import random


class Die:

    def __init__(self, sides=6, face=None):
        if face is not None and face > sides:
            raise IndexError("die face is greater than die sides")
        else:
            self.face = face

        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def getFace(self):
        return self.face
