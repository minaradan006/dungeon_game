import random
import time
import textwrap
from game.entities.adventurer import Character
from game.assets.items import Weapon, Armour, Potion
from game.rooms.rooms import Room
from game.core.story import show_start_screen, begin_story, end_story
from game.core.scenarios  import scenario_1, scenario_2, scenario_3
from game.rooms.enemy_room import enemy
from game.rooms.treasure_room import treasure
from game.rooms.empty_room import empty
from game.rooms.trap_room import trap
from game.rooms.shop_room import shop
from game.rooms.boss_room import boss

def fainted():
	print(textwrap.fill("You open your eyes and see the faint sunlight streaming through the tree leaves.", 70) + "\n")
	time.sleep(3)

	print(textwrap.fill("The dungeon entrace is open, ready for you to try again.\n", 70) + "\n")
	time.sleep(3)

	return

def enter_room(room: Room, character: Character, level: int, first_shop: list):
	print("-" * 70 + "\n")
	time.sleep(1)

	print(f"You enter the {room.desc} and look around." + "\n")
	time.sleep(3)

	print(textwrap.fill(room.entry, 70) + "\n")
	time.sleep(8)

	print(textwrap.fill(room.adj, 70) + "\n")
	time.sleep(5)

	if room.event == "enemy":
		if not enemy(character, level, room.monster):
			fainted()

	if room.event == "treasure":
		treasure(character)

	if room.event == "empty":
		empty(character)

	if room.event == "trap":
		if not trap(character):
			fainted()

	if room.event == "shop":
		shop(character, first_shop)

	print(textwrap.fill(room.exit, 70) + "\n")
	time.sleep(5)

	print("You decide to leave the room.\n")
	time.sleep(3)

	print("-" * 70 + "\n")
	time.sleep(1)

def start_game():
	show_start_screen()

	name, attack, defense = begin_story()
	character = Character(name, attack, defense)

	first_shop = [True, True, True]
	for level in range(1, 5):
		print("=" * 70)
		print(f"LEVEL {level}".center(70))
		print("=" * 70 + "\n")
		time.sleep(1)

		mini_stages = random.choice([2, 3, 4])

		for mini in range(0, mini_stages):
			scenario = random.choice([1, 2, 3])

			room = None
			if scenario == 1:
				room = scenario_1(character, level)
			elif scenario == 2:
				room =  scenario_2(character, level)
			elif scenario == 3:
				room = scenario_3(character, level)

			enter_room(room, character, level, first_shop)

		print("You reach a torchlit corridor.\n")
		time.sleep(2)

		print(textwrap.fill("Slowly you walk towards the end and see a ladder that gets you to the next level of the dungeon.", 70) + "\n")
		time.sleep(4)

		print(textwrap.fill("Before touching the wooden boards, an aura of light envelops you for a moment in a calm embrace of pure happiness.", 70) + "\n")
		time.sleep(4)

		print("Suddenly you feel at peace.\n")
		time.sleep(2)

		print("Your health has been restored.\n")
		time.sleep(2)

		character.health = character.max_health

		print("You climb the ladder and go further into the dungeon.\n")
		time.sleep(3)

		print("-" * 70 + "\n")

	print("=" * 70)
	print("LEVEL 5".center(70))
	print("=" * 70 + "\n")
	time.sleep(1)

	if not boss(character):
		fainted()

	end_story(character)
