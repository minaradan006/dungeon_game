import textwrap
import time
import random
from hero import Character, Gold
from items import Weapon, Armour, Potion
from monsters import Monster, shadow_dragon
from story import print_choices

fight_messages = [
	"The Shadow Dragon's dark blue eyes glow brighter as it glares at you.",
	"Indigo blood oozes out of The Shadow Dragon's wounds.",
	"A puff of blue smoke escaped The Shadow Dragon's nostrils.",
	"The walls and floor of the room rumble, flecks of dust floating about.",
	"A lilac haze covers the room.",
	"The light blue flames disappear, turning the room to pitch black for a few seconds.",
	"A few small flames float around The Shadow Dragon."
]

def boss(character: Character, boss: Monster):
	print(textwrap.fill("You step off the ladder and you dust yourself off from all that you have been through in The Dungeonof Shadow and Light.") + "\n")
	time.sleep(3)

	print(textwrap.fill("You feel tired but at the same time the strongest you have ever been.", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("The room looks like the ruins of a castle.", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("The silver and golden banners are torn and stone bricks are missing from the walls.", 70)  + "\n")
	time.sleep(2)

	print("Two thrones rest at the back of the room.\n")
	time.sleep(2)

	print(textwrap.fill("A throne made of blue sapphire gems and a throne made of white opal gems.", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("The gleaming sunlight shines upon you through the open ceiling of the room.\n", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("Brigther than the sun beams, the Book of Light stands in the center of the room on a marble pedestal, adorned with gold and diamonds.", 70) + "\n")
	time.sleep(4)

	print(textwrap.fill("You take one step forward, but suddenly the daylight turns into darkness.", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("The torches on the walls of the room light up with light blue flames which look like spirits.", 70) + "\n")
	time.sleep(2)

	print("???: I see you have reached the final level of the challenge...\n")
	time.sleep(2)

	print("???: You are certainly one courageous adventurer...\n")
	time.sleep(2)

	print("???: Maybe you just don't know what you are doing...\n")
	time.sleep(3)

	print(f"{character.name}: Who are you? Show yourself!\n")
	time.sleep(2)

	print(textwrap.fill("From the night sky a gigantic figure floats down, almost like it came from behind the moon.", 70) + "\n")
	time.sleep(3)

	dragon = r"""
					  __
				  _.-'.-'-.__
			   .-'.       '-.'-._ __.--._
		-..'\,-,/..-  _         .'   \   '----._
		 ). /_ _\' ( ' '.         '-  '/'-----._'-.__
		 '.\'. .'/.'     '-r   _      .-.       '-._ \
		 '.\. Y .).'       ( .'  .      .\          '\'.
		 .-')'|'/'-.        \)    )      '',_      _.c_.\
		   .<, ,>.          |   _/\        . ',   :   : \\
		  .' \_/ '.        /  .'   |          '.     .'  \)
						  / .-'    '-.        : \   _;   ||
						 / /    _     \_      '.'\ ' /   ||
						/.'   .'        \_      .|   \   \|
					   / /   /      __.---'      '._  ;  ||
					  /.'  _:-.____< ,_           '.\ \  ||
					 // .-'     '-.__  '-'-\_      '.\/_ \|
					( };====.===-==='        '.    .  \\: \
					 \\ '._        /          :   ,'   )\_ \
					  \\   '------/            \ .    /   )/
					   \|        _|             )Y    |   /
						\\      \             .','   /  ,/
						 \\    _/            /     _/
						  \\   \           .'    .'
						   '| '1          /    .'
							 '. \        |:    /
							   \ |       /', .'
								\(      ( ;z'
								 \:      \ '(_
								  \_,     '._ '-.___
											  '-' -.\
	"""
	print(dragon)

	print("The dragon's eyes look as if they are lit up by a dim dark blue flame.\n")
	time.sleep(2)

	print("Its gigantic wings create a strong wind that blows you backwards.\n")
	time.sleep(2)

	print("It is as majestic as it is scary.\n")
	time.sleep(2)

	print(textwrap.fill("The Shadow Dragon: My name is The Shadow Dragon and I have been watching you in the dungeon.", 70) + "\n")
	time.sleep(3)

	print(textwrap.fill("The Shadow Dragon: I am the guardian of the Book of Light.", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("The Shadow Dragon: Only the most worthy can become the bearer of the magic contained inside of it.", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("The Shadow Dragon: So let us see if that person is you... Brave adventurer...", 70) + "\n")
	time.sleep(3)

	print(boss.sprite)
	time.sleep(1)

	print("-" * 70)
	print(boss.name + f"({boss.health} HP, {boss.attack} ATK)")
	print("-" * 70 + "\n")
	time.sleep(2)

	print()

	half = False
	while True:
		if character.health <= 0:
			print("You fainted...\n")
			time.sleep(5)
			return False

		print("What will you do?")
		time.sleep(0.5)

		choices = ["Attack", "Heal", "Check stats", "Check boss"]
		print_choices(choices)

		choice = input()
		print()

		if choice.lower() == "check stats":
			print("STATS".center(40, "=") + "\n")
			print(character)
			continue
		elif choice.lower() == "check ":
			print(boss)
			continue
		elif choice.lower() == "heal":
			print("Health Potions".center(20, "-") + "\n")
			time.sleep(0.5)

			for item in character.inventory["health potions"]:
				print(item)
				time.sleep(0.5)
			print("[Back]\n")
			time.sleep(0.5)

			potion_name = input("What potion do you want to use? ")
			print()

			if potion_name.lower() == "back":
				continue

			character.heal(potion_name)
		elif choice.lower() == "attack":
			print(f"You decide to attack [{boss.name}].\n")
			time.sleep(3)
			boss.damage_taken(character)
			if boss.health <= 100 and not half:
				boss.attack *= 2

				print(textwrap.fill("The Shadow Dragon is panting and it drops to the floor, landing with a thud.", 70) + "\n")
				time.sleep(2)

				print(textwrap.fill("The Shadow Dragon: You are much stronger than I thought...", 70) + "\n")
				time.sleep(2)

				print(textwrap.fill("The Shadow Dragon: Let's make this more interesting...", 70) + "\n")
				time.sleep(2)

				print("The Shadow Dragon's attack has doubled!\n")
				time.sleep(1)

				half = True

			if boss.health <= 0:
				print("=" * 70 + "\n")
				print(f"You defeated [{boss.name}]!\n")
				print("=" * 70 + "\n")
				time.sleep(5)

				return True

			print("-" * 70 + "\n")
			print(random.choice(fight_messages))
			print("-" * 70 + "\n")
			time.sleep(3)
		else:
			print("Invalid choice. Try again.\n")
			time.sleep(2)
			continue

		boss.attack_character(character)
		print("-" * 70 + "\n")