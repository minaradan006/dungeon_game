import time
import textwrap
import random
from hero import Character
from rooms import Room
from rooms import walls, room_adjectives
from story import print_choices

def inventory(character: Character):
	print("INVENTORY".center(40, "=") + "\n")

	while(True):
		print("What will you do?")
		time.sleep(0.5)
		choices = ["Equip Weapon", "Equip Armour", "Heal", "Close inventory"]
		print_choices(choices)

		choice = input()
		print()

		if choice.lower() == "equip weapon":
			print("Weapons".center(20, "-") + "\n")
			time.sleep(0.5)
			for item in character.inventory["weapons"]:
				print(item)
				time.sleep(0.5)
			print()

			weapon_name = input("What weapon do you want to equip? ")
			print()
			character.equip_weapon(weapon_name)
		elif choice.lower() == "equip armour":
			print("Armour".center(20, "-") + "\n")
			time.sleep(0.5)
			for item in character.inventory["armour"]:
				print(item)
				time.sleep(0.5)
			print()

			armour_name = input("What armour do you want to equip? ")
			print()
			character.equip_armour(armour_name)
		elif choice.lower() == "heal":
			print("Health Potions".center(20, "-") + "\n")
			time.sleep(0.5)
			for item in character.inventory["health potions"]:
				print(item)
				time.sleep(0.5)
			print()

			potion_name = input("What potion do you want to use? ")
			print()
			character.heal(potion_name)
		elif choice.lower() == "close inventory":
			break
		else:
			print("Invalid choice. Try again\n")
			time.sleep(2)

	print("Closing inventory...\n")

def scenario_1(character: Character, level: int):
	print(textwrap.fill(f"Walls of {random.choice(walls)} block your sides. You can only go [ahead].", width=70) + "\n")
	time.sleep(3)

	ahead = Room(level)
	ahead_message = textwrap.fill(f"Ahead, there is a {ahead.desc}({ahead.event}).", width=70) + "\n"
	print(ahead_message)
	time.sleep(3)

	choices = ["Go ahead", "Check stats", "Open inventory", "Check directions"]

	while True:
		print("What will you do?")
		time.sleep(0.5)
		print_choices(choices)
		choice = input()
		print()

		if choice.lower() == "check stats":
			print("STATS".center(40, "=") + "\n")
			print(character)
		elif choice.lower() == "open inventory":
			inventory(character)
		elif choice.lower() == "go ahead":
			print(f"You decide to go straight.\n")
			time.sleep(3)
			return ahead
		elif choice.lower() == "check directions":
			print(ahead_message)
			time.sleep(3)
		else:
			print("Invalid choice. Try again.\n")
			time.sleep(2)

def scenario_2(character: Character, level: int):
	print(textwrap.fill(f"A wall of {random.choice(walls)} blocks your path. You can only go [left] or [right].", width=70) + "\n")
	time.sleep(3)

	left = Room(level)
	left_message = textwrap.fill(f"To the left, there is a {left.desc}({left.event}).", width=70) + "\n"
	print(left_message)
	time.sleep(3)

	right = Room(level)
	right_message = textwrap.fill(f"To the right, there is a {right.desc}({right.event}).", width=70) + "\n"
	print(right_message)
	time.sleep(3)

	choices = ["Go left", "Go right", "Check stats", "Open inventory", "Check directions"]

	while True:
		print("What will you do?")
		time.sleep(0.5)
		print_choices(choices)
		choice = input()
		print()
	
		if choice.lower() == "check stats":
			print("STATS".center(40, "=") + "\n")
			print(character)
		elif choice.lower() == "open inventory":
			inventory(character)
		elif choice.lower() == "go left":
			print(f"You decide to go to the left.\n")
			time.sleep(3)
			return left
		elif choice.lower() == "go right":
			print(f"You decide to go to the right.\n")
			time.sleep(3)
			return right
		elif choice.lower() == "check directions":
			print(left_message)
			time.sleep(3)

			print(right_message)
			time.sleep(3)
		else:
			print("Invalid choice. Try again\n")
			time.sleep(2)

def scenario_3(character: Character, level: int):
	print(textwrap.fill(f"You stand at a crossroad. You can go [left], [right] or [ahead].", width=70) + "\n")
	time.sleep(3)

	left = Room(level)
	left_message = textwrap.fill(f"To the left, there is a {left.desc}({left.event}).", width=70) + "\n"
	print(left_message)
	time.sleep(3)

	right = Room(level)
	right_message = textwrap.fill(f"To the right, there is a {right.desc}({right.event}).", width=70) + "\n"
	print(right_message)
	time.sleep(3)

	ahead = Room(level)
	ahead_message = textwrap.fill(f"Ahead, there is a {ahead.desc}({ahead.event}).", width=70) + "\n"
	print(ahead_message)
	time.sleep(3)

	choices = ["Go left", "Go right","Go ahead", "Check stats", "Open inventory", "Check directions"]

	while True:
		print("What will you do?")
		time.sleep(0.5)
		print_choices(choices)
		choice = input()
		print()
	
		if choice.lower() == "check stats":
			print("STATS".center(40, "=") + "\n")
			print(character)
		elif choice.lower() == "open inventory":
			inventory(character)
		elif choice.lower() == "go left":
			print(f"You decide to go to the left.\n")
			time.sleep(3)
			return left
		elif choice.lower() == "go right":
			print(f"You decide to go to the right.\n")
			time.sleep(3)
			return right
		elif choice.lower() == "go ahead":
			print(f"You decide to go straight.\n")
			time.sleep(3)
			return ahead
		elif choice.lower() == "check directions":
			print(left_message)
			time.sleep(3)

			print(right_message)
			time.sleep(3)

			print(ahead_message)
			time.sleep(3)
		else:
			print("Invalid choice. Try again\n")
			time.sleep(2)
