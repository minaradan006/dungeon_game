import time
import textwrap
from game.entities.adventurer import Character

def show_start_screen():
	time.sleep(0.5)

	print("\n")
	print(r"""
	          ______          \'/                                .
	      .-'` .    `'-.    -= * =-                          .   :   .
	    .'  '    .---.  '.    /.\                        '.   .  :  .   .'
	   /  '    .'     `'. \                           ._   '._.-'''-._.'   _.
	  ;  '    /          \|                             '-..'         '..-' 
	 :  '  _ ;            `             THE          --._ /.==.     .==.\ _.--
	;  :  /(\ \                       DUNGEON            ;/_o__\   /_o__\;
	|  .       '.                    OF SHADOW      -----|`     ) (     `|-----
	|  ' /     --'                   AND LIGHT          _: \_) (\_/) (_/ ;_
	|  .   '.__\                                     --'  \  '._.=._.'  /  '--
	;  :       /                                       _.-''.  '._.'  .''-._
	 ;  .     |            ,                          '    .''-.(_).-''.    '
	  ;  .    \           /|                             .'   '  :  '   '.
	   \  .    '.       .'/                        \'/      '    :   '
	    '.  '  . `'---'`.'                       -= * =-         '
	     `'-..._____.-`                            /.\           '
		 
	""")

	time.sleep(0.5)

	eq_line = "=" * 70
	print(eq_line.center(90))
	time.sleep(0.5)

	print("WELCOME TO THE DUNGEON OF SHADOW AND LIGHT".center(90))
	time.sleep(0.5)

	print(eq_line.center(90))
	time.sleep(0.5)

	print("Survive 5 levels and win!".center(90))
	time.sleep(0.5)

	line = "-" * 70
	print(line.center(90))
	time.sleep(0.5)

	print("\n" * 1)
	input("Press [Enter] to begin your adventure...")
	print("\n" * 1)
	time.sleep(0.5)

def begin_story() -> Character:
	print(textwrap.fill("The Book of Light is an ancient relic that is found at the end of The Dungeon of Shadow and Light.", width=70))
	print()
	time.sleep(3)

	print(textwrap.fill("It is said that only the strongest and wisest of men can complete the gauntlet of challenges inside the dungeon.", width=70))
	print()
	time.sleep(3)

	print(textwrap.fill("You make your way through The Forest of Wishes and reach the vine covered entrance.\n", width=70))
	print()
	time.sleep(3)

	print(textwrap.fill("There's some writing etched into the smooth stone door:\n", width=70))
	print()
	time.sleep(3)

	print(textwrap.fill("'To pass this door, one must state their name followed by their power.'\n", width=70))
	print()
	time.sleep(3)

	print(textwrap.fill("You remember reading in The Book of Dungeons that power means attack and defense. Their sum must be 20.\n", width=70))
	print()
	time.sleep(3)

	print(textwrap.fill("Hesitantly, you open your mouth and utter the three words.\n", width=70))
	print()
	time.sleep(2)

	name = input("What is your name? ")

	while True:
		attack = int(input("What is your attack stat? "))
		defense = int(input("What is your defense stat? "))
		print()

		if attack + defense == 20:
			print(textwrap.fill("The door rumbles and slowly lowers itself into the ground.\n", width=70))
			print()
			time.sleep(3)

			print(textwrap.fill("As a cold wind escapes the dungeon, you push past the creeping vines and enter through the opening.\n", width=70))
			print()
			time.sleep(3)

			print(textwrap.fill("The heavy door instantly seals itself behind you.\n", width=70))
			print()
			time.sleep(2)

			print("The challenge has begun!\n")
			print()
			time.sleep(2)

			return name, attack, defense
		else:
			print(textwrap.fill("The sum of the attack stat and the defense stat should be 20. Try again.\n", width=70))
			print()

def print_choices(valid_choices: list):
	for choice in valid_choices:
		print(f"[{choice}]", end="  ")
	print()

def end_story(character: Character):
	print("You did it!\n")
	time.sleep(3)

	print("The Shadow Dragon stares at you without saying anything.\n")
	time.sleep(4)

	print("You can hear the sound of crikets singing and of leaves rustling.\n")
	time.sleep(4)

	print("The Shadow Dragon: Well done, adventurer...\n")
	time.sleep(4)

	print("The Shadow Dragon: You are worthy indeed...\n")
	time.sleep(4)

	print("Amara: My real name is Amara, The Shadow Dragon.\n")
	time.sleep(4)

	print(textwrap.fill("Amara: I keep it hidden so no one finds me or my sister, The Light Dragon.\n", 70) + "\n")
	time.sleep(5)

	print("Amara: During the battle, I sensed a light inside of you.\n")
	time.sleep(4)

	print("Amara: It's something I have not felt in any being.\n")
	time.sleep(4)

	print("Amara: That is very curious...\n")
	time.sleep(3)

	print("Amara: You earned the right to the magic inside of the Book of Light.\n")
	time.sleep(4)

	print("Amara: Go ahead, take it...\n")
	time.sleep(3)

	print("Amara: Do not fret, I shall know if the book is in danger.\n")
	time.sleep(4)

	book_of_light = r"""
                      _____________________
                    ,'-,-,-------------.-,'|
                    |==|/ __            \|||
                    |  |  )_)  _  _\/_   |||
                    |  |  )__))_))_)) \  |||
                    |  |          _      |||
                    |  |       _ )_      |||
                    |  |      )_))       |||
                    |  |                 |||
                    |  |   )  . _ )_-)-  |||
                    |  |  /__,))_)) ))   |||
                    |  |        _)       |||
                    |==|\      -=-      /|,'
                    '--'-`-------------'-'
"""

	print(book_of_light)
	time.sleep(0.5)

	print(textwrap.fill("You approach the pedestal and rest your hand on the white cover.", 70) + "\n")
	time.sleep(3)

	print("A feeling of energy but at the same time of calm flows through you.\n")
	time.sleep(4)

	print("You pick it up and put it inside of your bag.\n")
	time.sleep(3)

	print("Amara: I shall now return to my sister, The Light Dragon...Amina.\n")
	time.sleep(4)

	print(textwrap.fill(f"{character.name}: Thank you, Amara, I shall protect this with my soul.", 70) + "\n")
	time.sleep(4)

	print("Amara: I know.\n")
	time.sleep(3)

	print(textwrap.fill("Amara lifts from the ground and flies away into the night sky, resting between the moon and stars.", 70) + "\n")
	time.sleep(4)

	print("The morning sunlight bathes the room once more and the door between the two thrones opens.\n")
	time.sleep(4)

	print("It's time to go home.\n")
	time.sleep(5)

	the_end = r"""
    ===================================================================================
                         _____ _            _____           _ 
                        |_   _| |__   ___  | ____|_ __   __| |
                          | | | '_ \ / _ \ |  _| | '_ \ / _` |
                          | | | | | |  __/ | |___| | | | (_| |
                          |_| |_| |_|\___| |_____|_| |_|\__,_|

    ===================================================================================
"""

	print(the_end)
	time.sleep(5)

	print("Thank you for playing!\n")
	time.sleep(2)
