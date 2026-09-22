import textwrap
import time
import random
from hero import Character, Gold
from items import Weapon, Armour, Potion
from monsters import Monster, shadow_dragon
from story import print_choices

fight_messages = []

def boss(character: Character, boss: Monster):
	half = False
	while True:
		if character.health <= 0:
			print("You fainted...\n")
			time.sleep(5)
			return False

		print("What will you do?")
		time.sleep(0.5)

		choices = ["Attack", "Heal", "Check stats", "Check boss"]
		print_choices(choices)

		choice = input()
		print()

		if choice.lower() == "check stats":
			print("STATS".center(40, "=") + "\n")
			print(character)
			continue
		elif choice.lower() == "check ":
			print(boss)
			continue
		elif choice.lower() == "heal":
			print("Health Potions".center(20, "-") + "\n")
			time.sleep(0.5)

			for item in character.inventory["health potions"]:
				print(item)
				time.sleep(0.5)
			print("[Back]\n")
			time.sleep(0.5)

			potion_name = input("What potion do you want to use? ")
			print()

			if potion_name.lower() == "back":
				continue

			character.heal(potion_name)
		elif choice.lower() == "attack":
			print(f"You decide to attack [{boss.name}].\n")
			time.sleep(3)
			boss.damage_taken(character)
			if boss.health <= 100 and not half:
				boss.attack *= 2
				# story

			if boss.health <= 0:
				print("=" * 70 + "\n")
				print(f"You defeated [{boss.name}]!\n")
				print("=" * 70 + "\n")
				time.sleep(5)

				return True

			print("-" * 70 + "\n")
			print(random.choice(fight_messages))
			print("-" * 70 + "\n")
			time.sleep(3)
		else:
			print("Invalid choice. Try again.\n")
			time.sleep(2)
			continue

		boss.attack_character(character)
		print("-" * 70 + "\n")