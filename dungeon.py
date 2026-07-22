import random
import time
import textwrap
from obj import Weapon, Armour, Potion, Character, Room
from items import walls
from story import show_start_screen, begin_story

def print_choices(valid_choices):
	for choice in valid_choices:
		print(f"[{choice}]", end="  ")
		time.sleep(0.5)
	print()

def inventory(character: Character):
	print("INVENTORY".center(40, "=") + "\n")

	for category, content in character.inventory.items():
		print(f"{category.title()}".center(20, "-") + "\n")

		for item in content:
			print(item)

		print()
		time.sleep(0.5)

	while(True):
		print("What do you want to do?")
		time.sleep(0.5)
		choices = ["Equip Weapon", "Equip Armour", "Heal", "Go back"]
		print_choices(choices)

		choice = input()
		print()

		if choice.lower() == "equip weapon":
			weapon_name = input("What weapon do you want to equip? ")
			print()
			character.equip_weapon(weapon_name)

		if choice.lower() == "equip armour":
			armour_name = input("What armour do you want to equip? ")
			print()
			character.equip_armour(armour_name)

		if choice.lower() == "heal":
			potion_name = input("What potion do you want to use? ")
			print()
			character.heal(potion_name)

		if choice.lower() == "go back":
			break

	print("Closing inventory..." + "\n")

def scenario_1(character: Character, level: int):
	print(textwrap.fill(f"A wall of {random.choice(walls)} blocks your sides. You can only go [ahead].", width=60) + "\n")
	time.sleep(3)

	ahead = Room(level)
	print(textwrap.fill(f"Ahead, there is {ahead.desc}({ahead.event}).", width=70) + "\n")
	time.sleep(3)

	choices = ["Go ahead", "Check stats", "Open inventory"]

	while True:
		print("What will you do?")
		time.sleep(0.5)
		print_choices(choices)
		choice = input()
		print()

		if choice.lower() == "check stats":
			print("STATS".center(40, "=") + "\n")
			print(character)

		if choice.lower() == "open inventory":
			inventory(character)

		if choice.lower() == "go ahead":
			return ahead

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
			scenario = random.choice(range(1, 2))

			if scenario == 1:
				choice = scenario_1(character, level)
			elif scenario == 2:
				pass

	print("You did it!")
