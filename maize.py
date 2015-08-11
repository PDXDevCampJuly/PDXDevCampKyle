# Corny maze.

def main():
    print("""
    You awaken in a dank, cavernous brick room.
    """)
    process_user_movement()


def get_choice(doors):
    choice = ""
    while not choice:
        choice = input("Where would you like to go? >> ").capitalize()
        if choice.lower() == "exit":
            exit()
        elif choice not in doors:
            print("I don't follow.  Please give me a direction (e.g. 'East').")
            choice = ""
    return doors[choice]


def process_user_movement():
    inventory = {"North": "", "South": "", "East": "", "West": ""}
    inventory, choice = room0(inventory)
    while True:
        inventory, choice = choice(inventory)


def room0(inventory):
    doors = {"North": room3, "South": room4, "East": room1, "West": room2}
    print(
    """
    A thick layer of moss covers the deteriorated walls.
    The air is thick and heavy; you struggle to catch your
    breath in the dank environment.

    - A door lies to your west.
    - A second door to the north has an unlit torch beside it.
    - A faint glow eminates from a doorway to the east; the remains
      of the shattered door swing freely on their hinges.
    - Through a large hole in the southern wall, an ominous rumble
      gives you pause.
    """)
    return inventory, get_choice(doors)


def room1(inventory):
    doors = {"West": room0}
    if not inventory["West"]:
        print(
        """
    As you step through the portal no longer covered by the shattered
    door, you see that the glow is coming from an odd green flame atop
    a stone pedestal.  Approaching the source, you notice that there
    seems to BE no source; the flame burns without fuel.  You continue to
    approach carefully until the flame suddenly leaps from its perch,
    swirls playfully around you, then rests just in front of the palm
    you've defensively pushed outward.  You notice that as you move
    your hand, the cool flame moves with it as though it is at your command.
    You hope this condition resolves itself before your next high five.

    - The shattered door is behind you to the West.
        """)
        inventory["West"] = "flame"
    else:
        print(
        """
    Your firey friend seems calmer in its old home.  You, however, see
    no reason to be here.

    - The shattered door is behind you to the West.
        """)
    return inventory, get_choice(doors)


def room2(inventory):
    pass


def room3(inventory):
    pass


def room4(inventory):
    pass



if __name__ == '__main__':
    main()
