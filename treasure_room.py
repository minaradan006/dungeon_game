import random
import time
import textwrap
from hero import Character
from story import print_choices

class Chest:
	def __init__(self, name: str, locks: int, loot: list):
		self.name = name
		self.locks = locks
		self.loot = loot

	def unlock(self, character: Character) -> bool:
		if character.lockpicks < self.locks:
			print("You don't have enough lockpicks...\n")
			time.sleep(2)
			return False

		character.lockpicks -= self.locks
		print("You successfully opened the chest and received...\n")
		num_items = random.choices(
		[1, 2, 3], weights=[0.7, 0.2 + self.locks / 10, 0.1 + self.locks / 10],
		)[0]

		

def treasure(character: Character, level: int):
	print(textwrap.fill("The room is filled with chests and crates of different sizes and colours.", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("Three chests stand out, aligned next to eachother near the center of the room.", 70) + "\n")
	time.sleep(2)

	print(textwrap.fill("The chest on the left is made of wood and quite a bit smaller than the rest.", 70) + "\n")
	time.sleep(2)
	print("There is one lock on it.\n")
	time.sleep(1)

	print(textwrap.fill("The chest in the middle is made of silver, emitting a soft, twinkling light.", 70) + "\n")
	time.sleep(2)
	print("There are two locks on it.\n")
	time.sleep(1)

	print(textwrap.fill("The chest on the right is the biggest of the three, its gold exterior burning to the touch.", 70) + "\n")
	time.sleep(2)
	print("There are three locks on it.\n")
	time.sleep(1)

	print("You see a sign:\n")
	time.sleep(2)

	print("'You must choose at most one chest out of the three.'\n")
	time.sleep(2)

	while True:
		print("What will you do?")
		choices = ["Wooden chest", "Silver chest", "Gold chest", "Check lockpicks", "Leave"]
		print_choices(choices)

		choice = input()

		if choice.lower() == "wooden chest":


