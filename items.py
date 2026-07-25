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

copper_helmet = Armour("Copper Helmet", 5, "A few scratches can be seen reflected in the light.")
chainmail_shirt = Armour("Chainmail Shirt", 6, "A bit rusty, but still very effective against slashes.")
knight_suit = Armour("Knight Suit", 10, "It is very heavy, giving a menacing look to anyone who wears it")
leather_leggings = Armour("Leather Leggings", 2, "Very stylish, but not very useful in combat.")
wood_chestplate = Armour("Wood Chestplate", 3, "A fire hazard.")

silver_dagger = Weapon("Silver Dagger", 4, "Small but very agile.")
longsword = Weapon("Longsword", 8, "Heavy and slow, but sturdy.")
bow = Weapon("Bow", 7, "Carved with little vines and leaves.")
steel_gauntlets = Weapon("Steel Gauntlets", 4, "Good if you want to punch monsters to death.")
wood_sword = Weapon("Wood Sword", 2, "Pretty sharp but not very durable.")
stick = Weapon("Stick", 1, "Loved by many dogs.")
twin_blades = Weapon("Twin Blades", 6, "Two is always better than one.")
bone_spear = Weapon("Bone spear", 3, "Like a true caveman.")

small_potion = Potion("Small Potion", 10, "Can be used to heal a small amount of health.")
medium_potion = Potion("Medium Potion", 25, "Can be used to heal a medium amount of health.")
big_potion = Potion("Big Potion", 40, "Can be used to heal a big amount og health.")
max_potion = Potion("Max Potion", 100, "Can be used to heal your health to max.")
