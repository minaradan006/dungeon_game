import random
import time
import textwrap
from hero import Character, Gold
from story import print_choices
from items import all_loot

lily_the_tiger = r"""
 /_/___/__________/_____________/______________\_____________\_____________\_\
/_/____/_________/_____________/________________\______________\____________\_\
|  |     ,\/~~\_                       _/~~~\         ||                 |||  |
|  |     | ---, `\_    ___,--~ \__   /~' ,,'' |       ||                 |||  |
|  |     |`~`, ',,\`-~~--___---    - /, ,--/'/'       ||                 |||  |
|  |      `\_|\ _\`    ___-~~~\  ,_   '\_/' /'        ||_________________|||  |
|  |        \,_|   , '~,/'\ ,_  `\_\ \_  \_\'         |                   ||  |
|  |      /@@ _/  /' ./',            \       `@,      |    Lily's Shop    ||  |
|  |      @@ '   |  ___/ / /\ \ '\__ _`~|, `, @@      |  of Curious Goods ||  |
|  |    /@@ /  | | ',_-_  |    | ,,_-_,  |  | `@@,    |     and Stuff     ||  |
|  |    @@@ \  | | \ \_O`\ |   / / O_/' | \  \ @@@    |___________________||  |
|  |    @@@ |  | `| '   ~ /     \ ~    /  |    @@@                         |  |
|  |    `@@ |   \ `\     `|     | |  _/'  /'  | @@'                        |  |
|  |     @@ |    ~\ /--'~  | , |  \__   |   | |@@                          |  |
|  |     @@, \     | ,,|   |___|   | `\     /',@@                          |  |
|  |       `@@@_,---::::::=\,| /_=:::::''''''    `                         |  |
|  |       ,/~~_---'_,-___  _  ' -~~~\_```---                              |  |
|  |         ~`   ~~_/'/,--~\_/ ', |\_                                     |  |
|  |              /' \`@@@@@,,@@@@  / \                                    |  |
|  |                     ._      _.                                        |  |
|  |                    /  `"''"`  \                                       |  |
|  |           ..----""`'-..____..-'`""----..                              |  |
|  |          / `\                        /` \                             |  |
|  |         /`   |                      |   `\                            |  |
|__|________/______|_____________________|_____\___________________________|__|
"""

def shop(character: Character, first_shop: bool):
	print(textwrap.fill("From the back corner of the room, you hear jazz music playing.", 70) + "\n")
	time.sleep(3)

	print(textwrap.fill("You slowly approach the music which seems to be played by a live band, the saxophones as clear as a bird's song.", 70) + "\n")
	time.sleep(5)

	print(textwrap.fill("A soft, twinkling light is coming from the corner, almost like a sunset in summer.", 70) + "\n")
	time.sleep(3)

	print("    'Hey there!!'\n")
	time.sleep(3)

	if first_shop:
		print("    'Hello..?', you say trying to focus on the face of the speaker.\n")
		time.sleep(3)

		print("Standing behind a shop booth you see a...tiger?\n")
		time.sleep(3)

