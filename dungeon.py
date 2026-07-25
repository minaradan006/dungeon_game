import random
import time
import textwrap
from hero import Character
from items import Weapon, Armour, Potion
from rooms import Room
from story import show_start_screen, begin_story
from scenarios  import scenario_1, scenario_2, scenario_3
from monsters import enemy
from treasure_room import treasure

def enter_room(room: Room, character: Character, level: int):
	print("-" * 70 + "\n")
	time.sleep(1)

	print(f"You enter the {room.desc} and look around." + "\n")
	time.sleep(3)

	print(textwrap.fill(room.entry, 70) + "\n")
	time.sleep(8)

	print(textwrap.fill(room.adj, 70) + "\n")
	time.sleep(5)

	if room.event == "enemy":
		if not enemy(character, level, room.monster):
			print(textwrap.fill("You open your eyes and see the faint sunlight streaming through the tree leaves.", 70) + "\n")
			time.sleep(3)

			print(textwrap.fill("The dungeon entrace is open, ready for you to try again.\n", 70) + "\n")
			time.sleep(3)

			return

	if room.event == "treasure":
		treasure(character, level)

	print(textwrap.fill(room.exit, 70) + "\n")
	time.sleep(5)

	print("You decide to leave the room.\n")
	time.sleep(3)

	print("-" * 70 + "\n")
	time.sleep(1)

if __name__ == "__main__":
	show_start_screen()

	name, attack, defense = begin_story()
	character = Character(name, attack, defense)

	character.inventory["weapons"].append(Weapon("Longsword", 5, "Heavy and slow, but sturdy."))
	armour = Armour("Copper Helmet", 3, "A few scratches can be seen reflected in the light.")
	weapon = Weapon("Silver Dagger", 2, "Small but very agile.")
	potion = Potion("Small Potion", 10, "Can be used to heal a small amount of health")
	character.inventory["weapons"].append(weapon)
	character.inventory["armour"].append(armour)
	character.inventory["health potions"].append(potion)


	for level in range(1, 5):
		print("=" * 70)
		print(f"LEVEL {level}".center(70))
		print("=" * 70 + "\n")
		time.sleep(1)

		mini_stages = random.choice(range(1, 2))

		for mini in range(0, mini_stages):
			scenario = random.choice([1, 2, 3])

			room = None
			if scenario == 1:
				room = scenario_1(character, level)
			elif scenario == 2:
				room =  scenario_2(character, level)
			elif scenario == 3:
				room = scenario_3(character, level)

			enter_room(room, character, level)

	print("You did it!")
