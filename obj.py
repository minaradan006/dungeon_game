import time
import random
from items import room_types, room_adjectives

class Weapon:
	def __init__(self, name: str = None, damage: int = 0, desc: str = None):
		self.name = name
		self.damage = damage
		self.desc = desc

	def __str__(self):
		return f"[{self.name}] (+{self.damage} ATK): {self.desc}"

class Armour:
	def __init__(self, name: str = None, protection: int = 0, desc: str = None):
		self.name = name
		self.protection = protection
		self.desc = desc

	def __str__(self):
		return f"[{self.name}] (+{self.protection} DEF): {self.desc}"

class Potion:
	def __init__(self, name: str, points:int, desc: str):
		self.name = name
		self.points = points
		self.desc = desc

	def __str__(self):
		return f"[{self.name}] (+{self.points} HP): {self.desc}"

class Character:
	def __init__(self, name: str, attack: int, defense: int):
		self.name = name
		self.health = 100
		self.attack = attack
		self.defense = defense
		self.gold = 0
		self.inventory = {
			"weapons": [],
			"armour": [],
			"health potions": []
		}
		self.equipped = {
			"weapon": Weapon(),
			"armour": Armour()
		}

	def __str__(self):
		name = f"Name: {self.name}\n"
		health = f"HP: {self.health}/100\n"
		attack = f"ATK: {self.get_total_attack()}\n"
		defense = f"DEF: {self.get_total_defense()}\n"
		gold = f"Gold: {self.gold}\n"
		weapon = f"Weapon: {self.equipped["weapon"].name}\n"
		armour = f"Armour: {self.equipped["armour"].name}\n"

		return name + health + attack + defense + gold + weapon + armour

	def heal(self, potion_name):
		for idx, potion in enumerate(self.inventory["health potions"]):
			if potion.name.lower() == potion_name.lower():
				if self.health < 100:
					print(f"Your health has been restored!")
					self.health += potion.points

					if self.health > 100:
						self.health = 100

					del self.inventory["health potions"][idx]
					return
				else:
					print(f"Your health is full.")
					return
		print(f"No {potion_name} in your inventory...")


	def equip_weapon(self, weapon_name):
		found_weapon = None

		for weapon in self.inventory['weapons']:
			if weapon.name.lower() == weapon_name.lower():
				found_weapon = weapon

				old_attack = self.equipped["weapon"].damage
				self.equipped["weapon"] = weapon

				print(f"Equipped {weapon_name}: ", end="")

				if old_attack <= weapon.damage:
					print(f"+{weapon.damage - old_attack} ATK.\n")
				else:
					print(f"{weapon.damage - old_attack} ATK.\n")

				time.sleep(0.5)
				break

		if not found_weapon:
			print(f"{weapon_name} doesn't exist in inventory...\n")
			time.sleep(0.5)

	def equip_armour(self, armour_name):
		found_armour = None
		
		for armour in self.inventory['armour']:
			if armour.name.lower() == armour_name.lower():
				found_armour = armour

				old_defense = self.equipped["armour"].protection
				self.equipped["armour"] = armour

				print(f"Equipped {armour_name}: ", end="")

				if old_defense <= armour.protection:
					print(f"+{armour.protection - old_defense} DEF.\n")
				else:
					print(f"{armour.protection - old_defense} DEF.\n")

				time.sleep(0.5)
				break

		if not found_armour:
			print(f"{armour_name} doesn't exist in inventory...")
			time.sleep(0.5)

	def get_total_attack(self):
		base_attack = self.attack
		weapon_bonus = self.equipped["weapon"].damage
		return base_attack + weapon_bonus

	def get_total_defense(self):
			base_defense = self.defense
			armour_bonus = self.equipped["armour"].protection
			return base_defense + armour_bonus

class Room:
	def __init__(self, level):
		r_adj = random.choice(room_adjectives)
		r_type = random.choice(room_types)

		self.desc = f"a {r_adj} {r_type}"

		self.event = random.choices(
		["enemy", "treasure", "trap", "shop", "empty"],
		weights=[0.4 + (level * 0.05), 0.2, 0.3, 0.2, 0.2],
	)[0]
