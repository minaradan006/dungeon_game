import random
import time
import textwrap
from hero import Character, Gold
from story import print_choices
from items import all_weapons, all_armour, all_potions

class Animal:
	def __init__(self, name: str, species: str, shop_name: str, sprite: str, desc: str, stock: list, stock_weights: list):
		self.name = name
		self.species = species
		self.shop_name = shop_name
		self.sprite = sprite
		self.desc = desc
		self.stock = random.choices(stock, weights=stock_weights, k=3)

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
|  |             /      0}    {0     \               |      Healing      ||  |
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
|  |          --_*   '---.     .---'    *_--                               |  |
|  |             -_       `   `        _-                                  |  |
|  |               `.__.          .__.`                                    |  |
|  |              ,.' \`'.  @  .`'/  '..                                   |  |
|  |            .'  --_   \___/   `._-- ".                                 |  |
|  |           ' "     '.        .`       :                                |  |
|  |           '.   "    `,   ."   "*    .'                                |  |
|  |            /'.    *" '.  "      `." \                                 |  |
|  |           :  ".       ..' "*    *    :                                |  |
|  |          .     '.,    '"     ."   "   .                               |  |
|  |          '  ""    '.  "   ."     *   '                                |  |
|__|__________:___________._:__.___________:_______________________________|__|
"""

print(georgianna_sprite)

lila = Animal("Lila", "tiger", "Lila's Shop of Sharp Objects", lila_sprite, "Here at my shop you can find a variety of weapons that you can buy, but you can also sell your stuff if you please.", all_weapons, [1, 1, 2, 2, 2, 1, 1, 0.25, 0.25, 0.1])
kawa = Animal("Kawa", "bear", "Kawa's Shop of Sweet Healing", kawa_sprite, "Here at my shop you can find the most delicious and powerful healing items for sale, but also I can buy stuff from you too.", all_potions, [1, 1, 2, 2, 1, 0.25, 0.25])
georgianna = Animal("Georgianna", "fox", "Georgianna's Shop of Shiny Protection", georgianna_sprite, "Here at my shop you can dress up with the most dazzling armour, but I accept anything that you want to sell.", all_armour, [5, 2, 1, 0.5])

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

	print("{animal.name}: Here is what I have for you:\n")
	time.sleep(3)




