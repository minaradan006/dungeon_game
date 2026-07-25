import time
import textwrap

def show_start_screen():
	time.sleep(0.5)

	print("\n")
	print(r"""
	   \                             /
	   |                             |
	 .'|'.                         .'|'.
	/.'|\ \          THE          /./|'.\
	| /|'.|       OVERGROWN       |.'|\ |
	 \ |\/         DUNGEON         \/| /
	  \/                             \|
	  '                                `
	""")

	time.sleep(0.5)

	eq_line = "=" * 41
	print(eq_line.center(53))
	time.sleep(0.5)

	print("WELCOME TO THE OVERGROWN DUNGEON".center(53))
	time.sleep(0.5)

	print(eq_line.center(53))
	time.sleep(0.5)

	print("Survive 5 levels and win!".center(53))
	time.sleep(0.5)

	line = "-" * 41
	print(line.center(53))
	time.sleep(0.5)

	print("\n" * 1)
	input("Press [Enter] to begin your adventure...")
	print("\n" * 1)
	time.sleep(0.5)

def begin_story():
	print(textwrap.fill("The Book of Light is an ancient relic that is found at the end of the Overgrown Dungeon.", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("It is said that only the strongest and wisest of men can complete the gauntlet of challenges inside the dungeon.", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("You make your way through The Forest of Wishes and reach the vine covered entrance.\n", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("There's some writing etched into the smooth stone door:\n", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("'To pass this door, one must state their name followed by their power.'\n", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("You remember reading in The Book of Dungeons that power means attack and defense. Their sum must be 20.\n", width=60))
	print()
	time.sleep(3)

	print(textwrap.fill("Hesitantly, you open your mouth and utter the three words.\n", width=60))
	print()
	time.sleep(2)

	name = input("What is your name? ")

	while True:
		attack = int(input("What is your attack stat? "))
		defense = int(input("What is your defense stat? "))
		print()

		if attack + defense == 20:
			print(textwrap.fill("The door rumbles and slowly lowers itself into the ground.\n", width=60))
			print()
			time.sleep(3)

			print(textwrap.fill("As a cold wind escapes the dungeon, you push past the creeping vines and enter through the opening.\n", width=60))
			print()
			time.sleep(3)

			print(textwrap.fill("The heavy door instantly seals itself behind you.\n", width=60))
			print()
			time.sleep(2)

			print("The challenge has begun!\n")
			print()
			time.sleep(2)

			return name, attack, defense
		else:
			print(textwrap.fill("The sum of the attack stat and the defense stat should be 20. Try again.\n", width=60))
			print()

def print_choices(valid_choices):
	for choice in valid_choices:
		print(f"[{choice}]", end="  ")
	print()