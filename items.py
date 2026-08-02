import random

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
		self.num = 1
		self.points = points
		self.desc = desc

	def __str__(self):
		return f"{self.num} x [{self.name}] (+{self.points} HP): {self.desc}"

leather_leggings = Armour("Leather Leggings", 2, "Very stylish, but not very useful in combat.")
wooden_chestplate = Armour("Wooden Chestplate", 3, "A fire hazard.")
copper_helmet = Armour("Copper Helmet", 5, "A few scratches can be seen reflected in the light.")
chainmail_shirt = Armour("Chainmail Shirt", 6, "A bit rusty, but still very effective against slashes.")
copper_chestplate = Armour("Coppr Chestplate", 7, "It looks like it's made from lava.")
copper_suit = Armour("Copper Suit", 9, "Copper covers your full body.")
steel_armour = Armour("Steel Armour", 10, "It is very heavy, giving a menacing look to anyone who wears it")

stick = Weapon("Stick", 1, "Loved by many dogs.")
wooden_sword = Weapon("Wooden Sword", 2, "Pretty sharp but not very durable.")
lance = Weapon("Lance", 3, "The only thing missing is a horse.")
silver_dagger = Weapon("Silver Dagger", 4, "Small but very agile.")
bone_spear = Weapon("Bone Spear", 4, "Like a true caveman.")
steel_gauntlets = Weapon("Steel Gauntlets", 5, "Good if you like to punch monsters to death.")
twin_blades = Weapon("Twin Blades", 6, "Two is always better than one.")
bow = Weapon("Bow", 7, "Carved with little vines and leaves.")
longsword = Weapon("Longsword", 8, "Heavy and slow, but sturdy.")
warrior_sword = Weapon("Warrior Sword", 9, "Transforms you into a true warrior.")

small_potion = Potion("Small Potion", 10, "Can be used to heal a small amount of health.")
medium_potion = Potion("Medium Potion", 25, "Can be used to heal a medium amount of health.")
big_potion = Potion("Big Potion", 40, "Can be used to heal a big amount of health.")
giant_potion = Potion("Giant Potion", 100, "Can be used to heal a giant amount of health.")

wooden_chest_loot = [
	leather_leggings,
	wooden_chestplate,
	copper_helmet,
	chainmail_shirt,
	stick,
	wooden_sword,
	lance,
	bone_spear,
	silver_dagger,
	small_potion,
	medium_potion,
]

silver_chest_loot = [
	copper_helmet,
	chainmail_shirt,
	copper_chestplate,
	copper_suit,
	bone_spear,
	silver_dagger,
	steel_gauntlets,
	twin_blades,
	bow,
	medium_potion,
	big_potion
]

golden_chest_loot = [
	chainmail_shirt,
	copper_chestplate,
	copper_suit,
	steel_armour,
	steel_gauntlets,
	twin_blades,
	bow,
	longsword,
	warrior_sword,
	big_potion,
	giant_potion
]