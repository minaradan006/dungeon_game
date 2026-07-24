import textwrap
import time
from hero import Character
from monster_sprites import owl_sprite, skeleton_sprite, rat_sprite, knight_sprite, eye_sprite, axe_orc_sprite, moth_sprite,rose_assasin_sprite

class Monster:
	def __init__(self, name: str, desc: str, sprite: str, health: int, attack: int):
		self.name = name
		self.desc = desc
		self.sprite = sprite
		self.health = health
		self.attack = attack

	def attack_level(self, level: int):
		self.attack = int(self.attack * (1 + level * 0.05))

	def health_level(self, level: int):
		self.health = int(self.health * (1 + level * 0.1))

	def update_stats(self, level: int):
		self.attack_level(level)
		self.health_level(level)

	def attack_character(self, character: Character, level: int):
		character.health -= self.atk * (100 - character.get_total_defense()) // 100

	def damage_taken(self, character: Character, level: int):
		self.health -= character.get_total_attack()

wise_owl = Monster("The Wise Owl", "...", owl_sprite, 100, 5)
skeleton_warrior = Monster("The Skeleton Warrior", "...", skeleton_sprite, 50, 10)
rat_king = Monster("The Rat King", "...", rat_sprite, 80, 6)
knight = Monster("The Knight", "...", knight_sprite, 90, 7)
eye = Monster("The Eye", "...", eye_sprite, 40, 9)
axe_orc = Monster("The Axed Orc", "...", axe_orc_sprite, 80, 7)
glowing_moth = Monster("The Glowing Moth", "...", moth_sprite, 60, 5)
rose_assasin = Monster("The Rose Assassin", "...", rose_assasin_sprite, 60, 8)

fight_messages = [
	"The monster stumbles, but regains its footing.",
	"The monster seems scared.",
	"A whimper can be heard echoingin the room.",
	"The room shakes, dust particles floating in the air.",
	"The monster seems bored."
	"The monster stares at you, making you shiver.",
	"The monster doesn't seem too pleased.",
	"The lights seem to glow brighter.",
	"The lights seem to dim.",
	"Sweat droplets fall from your forehead to the ground."
]

def enemy(level: int, monster: Monster):
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
