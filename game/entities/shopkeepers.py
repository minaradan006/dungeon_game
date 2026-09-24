import random
import time
import textwrap
from game.entities.adventurer import Character
from game.assets.items import Potion, all_weapons, all_armour, all_potions
from game.assets.shopkeeper_sprites import lila_sprite, kawa_sprite, georgianna_sprite
from game.core.scenarios import print_inventory

class Shopkeeper:
	def __init__(self, name: str, species: str, shop_name: str, sprite: str, desc: str, stock: list, stock_weights: list, dialogue: list):
		self.name = name
		self.species = species
		self.shop_name = shop_name
		self.sprite = sprite
		self.desc = desc
		self.stock = random.choices(stock, weights=stock_weights, k=3)
		self.price_multiplier = random.choice(range(50, 200, 25))
		self.dialogue = dialogue

	def talk(self):
		for line in self.dialogue:
			print(textwrap.fill(f"{self.name}: {line}", 70) + "\n")
			time.sleep(5)

	def buy(self, character: Character, item_buy: str):
		for idx, item in enumerate(self.stock):
			if isinstance(item, str) == False:
				if item.name.lower() == item_buy:
					price = (item.buy_price * self.price_multiplier) // 100
					if price > character.gold:
						print("You don't have enough gold for this item...\n")
						time.sleep(2)
						return
					else:
						character.gold -= price
						character.receive_item(item)
						self.stock[idx] = "SOLD OUT"

						print(f"\n-{price} gold")
						time.sleep(1)
						print("Item purchased successfully!\n")
						time.sleep(1)
						print(f"{self.name}: Thank you for the purchase!\n")
						time.sleep(1)
						return

		print("There's no item with this name for sale.\n")
		time.sleep(2)

	def sell(self, character: Character, item_sell: str, category: str):
		for idx, item in enumerate(character.inventory[category]):
			if item.name.lower() == item_sell:
				price = (item.sell_price * self.price_multiplier) // 100
				character.gold += price
				if isinstance(item, Potion):
					item.num -= 1
					if item.num == 0:
						del character.inventory[category][idx]
				else:
					del character.inventory[category][idx]

				print(f"+{price} gold\n")
				time.sleep(1)
				print("Item sold successfully!\n")
				time.sleep(1)
				print(f"{self.name}: Thank you for the item!\n")
				time.sleep(1)
				return

		print("There's no item with this name in your inventory.\n")
		time.sleep(2)

weapon_weights = [1, 1, 2, 2, 2, 1, 1, 0.25, 0.25, 0.1]

lila_desc = "Here at my shop you can find a variety of weapons that you can buy, but you can also sell your stuff if you please."

lila_dialogue = [
	"So here's a tip from me.",
	"You might assume that [enemy] rooms are just annoying, but think again.",
	"From the monsters you fight you can gain some pretty awesome stuff.",
	"For example, from [The Wise Owl] in the [library], from [The Skeleton Pirate] in the [crypt], from [The Axed Orc] in the [corridor] and from [The Rose Assassin] in the [garden] you can get some pretty sick weapons.",
	"Don't tell them I spoke to you of this though.",
	"I want to stay on their good side, you understand, right?"
]

potion_weigths = [5, 2, 1, 0.5]

kawa_desc = "Here at my shop you can find the most delicious and powerful healing items for sale, but also I can buy stuff from you too."

kawa_dialogue = [
	"There is one pretty important thing you should know about the enemy rooms.",
	"If you decide to take the risk and fight the monster within them, the reward is pretty neat.",
	"The one that I like the most is the item dropped by [The Eye] in the [hallway].",
	"This item has a fascinating effect on the being who drinks it.",
	"I sure hope I can experience it for myself someday..."
]

armour_weights = [1, 1, 2, 2, 1, 0.25, 0.25]

georgianna_desc = "Here at my shop you can dress up with the most dazzling armour, but I accept anything that you want to sell."

georgianna_dialogue = [
	"Seeing as you're unfamiliar with this dungeon, I shall offer my assistance.",
	"If you have the courage to face the [enemy] rooms, you have the chance to obtain items that will aid you later.",
	"In terms of armour, you can obtain it from [The Rat King] in the [dungeon cell], from [The Knight] in the [armory] and from [The Glowing Moth] in the [chamber].",
	"These items will protect you greatly, if you choose to face the monsters.",
	"I'd say it's pretty worth it, wouldn't you?"
]
