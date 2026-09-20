import time
import random
from items import Weapon, Armour, Potion

class Character:
	def __init__(self, name: str, attack: int, defense: int):
		self.name = name
		self.health = 100
		self.max_health = 100
		self.attack = attack
		self.defense = defense
		self.gold = 0
		self.lockpicks = 0
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
		health = f"HP: {self.health}/{self.max_health}\n"
		attack = f"ATK: {self.get_total_attack()}\n"
		defense = f"DEF: {self.get_total_defense()}\n"
		gold = f"Gold: {self.gold}\n"
		lockpicks = f"Lockpicks: {self.lockpicks}\n"
		weapon = f"Weapon: {self.equipped["weapon"].name}\n"
		armour = f"Armour: {self.equipped["armour"].name}\n"

		return name + health + attack + defense + gold + lockpicks + weapon + armour

	def heal(self, potion_name):
		for idx, potion in enumerate(self.inventory["health potions"]):
			if potion.name.lower() == potion_name.lower():
				if potion_name.lower() == "crystal tears":
					self.max_health += 30
					print("Your max health has been increased by 30 points!\n")

				if self.health < self.max_health:
					print(f"Your health has been restored!\n")
					time.sleep(2)
					self.health += potion.points

					if self.health > self.max_health:
						self.health = self.max_health

					potion.num -= 1
					if potion.num == 0:
						del self.inventory["health potions"][idx]
					return
				else:
					print(f"Your health is full.\n")
					time.sleep(2)
					return
		print(f"No {potion_name} in your inventory...\n")
		time.sleep(2)


	def equip_weapon(self, weapon_name):
		found_weapon = None

		for weapon in self.inventory['weapons']:
			if weapon.name.lower() == weapon_name.lower():
				found_weapon = weapon

				old_attack = self.equipped["weapon"].damage
				self.equipped["weapon"] = weapon

				print(f"Equipped {weapon.name}: ", end="")

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

				print(f"Equipped {armour.name}: ", end="")

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

	def receive_item(self, item):
		if isinstance(item, Weapon):
			self.inventory["weapons"].append(item)

		if isinstance(item, Armour):
			self.inventory["armour"].append(item)

		if isinstance(item, Potion):
			exists = 0
			for idx, potion in enumerate(self.inventory["health potions"]):
				if item.name == potion.name:
					potion.num += 1
					exists = 1
					break

			if not exists:
				self.inventory["health potions"].append(item)

class Gold:
	def __init__(self, start, end):
		self.amount = random.choice(range(start, end, 1))
