import random

class Utilities(object):
	"""description of class"""

	@staticmethod
	def randomInt(min, max):
		return random.randint(min, max)

	@staticmethod
	def randomFloat(min, max):
		return random.uniform(min, max)