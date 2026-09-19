import random
import time
import textwrap
from hero import Character
from story import print_choices
from items import all_weapons, all_armour, all_potions

class Animal:
	def __init__(self, name: str, species: str, shop_name: str, sprite: str, desc: str, stock: list, stock_weights: list, dialogue: list):
		self.name = name
		self.species = species
		self.shop_name = shop_name
		self.sprite = sprite
		self.desc = desc
		self.stock = random.choices(stock, weights=stock_weights, k=3)
		self.dialogue = dialogue

	def talk(self):
		for line in self.dialogue:
			print(textwrap.fill(f"{self.name}: {line}", 70) + "\n")
			time.sleep(5)

lila_sprite = r"""
 /_/___/__________/_____________/______________\_____________\_____________\_\
/_/____/_________/_____________/________________\______________\____________\_\
|  |                                                  ||                 |||  |
|  |                                                  ||                 |||  |
|  |      ,\/~~\_                       _/~~~\        ||                 |||  |
|  |      |---, `\_    ___,--~ \__   /~' ,,'' |       ||                 |||  |
|  |      `\_|\ _\`    ___-~~~\  ,_   '\_/' /'        ||_________________|||  |
|  |        \,_|   , '~,/'\ ,_  `\_\ \_  \_\'         |                   ||  |
|  |      /@@ _/  /' ./',            \       `@,      |    Lila's Shop    ||  |
|  |      @@ '   |  ___/ / /\ \ '\__ _`~|, `, @@      |      of Sharp     ||  |
|  |    /@@ /  | | ',_-_  |    | ,,_-_,  |  | `@@,    |      Objects      ||  |
|  |     @@@ \ | | \ \_O`\ |   / / O_/' | \  \@@@     |___________________||  |
|  |    `@@ |   \ `\     `|     | |  _/'  /'  | @@'                        |  |
|  |      @@ |   ~\ /--'~  | , |  \__   |   | |@@                          |  |
|  |      @@,\     | ,,|   |___|   | `\    /',@@                           |  |
|  |       `@@@_,---::::::=\,| /_=:::::''''''    `                         |  |
|  |       ,/~~_---'_,-___  _  ' -~~~\_```---                              |  |
|  |         ~`   ~~_/'/,--~\_/ ', |\_                                     |  |
|  |              /' \`@@@@@,,@@@@  / \                                    |  |
|  |                     ._      _.                                        |  |
|  |                    /  `"''"`  \                                       |  |
|  |         ..----''""`'-..____..-'`''""----..                            |  |
|  |        / `\                            /` \                           |  |
|__|_______/____|__________________________|____\__________________________|__|
"""

weapon_weights = [1, 1, 2, 2, 2, 1, 1, 0.25, 0.25, 0.1]

lila_desc = "Here at my shop you can find a variety of weapons that you can buy, but you can also sell your stuff if you please."

lila_dialogue = [
	"So here's a tip from me.",
	"You might assume that [enemy] rooms are just annoying, but think again.",
	"From the monsters you fight you can gain some pretty awesome stuff.",
	"For example, from [The Wise Owl] in the [library], [The Skeleton Pirate] in the [crypt], [The Axed Orc] in the [corridor] and [The Rose Assassin] in the [garden] you can get some pretty sick weapons.",
	"Don't tell them I spoke to you of this though.",
	"I want to stay on their good side, you understand, right?"
]

kawa_sprite = r"""
 /_/___/__________/_____________/______________\_____________\_____________\_\
/_/____/_________/_____________/________________\______________\____________\_\
|  |                                                  ||                 |||  |
|  |                                                  ||                 |||  |
|  |                                                  ||                 |||  |
|  |             .--.              .--.               ||_________________|||  |
|  |            : (\ ". _......_ ." /) :              |                   ||  |
|  |             '.    `        `    .'               |    Kawa's Shop    ||  |
|  |              /'   _        _   `\                |     of Sweet      ||  |
|  |             /      0}    {0     \                |      Healing      ||  |
|  |            |       /      \       |              |___________________||  |
|  |            |     /'        `\     |                                   |  |
|  |             \   | .  .==.  . |   /                                    |  |
|  |              '._ \.' \__/ './ _.'                                     |  |
|  |              /  ``'._-''-_.'``  \                                     |  |
|  |             /                    \                                    |  |
|  |           .'.      ""            .'.                                  |  |
|  |          /\ \                    / /\                                 |  |
|  |        .'  | |            ""     | | '.                               |  |
|  |       .    '. '....._______.....' .'"  .                              |  |
|  |      .      |                     |     .                             |  |
|  |      ' ""    |    ___________    |      '                             |  |
|  |      '       |    |         |    |  ""  '                             |  |
|  |      .   ""  |    :         :    |      .                             |  |
|__|______'_______|_____\_______/_____|______'_____________________________|__|
"""

