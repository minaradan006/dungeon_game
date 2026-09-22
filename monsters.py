import textwrap
import time
import random
from hero import Character, Gold
from items import Weapon, Armour, Potion
from monster_sprites import owl_sprite, skeleton_sprite, rat_sprite, knight_sprite, eye_sprite, axe_orc_sprite, moth_sprite, rose_assasin_sprite, shadow_dragon_sprite
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

shadow_dragon = Monster("The Shadow Dragon", "...", shadow_dragon_sprite, 200, 10, None)