import textwrap
import time
import random
from hero import Character, Gold
from items import Weapon, Armour, Potion
from monsters import Monster, wise_owl, skeleton_pirate, rat_king, knight, eye, axe_orc, glowing_moth, rose_assasin
from story import print_choices

fight_messages = [
	"The monster stumbles, but regains its footing.\n",
	"The monster seems scared.\n",
	"A whimper can be heard echoing in the room.\n",
	"The room shakes, dust particles floating in the air.\n",
	"The monster seems bored.\n",
	"The monster stares at you, making you shiver.\n",
	"The monster doesn't seem too pleased.\n",
	"The lights seem to glow brighter.\n",
	"The lights seem to dim.\n",
	"Sweat droplets fall from your forehead to the ground.\n"
]

def enemy(character: Character, level: int, monster: Monster) -> bool:
	print(textwrap.fill("A quiet, rumbling sound can be heard from the shadows and slowly something emerges from them.", 70) + "\n")
	time.sleep(3)

	monster.update_stats(level)

	print(f"The monster is...\n")
	time.sleep(2)

	print(monster.sprite)
	time.sleep(1)

	print("-" * 70)
	print(monster.name + f"({monster.health} HP, {monster.attack} ATK)")
	print("-" * 70 + "\n")
	time.sleep(2)

	while True:
		if character.health <= 0:
			print("You fainted...\n")
			time.sleep(5)
			return False

		print("What will you do?")
		time.sleep(0.5)

		choices = ["Attack", "Heal", "Check stats", "Check monster"]
		print_choices(choices)

		choice = input()
		print()

		if choice.lower() == "check stats":
			print("STATS".center(40, "=") + "\n")
			print(character)
			continue
		elif choice.lower() == "check monster":
			print(monster)
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
			print(f"You decide to attack [{monster.name}].\n")
			time.sleep(3)
			monster.damage_taken(character)

			if monster.health <= 0:
				print("=" * 70 + "\n")
				print(f"You defeated [{monster.name}]!\n")
				print("=" * 70 + "\n")
				time.sleep(5)

				gold = Gold(30, 60)
				print(f"You received {gold.amount} gold!\n")
				time.sleep(2)

				item = random.choice([None, monster.loot])

				if not item:
					print("The monster scurried away before you could catch it.\n")
					time.sleep(3)

					return True

				print(f"You received: [{item.name}]!\n")

				character.receive_item(item)

				print("The monster scurried away before you could catch it.\n")
				time.sleep(3)

				return True

			print("-" * 70 + "\n")
			print(random.choice(fight_messages))
			print("-" * 70 + "\n")
			time.sleep(3)
		else:
			print("Invalid choice. Try again.\n")
			time.sleep(2)
			continue

		monster.attack_character(character)
		print("-" * 70 + "\n")
