import random
import time
import textwrap
from hero import Character
from story import print_choices
from items import Weapon, Armour, Potion, wooden_chest_loot, silver_chest_loot, golden_chest_loot

wooden_chest_sprite = r"""
                         _                 _
                  .-----|-|-=============-|-|-----.
                  |=====|.|======____======|.|=====|
                  |____|_|_____.._()_.._____|_|____|
                  /    |.|   <_.. /\ .._>   |.|    \
                  \___|___|_____\____/_____|___|___/
                   |===\:/==================\:/===|
                   |   |=|                  |=|   |
                   |===|.|==================|.|===|
                   |   |.|                  |.|   |
                   |===|.|==================|.|===|
                   `---|_|------------------|_|---'
"""

silver_chest_sprite = r"""
                 .---------------------------------.
                / /  /   / / <>'.---.'<> \ \   \  \ \
               /.| .'`' |.|     |   |     |.|`' `. |.\
               | |`'  ..| |.--. '^^^' .--.| |..  `'| |
               \_\__'_`.|_|_''_`.<o>.`_''_|_|.`_'__/_/
                | |==========.---------.==========| |
                |.|==========| ()   () |==========|.|
                | |. /  --_ /| /\   /\ |\ _--  \ .| |
                |.|.' .' - \|.'-------'.|/ - '. '.| |
                |.|    .-  .|.| ,.|., |.|.  -.    |.|
                \ \     `-.'|.| .'|'. |.|`.-'     / /
                 `----------|_|-------|_|----------`
"""

golden_chest_sprite = r"""
                      ____...---=====---...____
                 _.-"` /o/                  \o\ `"-._      +.
               .' /   |.|       _./\._       |.|   \ '.   .  + .
               |o|   |o|      .' .''. `. .    |o|   |o|    .+
               | |  |.|       | |    | |  +.   |.|  | |      .
               /o/ _/o\_      . .____. . .    _/o\_ \o\
               \_\_\___/_______'------'_______\___/_/_/
                ||  \8/         ------         \8/  ||
        + .     ||  |.|       .'()()()'.       |.|  ||
      .  +      ||  |o|   .   './\/\/\.'       |o|  ||  +.
                ||  |.|    +.  '------'        |.|  || .
                ||  |o|   .                    |o|  ||
                ||-_|.|________________________|.|_-||
                ``--|_|------------------------|_|--''
"""

class Chest:
	def __init__(self, name: str, sprite: str, locks: int, loot: list):
		self.name = name
		self.sprite = sprite
		self.locks = locks
		self.loot = loot

	def unlock(self, character: Character) -> bool:
		if character.lockpicks < self.locks:
			print("You don't have enough lockpicks...\n")
			time.sleep(2)
			return False

		character.lockpicks -= self.locks
		print("You successfully opened the chest and received...\n")
		num_items = random.choices(
		[1, 2, 3], weights=[0.7, 0.2 + self.locks / 10, 0.1 + self.locks / 10],
		)[0]

		for num in range(num_items):
			item = random.choice(self.loot, weights=[0.45, 0.35, 0.15, 0.05, 0.3, 0.35, 0.2, 0.15, 0.7, 0.3])[0]
			print(item)
			time.sleep(0.5)

			if isinstance(item, Weapon):
				character.inventory["weapons"].append(item)

			if isinstance(item, Armour):
				character.inventory["armour"].append(item)

			if isinstance(item, Potion):
				exists = 0
				for idx, potion in enumerate(character.inventory["health potions"]):
					if item.name == potion.name:
						potion.num += 1
						exists = 1
						break

				if not exists:
					character.inventory["healt potions"].append(item)

		gold = Gold()
		character.gold += gold
		print(f"{gold} gold\n")
		time.sleep(0.5)
		return True

class Gold:
	def __init__(self):
		self.amount = random.choice(range(10, 50, 1))

wooden_chest = Chest("Wooden chest", wooden_chest_sprite, 1, wooden_chest_loot)
silver_chest = Chest("Silver chest", silver_chest_sprite, 2, silver_chest_loot)
golden_chest = Chest("Golden chest", golden_chest_sprite, 3, golden_chest_loot)

def treasure(character: Character):
	print(textwrap.fill("The room is filled with chests and crates of different sizes and colours.", 70) + "\n")
	time.sleep(3)

	print(textwrap.fill("Three chests stand out, aligned next to eachother near the center of the room.", 70) + "\n")
	time.sleep(2)

	print(wooden_chest_sprite)
	print(textwrap.fill("The chest on the left is made of wood and quite a bit smaller than the rest. There is one lock on it.", 70) + "\n")
	time.sleep(7)

	print(silver_chest_sprite)
	print(textwrap.fill("The chest in the middle is made of silver, emitting a soft, twinkling light. There are two locks on it.", 70) + "\n")
	time.sleep(7)

	print(golden_chest_sprite)
	print(textwrap.fill("The chest on the right is the biggest of the three, its gold exterior burning to the touch. There are three locks on it.", 70) + "\n")
	time.sleep(7)

	print("You see a sign:\n")
	time.sleep(1)

	print("'You must choose at most one chest out of the three.'\n")
	time.sleep(2)

	while True:
		print("What will you do?")
		choices = ["Wooden chest", "Silver chest", "Gold chest", "Check lockpicks", "Leave"]
		print_choices(choices)

		choice = input()

		success = 0
		if choice.lower() == "wooden chest":
			success = wooden_chest.unlock(character)

		if choice.lower() == "silver chest":
			success = silver_chest.unlock(character)

		if choice.lower() == "golden chest":
			success = golden_chest.unlock(character)

		if choice.lower() == "leave":
			break

		if success:
			break
