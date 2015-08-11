from dice import Die

class Angry_dice:
    """
    Class that controls the flow of an Angry Dice player.

    Arguments:
    stage = Whetherhich stage the player is currently in.
    die_a = The first Die object.
    die_b = The second Die object.
    cheating = Whether or not the player held a 6 (bool).
    """

    def __init__(self):
        self.stage = 1
        self.die_a = Die(["1", "2", "ANGRY", "4", "5", "6"])
        self.die_b = Die(["1", "2", "ANGRY", "4", "5", "6"])
        self.cheating = False

    def play(self):
        """Controls the actual flow of the game."""
        done = False
        while not done:
            print("""
Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!
Stage 1 you need to roll 1 & 2
Stage 2 you need to roll ANGRY & 4
Stage 3 you need to roll 5 & 6
You can lock a die needed for your current stage
and just roll the other one, but beware!
If you ever get 2 ANGRY's at once, you have to restart to Stage 1!
Also, you can never lock a 6!  That's cheating!

To rol the dice, simply input the name of the die you want to roll.
Their names are a and b.

Press ENTER to start!
            """)
            input("")
            self.cheating = self.roll_parse("ab")
            while not done:
                self.print_hand()
                decision = input("Roll dice: ")
                self.cheating = self.roll_parse(decision)
                done = self.advance_check()
            self.print_hand()
            print("You've won!  Calm down!")

    def roll_parse(self, string):
        """
        Takes an input string and rolls the appropriate dice.  Returns
        whether or not the player was cheating with that roll (bool).

        Arguments:
        string = an input string from the user.
        VALUES = values you're allowed to hold in each stage.
        """
        VALUES = [["1", "2"], ["ANGRY", "4"], ["5"]]
        cheating = False
        if "a" not in string:
            self.die_a.held = True
            if self.die_a.value not in VALUES[self.stage - 1]:
                cheating = True
        else:
            self.die_a.held = False
        if "b" not in string:
            self.die_b.held = True
            if self.die_b.value not in VALUES[self.stage - 1]:
                cheating = True
        else:
            self.die_b.held = False
        if not self.die_a.held:
            self.die_a.roll()
        if not self.die_b.held:
            self.die_b.roll()
        return cheating

    def print_hand(self):
        """
        Prints to dice currently held, and whether or not the
        player has cheated.

        Arguments: none
        """
        if self.cheating:
            print("You're cheating!")
            print("until you reroll it!")
        print("""
You rolled:
a = [  {}  ]
b = [  {}  ]

You are in Stage {}
        """.format(self.die_a, self.die_b, self.stage))

    def advance_check(self):
        """Checks conditions of each stage."""
        values = [self.die_a.value, self.die_b.value]
        if self.stage == 3:
            if not self.cheating and "5" in values and "6" in values:
                return True
            return False
        if self.stage == 2 and "ANGRY" in values and "4" in values:
            self.stage = 3
        if self.stage == 1 and "1" in values and "2" in values:
            self.stage = 2
        if self.die_a.value == self.die_b.value == "ANGRY":
            print("WOW, you're ANGRY!")
            self.stage = 1
        return False

if __name__ == '__main__':
    game = Angry_dice()
    game.play()