potion_weigths = [5, 2, 1, 0.5]

kawa_desc = "Here at my shop you can find the most delicious and powerful healing items for sale, but also I can buy stuff from you too."

kawa_dialogue = [
	"There is one pretty important thing you should know about the enemy rooms.",
	"If you decide to take the risk and fight the monster within them, the reward is pretty neat.",
	"The one that I like the most is the item dropped by [The Eye] in the [hallway].",
	"This item has a fascinating effect on the being who drinks it.",
	"I sure hope I can experience it for myself someday..."
]

georgianna_sprite = r"""
 /_/___/__________/_____________/______________\_____________\_____________\_\
/_/____/_________/_____________/________________\______________\____________\_\
|  |                                                  ||                 |||  |
|  |                                                  ||                 |||  |
|  |                                                  ||                 |||  |
|  |                                                  ||_________________|||  |
|  |               *.               .*                |                   ||  |
|  |              "  *.           .*  "               |    Georgianna's   ||  |
|  |             ." " "'    .    '" " ".              |   Shop of Shiny   ||  |
|  |             '  ""  ";.":".;"  ""  '              |     Protection    ||  |
|  |             `. "'"           "'" .`              |___________________||  |
|  |              .*'' ..       .. ''*.                                    |  |
|  |           ..-       `     `       -..                                 |  |
|  |          --_*   '---.     .---'   *_--                                |  |
|  |             -_       `   `        _-                                  |  |
|  |               `.__.          .__.`                                    |  |
|  |              ,.' \`'.  @  .`'/  '..                                   |  |
|  |            .'  --_`  \___/   `._-- ".                                 |  |
|  |           ' "     '.        .`       :                                |  |
|  |           '.   "    `,   ."   "*    .'                                |  |
|  |            /'.    *" '.  "      `." \                                 |  |
|  |           :  ".       ..' "*    *    :                                |  |
|  |          .     '.,    '"     ."   "   .                               |  |
|  |          '  ""    '.  "   ."     *   '                                |  |
|__|__________:___________._:__.___________:_______________________________|__|
"""

armour_weights = [1, 1, 2, 2, 1, 0.25, 0.25]

georgianna_desc = "Here at my shop you can dress up with the most dazzling armour, but I accept anything that you want to sell."

georgianna_dialogue = [
	"Seeing as you're unfamiliar with this dungeon, I shall offer my assistance.",
	"If you have the courage to face the [enemy] rooms, you have the chance to obtain items that will aid you later.",
	"In terms of armour, you can obtain it from [The Rat King] in the [dungeon cell], from [The Knight] in the [armory] and from [The Glowing Moth] in the [chamber].",
	"These items will protect you greatly, if you choose to face the monsters.",
	"I'd say it's pretty worth it, wouldn't you?"
]

lila = Animal("Lila", "tiger", "Lila's Shop of Sharp Objects", lila_sprite, lila_desc, all_weapons, weapon_weights, lila_dialogue)
kawa = Animal("Kawa", "bear", "Kawa's Shop of Sweet Healing", kawa_sprite, kawa_desc, all_potions, potion_weigths, kawa_dialogue)
georgianna = Animal("Georgianna", "fox", "Georgianna's Shop of Shiny Protection", georgianna_sprite, georgianna_desc, all_armour, armour_weights, georgianna_dialogue)

person = Character("Mina", 10, 10)

def shop(character: Character, first_shop: bool):
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

	animal = random.choice([lila, kawa, georgianna])

	if first_shop:
		print(f"Standing behind a shop booth you see a...{animal.species}?\n")
		time.sleep(3)

		print(animal.sprite)
		time.sleep(5)

		print(f"{animal.name}: I'm {animal.name} and this is {animal.shop_name}!\n")
		time.sleep(3)

		print(textwrap.fill(f"{animal.name}: {animal.desc}", 70) + "\n")
		time.sleep(5)
	else:
		print(f"{character.name}: Oh, hi {animal.name}!\n")

	print(f"{animal.name}: Here is what I have for you at the moment:\n")
	time.sleep(3)

	for item in animal.stock:
		print(item)
		time.sleep(1)

	print()

	while True:
		print("What will you do?\n")
		time.sleep(2)

		choices = ["Buy", "Sell", "Talk", "Leave"]
		print_choices(choices)

		choice = input()
		print()

		if choice.lower() == "buy":
			pass
		elif choice.lower() == "sell":
			pass
		elif choice.lower() == "talk":
			print(animal.sprite)
			animal.talk()
		elif choice.lower() == "leave":
			print(f"{animal.name}: See you next time!\n")
			time.sleep(2)

			print(f"{character.name}: Bye, {animal.name}!\n")
			time.sleep(2)

			return
		else:
			print("Invalid choice. Try again.\n")
			time.sleep(2)
			continue

		print(70 * "-" + "\n")

shop(person, True)
