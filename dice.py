"""A generic Die class that can be imported into any dice-rolling game."""

from random import choice


class Die:
    """
    Creates a Die object with arbitrary faces and a roll method.

    Arguments:
    faces = a list of objects that represent each face
            (e.g., [1,2,3,4,5,6])
    value = an item in faces that the object is currently 'showing'
    held = whether or not the die's value is locked
    """

    def __init__(self, faces):
        self.faces = faces
        self.value = faces[0]
        self.held = False

    def __repr__(self):
        return str(self.value)

    def roll(self):
        """
        Rolls the Die to get a new value from faces, and returns
        for printing purposes."""
        self.value = choice(self.faces)
        return self.value
