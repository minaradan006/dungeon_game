import time
import textwrap
import random
from obj import Character, Room
from items import walls, room_adjectives

def print_choices(valid_choices):
	for choice in valid_choices:
		print(f"[{choice}]", end="  ")
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
	print(textwrap.fill(f"Walls of {random.choice(walls)} block your sides. You can only go [ahead].", width=70) + "\n")
	time.sleep(3)

	ahead = Room(level)
	print(textwrap.fill(f"Ahead, there is a {ahead.desc}({ahead.event}).", width=70) + "\n")
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
			print(f"You decide to go straight.\n")
			time.sleep(3)
			return ahead

def scenario_2(character: Character, level: int):
	print(textwrap.fill(f"A wall of {random.choice(walls)} blocks your path. You can only go [left] or [right].", width=70) + "\n")
	time.sleep(3)

	left = Room(level)
	print(textwrap.fill(f"To the left, there is a {left.desc}({left.event}).", width=70) + "\n")
	time.sleep(3)

	right = Room(level)
	print(textwrap.fill(f"To the right, there is a {right.desc}({right.event}).", width=70) + "\n")
	time.sleep(3)

	choices = ["Go left", "Go right", "Check stats", "Open inventory"]

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
	
		if choice.lower() == "go left":
			print(f"You decide to go to the left.\n")
			time.sleep(3)
			return left

		if choice.lower() == "go right":
			print(f"You decide to go to the right.\n")
			time.sleep(3)
			return right

def scenario_3(character: Character, level: int):
	print(textwrap.fill(f"You stand at a crossroad. You can go [left], [right] or [ahead].", width=70) + "\n")
	time.sleep(3)

	left = Room(level)
	print(textwrap.fill(f"To the left, there is a {left.desc}({left.event}).", width=70) + "\n")
	time.sleep(3)

	right = Room(level)
	print(textwrap.fill(f"To the right, there is a {right.desc}({right.event}).", width=70) + "\n")
	time.sleep(3)

	ahead = Room(level)
	print(textwrap.fill(f"Ahead, there is a {ahead.desc}({ahead.event}).", width=70) + "\n")
	time.sleep(3)

	choices = ["Go left", "Go right","Go ahead", "Check stats", "Open inventory"]

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
	
		if choice.lower() == "go left":
			print(f"You decide to go to the left.\n")
			time.sleep(3)
			return left

		if choice.lower() == "go right":
			print(f"You decide to go to the right.\n")
			time.sleep(3)
			return right

		if choice.lower() == "go ahead":
			print(f"You decide to go straight.\n")
			time.sleep(3)
			return ahead