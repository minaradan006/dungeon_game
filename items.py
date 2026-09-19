import random

class Weapon:
	def __init__(self, name: str = None, damage: int = 0, desc: str = None, price: int = 0):
		self.name = name
		self.damage = damage
		self.desc = desc
		self.sell_price = price
		self.buy_price = price * 2

	def __str__(self):
		return f"[{self.name}] (+{self.damage} ATK): {self.desc}"

class Armour:
	def __init__(self, name: str = None, protection: int = 0, desc: str = None, price: int = 0):
		self.name = name
		self.protection = protection
		self.desc = desc
		self.sell_price = price
		self.buy_price = price * 2

	def __str__(self):
		return f"[{self.name}] (+{self.protection} DEF): {self.desc}"

class Potion:
	def __init__(self, name: str, points:int, desc: str, price: int = 0):
		self.name = name
		self.num = 1
		self.points = points
		self.desc = desc
		self.sell_price = price
		self.buy_price = price * 2

	def __str__(self):
		return f"{self.num} x [{self.name}] (+{self.points} HP): {self.desc}"

leather_leggings = Armour("Leather Leggings", 2, "Very stylish, but not very useful in combat.", 5)
wooden_chestplate = Armour("Wooden Chestplate", 3, "A fire hazard.", 7)
copper_helmet = Armour("Copper Helmet", 5, "A few scratches can be seen reflected in the light.", 10)
chainmail_shirt = Armour("Chainmail Shirt", 6, "A bit rusty, but still very effective against slashes.", 12)
copper_chestplate = Armour("Coppr Chestplate", 7, "It looks like it's made from lava.", 15)
copper_suit = Armour("Copper Suit", 9, "Copper covers your full body.", 20)
steel_armour = Armour("Steel Armour", 10, "It is very heavy, giving a menacing look to anyone who wears it", 25)

stick = Weapon("Stick", 1, "Loved by many dogs.", 1)
wooden_sword = Weapon("Wooden Sword", 2, "Pretty sharp but not very durable.", 3)
lance = Weapon("Lance", 3, "The only thing missing is a horse.", 5)
silver_dagger = Weapon("Silver Dagger", 4, "Small but very agile.", 7)
bone_spear = Weapon("Bone Spear", 4, "Like a true caveman.", 8)
steel_gauntlets = Weapon("Steel Gauntlets", 5, "Good if you like to punch monsters to death.", 10)
twin_blades = Weapon("Twin Blades", 6, "Two is always better than one.", 12)
bow = Weapon("Bow", 7, "Carved with little vines and leaves.", 15)
longsword = Weapon("Longsword", 8, "Heavy and slow, but sturdy.", 20)
warrior_sword = Weapon("Warrior Sword", 9, "Transforms you into a true warrior.", 25)

small_potion = Potion("Small Potion", 10, "Can be used to heal a small amount of health.", 5)
medium_potion = Potion("Medium Potion", 25, "Can be used to heal a medium amount of health.", 10)
big_potion = Potion("Big Potion", 40, "Can be used to heal a big amount of health.", 20)
giant_potion = Potion("Giant Potion", 100, "Can be used to heal a giant amount of health.", 40)

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

all_armour = [
	leather_leggings,
	wooden_chestplate,
	copper_helmet,
	chainmail_shirt,
	copper_chestplate,
	copper_suit,
	steel_armour
]

all_weapons = [
	stick,
	wooden_sword,
	lance,
	silver_dagger,
	bone_spear,
	steel_gauntlets,
	twin_blades,
	bow,
	longsword,
	warrior_sword
]

all_potions = [
	small_potion,
	medium_potion,
	big_potion,
	giant_potion
]
