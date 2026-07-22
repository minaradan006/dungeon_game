import random

class Character:
	def __init__(self, name, attack, defense):
		self.name = name
		self.health = 100
		self.attack = attack
		self.defense = defense
		self.gold = 0
		self.inventory = dict()
		self.equipped = {
			"weapon": None,
			"armour": None
		}

	def heal(self):
		if 'health potion' in self.inventory:
			if self.health < 100:
				self.inventory['health potion'] -= 1
				print(f"{self.name}'s health has been restored!")
				self.health += 30
			else:
				print(f"{self.name}'s health is full.")
		else:
			print(f"No healing potions in {self.name}'s inventory...")

	def equip_weapon(self, weapon_name):
		found_weapon = None

		for weapon in self.inventory['weapons']:
			if weapon["name"].lower() == weapon_name.lower():
				found_weapon = weapon

				old_attack = weapon["attack_bonus"]
				self.equipped["weapon"] = weapon["name"]

				print(f"Equipped {weapon["name"]}: ", end="")

				if old_attack <= weapon["attack_bonus"]:
					print(f"+{weapon["attack_bonus"] - old_attack}.")
				else:
					print(f"{weapon["attack_bonus"] - old_attack}.")

				break

		if not found_weapon:
			print(f"{weapon_name} doesn't exist in inventory...")

	def equip_armour(self, armour_name):
		found_armour = None
		
		for armour in self.inventory['armour']:
			if armour["name"].lower() == armour_name.lower():
				found_armour = armour

				old_defense = armour["defense_bonus"]
				self.equipped["armour"] = armour["name"]

				print(f"Equipped {armour["name"]}: ", end="")

				if old_defense <= armour["defense_bonus"]:
					print(f"+{armour["defense_bonus"] - old_defense}.")
				else:
					print(f"{armour["defense_bonus"] - old_defense}.")

				break

		if not found_armour:
			print(f"{armour_name} doesn't exist in inventory...")

	def get_total_attack(self):
		base_attack = self.attack
		weapon_bonus = self.equipped["weapon"]["attack_bonus"]
		return base_attack + weapon_bonus

	def get_total_defense(self):
			base_defense = self.defense
			armour_bonus = self.equipped["armour"]["armour_bonus"]
			return base_defense + armour_bonus

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
	"castle ruins",
	"garden"
]

def generate_random_room(level):
	r_adj = random.choice(room_adjectives)
	r_type = random.choice(room_types)
	description = f"You step into a {r_adj} {r_type}"

	event = random.choices(
		["enemy", "treasure", "trap", "empty"],
		weights=[0.4 + (level * 0.05), 0.2, 0.1, 0.2],
	)[0]

	room_data = {"description": description, "event": event}

	return room_data

def show_start_screen():
	print(r"""
	   |                             |
	 .'|'.                         .'|'.
	/.'|\ \          THE          /.'|'.\
	| /|'.|       OVERGROWN       |.'|\ |
	 \ |\/         DUNGEON         \/| /
	  \|/                           \|/
	   `                             `
	""")
	eq_line = "=" * 41
	print(eq_line.center(53))
	print("WELCOME TO THE OVERGROWN DUNGEON".center(53))
	print(eq_line.center(53))
	print("Survive 5 levels and win!".center(53))
	line = "-" * 41
	print(line.center(53))

	print("\n" * 1)
	input("Press [Enter] to begin your adventure...")
	print("\n" * 1)

if __name__ == "__main__":
	show_start_screen()
