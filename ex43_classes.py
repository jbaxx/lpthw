from sys import exit
from random import randint


class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()"
		exit(1)


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		current_scene.enter()


class Death(Scene):

	quips = [
		"You died. You kinda suck at this lol.",
		"Your mom would be proud... if she were smarter.",
		"Such a loser.",
		"I have a small puppy that's better at this."]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal have invaded your ship"
		print "He's blocking the door, what should you do?"

		action = raw_input("> ")

		if action == "shoot":
			print "you're death" 
			return "death"

		elif action == "dodge":
			print "you're death"
			return "death"

		elif action == "joke":
			print "Lucky for you"
			return "laser_weapon_armory"

		else:
			print "Does not compute"
			return "central_corridor"


class LaserWeaponArmory(Scene):

	def enter(self):
		print "You enter the weaponry"
		print "get the bom, the code is 3 digit"
		code = "%d" % (randint(1, 9))
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZZEDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == code:
			print "It opens and you spot the bridge"
			return "the_bridge"
		else:
			print "The lock buzzes"
			return "death"


class TheBridge(Scene):

	def enter(self):
		print "You enter into the Bridge, what to do?"
		print "throw bomb, place bomb"

		action = raw_input("> ")

		if action == "throw bomb":
			print "You're dead"
			return "death"

		elif action == "place_bomb":
			print "You go to escape pod"
			return "escape_pod"

		else:
			print "Does not compute"
			return "the_bridge"

class EscapePod(Scene):

	def enter(self):
		print "You enter the escape pod, there are 5, choose one."

		good_pod = randint(1, 5)
		guess = raw_input("[pod #]> ")

		if int(guess) != good_pod:
			print "wrong pod"
			return "death"
		else:
			print "You won!"
			return "finished"

class Finished(Scene):

	def enter(self):
		print "You won! Good Job."
		return "finished"

class Map(object):

	scenes = {
	"central_corridor": CentralCorridor(),
	"laser_weapon_armory": LaserWeaponArmory(),
	"the_bridge": TheBridge(),
	"death": Death(),
	"finished": Finished()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()





