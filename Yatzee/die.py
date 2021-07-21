import random


class Die:

    def __init__(self, sides=6, face=None):
        if face is not None and face > sides:
            raise IndexError("die face is greater than die sides")
        else:
            self.face = face

        self.sides = sides

    def __str__(self) -> str:
        if self.face is not None:
            return str(self.face)

    def roll(self):
        self.face = random.randint(1, self.sides)

    def get_face(self):
        return self.face
