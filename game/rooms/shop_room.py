import random
import time
import textwrap
from game.entities.adventurer import Character
from game.core.story import print_choices
from game.assets.items import Potion,  all_weapons, all_armour, all_potions
from game.core.scenarios import print_inventory
from game.entities.shopkeepers import Shopkeeper, weapon_weights, armour_weights, potion_weigths, lila_sprite, lila_desc, lila_dialogue, kawa_sprite, kawa_desc, kawa_dialogue, georgianna_sprite, georgianna_desc, georgianna_dialogue

def shop(character: Character, first_shop: list):
	print(textwrap.fill("From the back corner of the room, you hear jazz music playing.", 70) + "\n")
	time.sleep(3)

	print(textwrap.fill("You slowly approach the music which seems to be played by a live band, the saxophones as clear as a bird's song.", 70) + "\n")
	time.sleep(5)

	print(textwrap.fill("A soft, twinkling light is coming from the corner, almost like a sunset in summer.", 70) + "\n")
	time.sleep(3)

	print("???: Hey there!!\n")
	time.sleep(3)

	print(f"{character.name}: Hello..?\n")
	time.sleep(3)

	print("You try to focus on the face of the speaker.\n")
	time.sleep(3)

	lila = Shopkeeper("Lila", "tiger", "Lila's Shop of Sharp Objects", lila_sprite, lila_desc, all_weapons, weapon_weights, lila_dialogue)
	kawa = Shopkeeper("Kawa", "bear", "Kawa's Shop of Sweet Healing", kawa_sprite, kawa_desc, all_potions, potion_weigths, kawa_dialogue)
	georgianna = Shopkeeper("Georgianna", "fox", "Georgianna's Shop of Shiny Protection", georgianna_sprite, georgianna_desc, all_armour, armour_weights, georgianna_dialogue)

	shopkeeper = random.choice([lila, kawa, georgianna])

	shop = 0
	if shopkeeper.name == "Lila":
		shop = 0
	elif shopkeeper.name == "Kawa":
		shop = 1
	else:
		shop = 2

	if first_shop[shop]:
		print(f"Standing behind a shop booth you see a...{shopkeeper.species}?\n")
		time.sleep(3)

		print(shopkeeper.sprite)
		time.sleep(5)

		print(f"{shopkeeper.name}: I'm {shopkeeper.name} and this is {shopkeeper.shop_name}!\n")
		time.sleep(3)

		print(textwrap.fill(f"{shopkeeper.name}: {shopkeeper.desc}", 70) + "\n")
		time.sleep(5)
	else:
		print(shopkeeper.sprite)
		time.sleep(1)

		print(f"{character.name}: Oh, hi {shopkeeper.name}!\n")
		time.sleep(3)

	print(f"{shopkeeper.name}: Here is what I have for you at the moment:\n")
	time.sleep(3)

	for item in shopkeeper.stock:
		price = (item.buy_price * shopkeeper.price_multiplier) // 100
		print(f"{item} -> {price} gold")
		time.sleep(1)

	print()

	while True:
		print("What will you do?")
		time.sleep(2)

		choices = ["Buy", "Sell", "Check coins", "Talk", "Leave"]
		print_choices(choices)

		choice = input()
		print()

		if choice.lower() == "buy":
			while True:
				for item in shopkeeper.stock:
					if isinstance(item, str) == True:
						print(item)
						time.sleep(1)
						continue

					price = (item.buy_price * shopkeeper.price_multiplier) // 100
					print(f"{item} -> {price} gold")
					time.sleep(1)

				print("[Back]\n")

				print("What do you want to buy?")
				time.sleep(1)

				item_buy = input().lower()

				if item_buy == "back":
					break

				shopkeeper.buy(character, item_buy)
		elif choice.lower() == "sell":
			while True:
				print_inventory(character)
				print("What type of item would you like to sell?")
				time.sleep(1)

				choices = ["Weapons", "Armour", "Health Potions", "Back"]
				print_choices(choices)

				category = input().lower()
				print()

				if category == "back":
					break

				if category not in ["weapons", "armour", "health potions"]:
					print("Not a valid category.\n")
					time.sleep(1)
					continue
				while True:
					for item in character.inventory[category]:
						price = item.sell_price * shopkeeper.price_multiplier // 100
						print(f"[{item.name}] : {price} gold")
						time.sleep(1)
					print("[Back]\n")

					print("What do you want to sell?")
					time.sleep(1)

					item_sell = input().lower()
					print()

					if item_sell == "back":
						break

					shopkeeper.sell(character, item_sell, category)
		elif choice.lower() == "check coins":
			print(f"Gold: {character.gold}\n")
			time.sleep(1)
		elif choice.lower() == "talk":
			print(shopkeeper.sprite)
			shopkeeper.talk()
		elif choice.lower() == "leave":
			print(f"{shopkeeper.name}: Let me just open the next room for you...\n")
			time.sleep(2)

			print(f"{shopkeeper.name}: See you next time!\n")
			time.sleep(2)

			print(f"{character.name}: Bye, {shopkeeper.name}!\n")
			time.sleep(2)

			first_shop[shop] = False

			return
		else:
			print("Invalid choice. Try again.\n")
			time.sleep(2)
			continue

		print(70 * "-" + "\n")
