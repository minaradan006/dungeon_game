import random
import time
import textwrap

class Weapon:
	def __init__(self, name: str = None, damage: int = 0, desc: str = None):
		self.name = name
		self.damage = damage
		self.desc = desc

	def __str__(self):
		return f"[{self.name}] (+{self.damage} ATK): {self.desc}\n"

class Armour:
	def __init__(self, name: str = None, protection: int = 0, desc: str = None):
		self.name = name
		self.protection = protection
		self.desc = desc

	def __str__(self):
		return f"[{self.name}] (+{self.protection} DEF): {self.desc}\n"

class Potion:
	def __init__(self, name: str, points:int, desc: str):
		self.name = name
		self.points = points
		self.desc = desc

	def __str__(self):
		return f"[{self.name}] (+{self.points} HP): {self.desc}\n"

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

def show_start_screen():
	time.sleep(0.5)

	print("\n")
	print(r"""
	   \                             /
	   |                             |
	 .'|'.                         .'|'.
	/.'|\ \          THE          /./|'.\
	| /|'.|       OVERGROWN       |.'|\ |
	 \ |\/         DUNGEON         \/| /
	  \/                             \|
	  '                                `
	""")

	time.sleep(0.5)

	eq_line = "=" * 41
	print(eq_line.center(53))
	time.sleep(0.5)

	print("WELCOME TO THE OVERGROWN DUNGEON".center(53))
	time.sleep(0.5)

	print(eq_line.center(53))
	time.sleep(0.5)

	print("Survive 5 levels and win!".center(53))
	time.sleep(0.5)

	line = "-" * 41
	print(line.center(53))
	time.sleep(0.5)

	print("\n" * 1)
	input("Press [Enter] to begin your adventure...")
	print("\n" * 1)
	time.sleep(0.5)

def begin():
	print(textwrap.fill("The Book of Light is an ancient relic that is found at the end of the Overgrown Dungeon.", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("It is said that only the strongest and wisest of men can complete the gauntlet of challenges inside the dungeon.", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("You make your way through The Forest of Wishes and reach the vine covered entrance.\n", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("There's some writing etched into the smooth stone door:\n", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("'To pass this door, one must state their name followed by their power.'\n", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("You remember reading in The Book of Dungeons that power means attack and defense. Their sum must be 10.\n", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("Reluctantly, you open your mouth and utter the three words.\n", width=60))
	print()
	time.sleep(2)

	name = input("What is your name? ")

	while True:
		attack = int(input("What is your attack stat? "))
		defense = int(input("What is your defense stat? "))
		print()

		if attack + defense == 10:
			print(textwrap.fill("The door rumbles and slowly lowers itself into the ground.\n", width=60))
			print()
			time.sleep(3)

			print(textwrap.fill("As a cold wind escapes the dungeon, you push past the creeping vines and enter through the opening.\n", width=60))
			print()
			time.sleep(3)

			print(textwrap.fill("The heavy door instantly seals itself behind you.\n", width=60))
			print()
			time.sleep(2)

			print("The challenge has begun!\n")
			print()
			time.sleep(2)

			return name, attack, defense
		else:
			print(textwrap.fill("The sum of the attack stat and the defense stat should be 10. Try again.\n", width=60))
			print()

walls = [
	"vines",
	"fire",
	"bones",
	"gems",
	"water",
	"flowers",
	"blood"
]

room_adjectives = [
	"dark",
	"dusty",
	"musty",
	"echoing",
	"freezing",
	"burning",
	"crumbling",
	"blood-stained",
	"sunny",
	"bright"
]

room_types = [
	"corridor",
	"chamber",
	"crypt",
	"armory",
	"dungeon cell",
	"hallway",
	"library",
	"garden"
]

class Room:
	def __init__(self, level):
		r_adj = random.choice(room_adjectives)
		r_type = random.choice(room_types)

		self.desc = f"a {r_adj} {r_type}"

		self.event = random.choices(
		["enemy", "treasure", "trap", "shop", "empty"],
		weights=[0.4 + (level * 0.05), 0.2, 0.3, 0.2, 0.2],
	)[0]

def print_valid_choices(valid_choices):
	for choice in valid_choices:
		print(f"[{choice}]", end=" ")
		time.sleep(0.2)
	print()

def inventory(character: Character):
	print("INVENTORY".center(40, "=") + "\n")

	for category, content in character.inventory.items():
		print(f"{category.title()}".center(20, "-") + "\n")

		for item in content:
			print(item)

		print()
		time.sleep(0.5)

	while(True):
		print("What do you want to do?")
		time.sleep(0.5)
		print("[Equip Weapon]", end="  ")
		print("[Equip Armour]", end="  ")
		print("[Heal]", end="  ")
		print("[Go back]")

		choice = input()
		print()

		if choice.lower() == "equip weapon":
			weapon_name = input("What weapon do you want to equip? ")
			print()
			character.equip_weapon(weapon_name)

		if choice.lower() == "equip armour":
			armour_name = input("What armour do you want to equip? ")
			print()
			character.equip_armour(armour_name)

		if choice.lower() == "heal":
			potion_name = input("What potion do you want to use? ")
			print()
			character.heal(potion_name)

		if choice.lower() == "go back":
			break

	print("Closing inventory..." + "\n")


def scenario_1(character: Character, level: int):
	print(textwrap.fill(f"A wall of {random.choice(walls)} blocks your sides. You can only go [ahead].", width=60))
	print()
	time.sleep(3)

	ahead = Room(level)
	print(textwrap.fill(f"Ahead, there is {ahead.desc}({ahead.event}).", width=70) + "\n")
	time.sleep(3)

	valid_choices = ["Go ahead", "Check stats", "Open inventory"]

	while True:
		print("What will you do?")
		time.sleep(0.5)
		print_valid_choices(valid_choices)
		choice = input()
		print()

		if choice.lower() == "check stats":
			print("STATS".center(40, "=") + "\n")
			print(character)

		if choice.lower() == "open inventory":
			inventory(character)

		if choice.lower() == "go ahead":
			return ahead

if __name__ == "__main__":
	show_start_screen()

	name, attack, defense = begin()
	character = Character(name, attack, defense)

	character.inventory["weapons"].append(Weapon("Longsword", 5, "Heavy and slow, but sturdy."))
	armour = Armour("Copper Helmet", 3, "A few scratches can be seen reflected in the light.")
	weapon = Weapon("Silver Dagger", 2, "Small but very agile.")
	potion = Potion("Small Potion", 10, "Can be used to heal a small amount of health")
	character.inventory["weapons"].append(weapon)
	character.inventory["armour"].append(armour)
	character.inventory["health potions"].append(potion)


	for level in range(1, 5):
		print("~" * 70)
		print(f"LEVEL {level}".center(70))
		print("~" * 70 + "\n")
		time.sleep(1)

		mini_stages = random.choice(range(1, 2))

		for mini in range(0, mini_stages):
			scenario = random.choice(range(1, 2))

			if scenario == 1:
				choice = scenario_1(character, level)
			elif scenario == 2:
				pass

	print("You did it!")
