#!/usr/bin/env python3

"""A small command-line choose-your-own-adventure game."""

from typing import Dict, List, Optional, Tuple


def say(text: str) -> None:
    print(f"\n{text}")


def choose(prompt: str, options: List[Tuple[str, str]]) -> str:
    print(f"\n{prompt}")
    for key, description in options:
        print(f"  {key}) {description}")

    valid = {key for key, _ in options}
    while True:
        answer = input("\n> ").strip().lower()
        if answer in valid:
            return answer
        print(f"Please choose one of: {', '.join(sorted(valid))}")


def add_item(inventory: List[str], item: str) -> None:
    if item not in inventory:
        inventory.append(item)
        say(f"You found: {item}.")


def has_item(inventory: List[str], item: str) -> bool:
    return item in inventory


def show_inventory(inventory: List[str]) -> None:
    if inventory:
        print(f"\nInventory: {', '.join(inventory)}")
    else:
        print("\nInventory: empty")


def ending(title: str, text: str, inventory: List[str]) -> None:
    say(f"=== {title} ===")
    say(text)
    show_inventory(inventory)
    print("\nThanks for playing!")


def main() -> None:
    inventory: List[str] = []

    say("THE LANTERN OF MOONFALL")
    say(
        "You are a courier in the village of Bramblewick. "
        "At midnight, the ancient Moonfall Bell rings once, then goes silent. "
        "Legend says the bell protects the valley from the Hollow King."
    )
    say(
        "Tonight, the bell has stopped ringing. A silver light flickers "
        "from the ruins beyond the forest."
    )

    # Scene 1
    choice = choose(
        "You stand at the edge of the village. What do you do?",
        [
            ("a", "Visit the old watchtower."),
            ("b", "Take the forest path toward the ruins."),
            ("c", "Search the abandoned blacksmith's shop."),
        ],
    )

    if choice == "a":
        say(
            "At the watchtower, the retired guard Mara gives you a brass key "
            "and warns you not to trust anything that speaks from the shadows."
        )
        add_item(inventory, "brass key")
    elif choice == "b":
        say(
            "You follow the forest path and discover a torn traveler's cloak "
            "caught on a thorn bush."
        )
        add_item(inventory, "red thread")
    else:
        say(
            "Inside the blacksmith's shop, you find a sturdy iron lantern. "
            "It has no oil, but its glass is unbroken."
        )
        add_item(inventory, "iron lantern")

    show_inventory(inventory)

    # Scene 2
    choice = choose(
        "The path divides beneath a huge oak tree.",
        [
            ("a", "Follow a trail of blue mushrooms."),
            ("b", "Climb the oak to scout the area."),
            ("c", "Light a small fire and wait for dawn."),
        ],
    )

    if choice == "a":
        say(
            "The mushrooms lead you to a hollow log. Inside is a sealed "
            "glass vial filled with glowing blue oil."
        )
        add_item(inventory, "blue oil")
    elif choice == "b":
        say(
            "From the branches, you spot a stone bridge, a ruined chapel, "
            "and a black tower rising beyond them."
        )
        add_item(inventory, "map scrap")
    else:
        say(
            "The fire attracts a nervous fox. It drops a smooth white stone "
            "at your feet before disappearing into the dark."
        )
        add_item(inventory, "moonstone")

    # Scene 3
    choice = choose(
        "A whisper comes from the darkness: 'Courier, carry this message.'",
        [
            ("a", "Answer the whisper."),
            ("b", "Ignore it and cross the stone bridge."),
            ("c", "Hide and watch for movement."),
        ],
    )

    if choice == "a":
        say(
            "A shadowy figure gives you a parchment sealed with black wax. "
            "It promises safe passage if you deliver it to the tower."
        )
        add_item(inventory, "sealed parchment")
    elif choice == "b":
        say(
            "You cross the bridge. Halfway over, a spectral wolf blocks your "
            "path, its eyes fixed on your hands."
        )
    else:
        say(
            "You wait. A spectral wolf appears, then fades when it sees the "
            "moonstone in your possession."
        )
        if has_item(inventory, "moonstone"):
            say("The wolf leaves behind a silver fang.")
            add_item(inventory, "silver fang")

    # Scene 4
    choice = choose(
        "You reach the ruined chapel. Its doors are locked.",
        [
            ("a", "Use the brass key, if you have it."),
            ("b", "Search around the chapel."),
            ("c", "Force the doors open."),
        ],
    )

    if choice == "a" and has_item(inventory, "brass key"):
        say(
            "The key turns smoothly. Inside, you find an altar and a bronze "
            "bell clapper wrapped in velvet."
        )
        add_item(inventory, "bronze clapper")
    elif choice == "a":
        say("You have no key, so you search the walls instead.")
        add_item(inventory, "chalk symbol")
    elif choice == "b":
        say(
            "Behind the chapel, you find a hidden stairway descending beneath "
            "the earth."
        )
        add_item(inventory, "stone token")
    else:
        say(
            "The doors burst open, but the noise awakens a swarm of paper "
            "ravens. They scatter your belongings before flying away."
        )
        if inventory:
            lost_item = inventory.pop(0)
            say(f"You lose your {lost_item}.")
        else:
            say("You had nothing to lose, which is fortunate.")

    # Scene 5
    choice = choose(
        "Beneath the chapel, you find three tunnels.",
        [
            ("a", "Take the tunnel marked with a bell."),
            ("b", "Take the tunnel marked with a crown."),
            ("c", "Take the tunnel marked with an eye."),
        ],
    )

    if choice == "a":
        say(
            "The bell tunnel leads to a cavern filled with floating candles. "
            "One candle burns with blue flame."
        )
        add_item(inventory, "blue flame")
    elif choice == "b":
        say(
            "The crown tunnel leads to a throne carved from salt. A voice "
            "offers you power in exchange for your name."
        )
        choice = choose(
            "How do you respond?",
            [
                ("a", "Give the voice a false name."),
                ("b", "Refuse and leave."),
            ],
        )
        if choice == "a":
            say("The throne cracks. A black crown tumbles to the floor.")
            add_item(inventory, "black crown")
        else:
            say("The voice laughs, but the tunnel remains open.")
    else:
        say(
            "The eye tunnel leads to a round chamber. A crystal eye watches "
            "you from a pedestal."
        )
        add_item(inventory, "crystal eye")

    # Scene 6
    choice = choose(
        "The tunnels end at a sealed iron gate.",
        [
            ("a", "Try to open the gate."),
            ("b", "Place an item into the gate's empty slot."),
            ("c", "Knock three times."),
        ],
    )

    if choice == "a":
        if has_item(inventory, "brass key"):
            say("The brass key opens the gate with a deep metallic groan.")
        else:
            say(
                "You pull at the gate until your hands ache. It does not move."
            )
    elif choice == "b":
        if has_item(inventory, "stone token"):
            say(
                "The stone token fits perfectly. The gate opens, revealing "
                "a stairway to the black tower."
            )
            inventory.remove("stone token")
        elif has_item(inventory, "crystal eye"):
            say(
                "The crystal eye fits the slot, but the gate opens only halfway. "
                "You squeeze through."
            )
            inventory.remove("crystal eye")
        else:
            say("None of your items fit the slot.")
    else:
        say(
            "You knock three times. Something knocks back from the other side. "
            "Then the gate opens by itself."
        )

    # Scene 7
    choice = choose(
        "At the tower entrance, a guardian made of smoke blocks the stairs.",
        [
            ("a", "Show the guardian the sealed parchment."),
            ("b", "Offer the guardian the silver fang."),
            ("c", "Challenge the guardian."),
        ],
    )

    if choice == "a" and has_item(inventory, "sealed parchment"):
        say(
            "The guardian reads the parchment and steps aside. "
            "The black wax melts away."
        )
    elif choice == "b" and has_item(inventory, "silver fang"):
        say(
            "The guardian recognizes the fang as a token of the forest wolf "
            "and lets you pass."
        )
    elif choice == "c":
        say(
            "You raise your fists. The guardian dissolves into smoke, leaving "
            "a cold mark on your palm."
        )
        add_item(inventory, "smoke mark")
    else:
        say(
            "The guardian does not understand your words, but it is distracted "
            "by a distant bell. You slip past."
        )

    # Scene 8
    choice = choose(
        "At the top of the tower, you find the Moonfall Bell cracked in two.",
        [
            ("a", "Repair it with the bronze clapper."),
            ("b", "Pour blue oil into its crack."),
            ("c", "Place the moonstone inside it."),
        ],
    )

    if choice == "a" and has_item(inventory, "bronze clapper"):
        ending(
            "ENDING: THE BELL RINGS AGAIN",
            "The bronze clapper touches the cracked bell. Golden light floods "
            "the valley, and the Hollow King is sealed away for another century. "
            "By sunrise, villagers call you the Bellkeeper.",
            inventory,
        )
    elif choice == "b" and has_item(inventory, "blue oil"):
        ending(
            "ENDING: THE SILVER DAWN",
            "The blue oil flows through the crack and transforms the bell into "
            "a silver moon. Its light protects the valley, but the old bell "
            "will never ring again. You become the guardian of the tower.",
            inventory,
        )
    elif choice == "c" and has_item(inventory, "moonstone"):
        ending(
            "ENDING: THE HOLLOW KING AWAKENS",
            "The moonstone fits the bell perfectly. Instead of healing the crack, "
            "it opens a doorway beneath the tower. A crowned shadow reaches "
            "through, and the valley falls silent.",
            inventory,
        )
    else:
        ending(
            "ENDING: A BRAVE FAILURE",
            "You cannot repair the bell, but you strike it with all your strength. "
            "The sound is weak and broken, yet enough to wake the villagers. "
            "Together, they light every lantern in the valley and drive the "
            "Hollow King back into the dark.",
            inventory,
        )


if __name__ == "__main__":
    main()
