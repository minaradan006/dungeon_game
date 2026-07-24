import textwrap
import time
import random
from hero import Character
from monster_sprites import owl_sprite, skeleton_sprite, rat_sprite, knight_sprite, eye_sprite, axe_orc_sprite, moth_sprite,rose_assasin_sprite
from story import print_choices

class Monster:
	def __init__(self, name: str, desc: str, sprite: str, health: int, attack: int):
		self.name = name
		self.desc = desc
		self.sprite = sprite
		self.health = health
		self.max_health = health
		self.attack = attack

	def __str__(self):
		return f"{self.name}: {self.desc}\nHP: {self.health}/{self.max_health}\n"

	def attack_level(self, level: int):
		self.attack = int(self.attack * (1 + level * 0.05))

	def health_level(self, level: int):
		self.health = int(self.health * (1 + level * 0.1))
		self.max_health = self.health

	def update_stats(self, level: int):
		self.attack_level(level)
		self.health_level(level)

	def attack_character(self, character: Character, level: int):
		random_atk = random.choice(range(-20 * level, 20 * level, 1))

		if random_atk < int(-20 * level * 0.75):
			print(f"{self.name} doesn't take you very seriously, dealing a very weak attack!\n")
			time.sleep(3)
		elif random_atk < int(-20 * level * 0.25):
			print("The monster misses parts of its attack, dealing a weak attack.\n")
			time.sleep(3)
		elif random_atk < int(20 * level * 0.25):
			print(f"{self.name} throws you to the back of the room, dealing a normal attack.\n")
			time.sleep(3)
		elif random_atk < int(20 * level * 0.75):
			print(f"{self.name} slashes at you, dealing a powerful attack.\n")
			time.sleep(3)
		else:
			print(f"{self.name} manages to hit your weak spot, dealing a very powerful attack...\n")
			time.sleep(3)

		damage = self.attack * (100 - character.get_total_defense() + random_atk) // 100
		character.health -= damage

		print(f"Your HP dropped by {damage} points.\n")
		time.sleep(3)

	def damage_taken(self, character: Character, level: int):
		random_atk = random.choice(range(-20 * level, 20 * level, 1))

		if random_atk < int(-20 * level * 0.75):
			print("You trip and fumble, landing a very weak attack...\n")
			time.sleep(3)
		elif random_atk < int(-20 * level * 0.25):
			print("You get distracted, landing a weak attack.\n")
			time.sleep(3)
		elif random_atk < int(20 * level * 0.25):
			print(f"You punch {self.name}, landing a normal attack.\n")
			time.sleep(3)
		elif random_atk < int(20 * level * 0.75):
			print(f"You slash at {self.name}, landing a powerful attack.\n")
			time.sleep(3)
		else:
			print("You hit a weak spot, landing a very powerful attack!\n")
			time.sleep(3)

		damage = character.get_total_attack() * (100 + random_atk) // 100
		self.health -= damage

		print(f"{self.name}'s HP dropped by {damage} points.\n")
		time.sleep(2)


wise_owl = Monster("The Wise Owl", "...", owl_sprite, 100, 5)
skeleton_warrior = Monster("The Skeleton Warrior", "...", skeleton_sprite, 50, 10)
rat_king = Monster("The Rat King", "...", rat_sprite, 80, 6)
knight = Monster("The Knight", "...", knight_sprite, 90, 7)
eye = Monster("The Eye", "...", eye_sprite, 40, 9)
axe_orc = Monster("The Axed Orc", "...", axe_orc_sprite, 80, 7)
glowing_moth = Monster("The Glowing Moth", "...", moth_sprite, 60, 5)
rose_assasin = Monster("The Rose Assassin", "...", rose_assasin_sprite, 50, 8)

fight_messages = [
	"The monster stumbles, but regains its footing.\n",
	"The monster seems scared.\n",
	"A whimper can be heard echoing in the room.\n",
	"The room shakes, dust particles floating in the air.\n",
	"The monster seems bored.\n"
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
			potion_name = input("What potion do you want to use? ")
			print()
			character.heal(potion_name)
		elif choice.lower() == "attack":
			print("You decide to attack the monster.\n")
			time.sleep(3)
			monster.damage_taken(character, level)

			if monster.health <= 0:
				print(f"You defeated {monster.name}!\n")
				return True

			print("-" * 70 + "\n")
			print(random.choice(fight_messages))
			time.sleep(3)
		else:
			print("Invalid choice. Try again.\n")
			time.sleep(2)
			continue

		monster.attack_character(character, level)
		print("-" * 70 + "\n")

# character = Character("Mina", 10, 10)
# enemy(character, 3, rose_assasin)
