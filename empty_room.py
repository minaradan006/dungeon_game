import time
import textwrap
import random
from story import print_choices
from hero import Character, Gold

def empty(character: Character):
	print(textwrap.fill("The room seems to be empty, nothing standing out.", 70))
	time.sleep(3)
	print()

	while True:
		print("What will you do?")
		time.sleep(1)
		choices = ["Search around", "Leave"]
		print_choices(choices)

		choice = input()
		print()

		if choice.lower() == "search around":
			print(textwrap.fill("You decide to search around the room.", 70) + "\n")
			time.sleep(2)

			loot = [None, "lockpick", "gold"]
			item = random.choices(loot, weights=[0.2, 0.35, 0.45])[0]

			if not item:
				print(textwrap.fill("You rummage through every corner of the room, but you don't find anything...", 70) + "\n")
				time.sleep(3)
				return

			print(textwrap.fill("You look around the room and...", 70) + "\n")
			time.sleep(4)
			if item == "lockpick":
				num = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]

				print(f"You found {num} x lockpick!\n")
				time.sleep(2)

				character.lockpicks += num
				return

			if item == "gold":
				gold = Gold(-20, 50)

				if gold.amount < 0:
					if -gold.amount > character.gold:
						gold.amount = -character.gold
					print(f"You stumbled and lost {gold.amount} gold...\n")
					time.sleep(2)
					character.gold += gold.amount
					return

				print(f"You found {gold.amount} gold!\n")
				time.sleep(2)
				character.gold += gold.amount
				return

		if choice.lower() == "leave":
			print(textwrap.fill("You decide to leave the room.", 70) + "\n")
			return

		print("Invalid choice. Try again\n")
		time.sleep(0.5)
