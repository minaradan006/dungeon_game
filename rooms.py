import random
from monsters import wise_owl, skeleton_warrior, rat_king, knight, eye, axe_orc, glowing_moth, rose_assasin

walls = [
	"vines",
	"fire",
	"bones",
	"gems",
	"water",
	"flowers",
	"blood"
]

room_adjectives = [
	"dark",
	"dusty",
	"musty",
	"echoing",
	"freezing",
	"burning",
	"crumbling",
	"blood-stained",
	"bright"
]

room_adjectives_desc = {
	"dark": "There is almost no light in the room, making it very difficult to see anything.",
	"dusty": "A thick layer of dust is layered on the floor.",
	"musty": "There is a moldy smell lingering in the room.",
	"echoing": "You try screaming, but you are only met with your own voice replying.",
	"freezing": "The room is so cold that you can see your own breath and the walls appear a shade of light blue.",
	"burning": "There are few fires that make it difficult to breathe, but they seem to be contained.",
	"crumbling": "The ceiling and walls are cracked, dust falling from them.",
	"blood-stained": "The walls are covered in glossy, maroon streaks of blood.",
	"bright": "There is an unnatural warm light in the room that makes everything seem calm and peaceful."
}

room_types = [
	"corridor",
	"chamber",
	"crypt",
	"armory",
	"dungeon cell",
	"hallway",
	"library",
	"garden"
]

room_types_desc = {
	"corridor": ["The long corridor stretches out in front of you, dozens of doors on each wall. They all seem to be locked.",
				"The door at the end of the corridor opens.", axe_orc],
	"chamber": ["The smell of wood escapes from the brick fireplace and the forest green armchairs seem very comfortable.",
			   "A hidden door opens behind the brick wall of the fireplace.", glowing_moth],
	"crypt": ["From the stone coffins ivory colored bones peek out and chalky dust spills from the urns.",
			 "A coffin with a strange carving unlocks and reveals an exit.", skeleton_warrior],
	"armory": ["A shining suit of armour stands proudly in the center of the room, hundreds of swords, shields, axes, daggers strewn on the floor and hung on the walls.",
			  "The suit of armour lowers itself into the floor and reveals a ladder toward an exit.", knight],
	"dungeon cell": ["The rusty bars don't budge when shaken. The only source of air is coming from a tiny window that you can't reach.",
					"You hear a clicking sound and the cell door opens.", rat_king],
	"hallway": ["A thin and long persian carpet stretches from one end of the room to the other, a few landscape paintings hung on the walls.",
			   "A painting of a sunset falls on the ground and reveals a hidden corridor.", eye],
	"library": ["The scent of old paper makes you dizzy, the walls being only a circular bookshelf filled to the brim with leatherbound books.",
			   "You pull the only golden book from its shelf and a hidden crawl space opens.", wise_owl],
	"garden": ["There are thousands of different coloured flowers, a myriad of butterflies floating about, the dewy grass glistening.",
			  "The flowers move on their own to reveal a trapdoor underneath.", rose_assasin]
}

class Room:
	def __init__(self, level):
		r_adj = random.choice(room_adjectives)
		r_type = random.choice(room_types)

		self.desc = f"{r_adj} {r_type}"

		self.entry = room_types_desc[r_type][0]
		self.exit = room_types_desc[r_type][1]
		self.monster = room_types_desc[r_type][2]

		self.adj = room_adjectives_desc[r_adj]

		self.event = random.choices(
		["enemy", "treasure", "trap", "shop", "empty"],
		weights=[0.4 + (level * 0.05), 0.2, 0.3, 0.2, 0.2],
	)[0]