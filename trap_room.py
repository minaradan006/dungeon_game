import random
import time
import textwrap
from hero import Character
from story import print_choices

d20 = r"""
                         _
                    _.'`/\ `-._     .+
                  .' 2 /  \ 14 /`     .
                 /1\  / 20 \  . .
          .      ._2\/______\/ 6.
          +.      \10`\     /`._|
                   `._ \ 8 /16.'
                       ``v`'
"""

def trap(character: Character):
	print(textwrap.fill("The room seems quiet, nothing out of the ordinary.", 70) + "\n")
	time.sleep(3)

	print(textwrap.fill("You take one step forward, the floor sinking under your foot.", 70) + "\n")
	time.sleep(3)

	print("It's a trap!\n")
	time.sleep(3)

	print(textwrap.fill("Cage walls fall from the ceiling around you and a table emerges from the floor.", 70) + "\n")
	time.sleep(5)

	print(d20)
	print(textwrap.fill("There is a glittering 20-sided die and a small inscription on the table.", 70) + "\n")
	time.sleep(5)

	print("'Get at least 10 and you're safe...'\n")
	time.sleep(3)

	print("'Get less and...'\n")
	time.sleep(3)

	print("The message doesn't continue.\n")
	time.sleep(3)

	print("You pick up the dice.\n")
	time.sleep(3)

	print("You hesitantly throw it on the table and roll a...\n")
	time.sleep(3)

	roll = random.choice(range(1, 20))

	print(roll)

	if roll >= 10:
		print("You are safe!\n")
		time.sleep(3)

	else:
		print(textwrap.fill("Before the dread can kick in, you hear a whoosh sound coming from behind you", 70) + "\n")
		time.sleep(3)

		print("An arrow shoots you in the shoulder and damages you 20 HP points.\n")
		time.sleep(3)

		character.health -= 20

		if character.health <= 0:
			return False

	print("The cage walls go back up in the ceiling and you are free to leave.\n")
	return True
