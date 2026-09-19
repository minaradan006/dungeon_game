import textwrap
import time
import random
from hero import Character, Gold
from items import Weapon, Armour, Potion
from monster_sprites import owl_sprite, skeleton_sprite, rat_sprite, knight_sprite, eye_sprite, axe_orc_sprite, moth_sprite, rose_assasin_sprite
from story import print_choices

class Monster:
	def __init__(self, name: str, desc: str, sprite: str, health: int, attack: int, loot):
		self.name = name
		self.desc = desc
		self.sprite = sprite
		self.health = health
		self.max_health = health
		self.attack = attack
		self.loot = loot

	def __str__(self):
		return f"[{self.name}]: {self.desc}\nHP: {self.health}/{self.max_health}\n"

	def attack_level(self, level: int):
		self.attack = int(self.attack * (1 + level * 0.20))

	def health_level(self, level: int):
		self.health = int(self.health * (1 + level * 0.20))
		self.max_health = self.health

	def update_stats(self, level: int):
		self.attack_level(level)
		self.health_level(level)

	def attack_character(self, character: Character):
		random_atk = random.choice(range(-50, 50, 5))

		if random_atk < int(-50 * 0.75):
			print(f"{self.name} doesn't take you very seriously, dealing a very weak attack!\n")
			time.sleep(3)
		elif random_atk < int(-50 * 0.5):
			print(f"{self.name} misses parts of its attack, dealing a weak attack.\n")
			time.sleep(3)
		elif random_atk < int(50 * 0.5):
			print(f"{self.name} throws you to the back of the room, dealing a normal attack.\n")
			time.sleep(3)
		elif random_atk < int(50 * 0.75):
			print(f"{self.name} slashes at you, dealing a powerful attack.\n")
			time.sleep(3)
		else:
			print(f"{self.name} manages to hit your weak spot, dealing a very powerful attack...\n")
			time.sleep(3)

		damage = self.attack * (100 - character.get_total_defense() + random_atk) // 100
		character.health -= damage

		print(f"Your HP dropped by {damage} points.\n")
		time.sleep(3)

	def damage_taken(self, character: Character):
		random_atk = random.choice(range(-50, 50, 5))

		if random_atk < int(-50 * 0.75):
			print("You trip and fumble, landing a very weak attack...\n")
			time.sleep(3)
		elif random_atk < int(-50 * 0.5):
			print("You get distracted, landing a weak attack.\n")
			time.sleep(3)
		elif random_atk < int(50 * 0.5):
			print(f"You punch {self.name}, landing a normal attack.\n")
			time.sleep(3)
		elif random_atk < int(50 * 0.75):
			print(f"You slash at {self.name}, landing a powerful attack.\n")
			time.sleep(3)
		else:
			print("You hit a weak spot, landing a very powerful attack!\n")
			time.sleep(3)

		damage = character.get_total_attack() * (100 + random_atk) // 100
		self.health -= damage

		print(f"{self.name}'s HP dropped by {damage} points.\n")
		time.sleep(2)

wise_owl_claw = Weapon("Wise Owl Claw", 11, "Its point is so sharp you can't even see it.", 40)
wise_owl = Monster("The Wise Owl", "...", owl_sprite, 50, 5, wise_owl_claw)

pirate_sword = Weapon("Pirate Sword", 12, "The metal blade is splattered with blood.", 45)
skeleton_pirate = Monster("The Skeleton Pirate", "...", skeleton_sprite, 50, 8, pirate_sword)

rat_suit = Armour("Rat Suit", 11, "The furry suit is surprisingly sturdy.", 40)
rat_king = Monster("The Rat King", "...", rat_sprite, 50, 6, rat_suit)

knight_suit = Armour("Knight Suit", 13, "Makes you look like royalty.", 45)
knight = Monster("The Knight", "...", knight_sprite, 55, 6, knight_suit)

crystal_tears = Potion("Crystal Tears", 999, "Increases max health and restores health to max.", 50)
eye = Monster("The Eye", "...", eye_sprite, 45, 9, crystal_tears)

flaming_axe = Weapon("Flaming Axe", 12, "It emits a bright red glow.", 45)
axe_orc = Monster("The Axed Orc", "...", axe_orc_sprite, 55, 7, flaming_axe)

wing_cloak = Armour("Wing Cloak", 12, "Makes you translucent.", 45)
glowing_moth = Monster("The Glowing Moth", "...", moth_sprite, 40, 5, wing_cloak)

rose_blade = Weapon("Rose Blade", 13, "Its handle is shaped like a delicate rose.", 55)
rose_assasin = Monster("The Rose Assassin", "...", rose_assasin_sprite, 55, 7, rose_blade)

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
			print()
			potion_name = input("What potion do you want to use? ")
			print()
			character.heal(potion_name)
		elif choice.lower() == "attack":
			print("You decide to attack the monster.\n")
			time.sleep(3)
			monster.damage_taken(character)

			if monster.health <= 0:
				print("=" * 70 + "\n")
				print(f"You defeated {monster.name}!\n")
				print("=" * 70 + "\n")
				time.sleep(5)

				gold = Gold(30, 60)
				print(f"You received {gold.amount} gold!\n")
				time.sleep(2)

				item = random.choices([None, monster.loot], weights = [0.9, 0.1])[0]

				if not item:
					print("The monster scurried away before you could catch it.\n")
					time.sleep(3)

					return True

				print(f"You received: [{item.name}]!\n")

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
						character.inventory["health potions"].append(item)

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
