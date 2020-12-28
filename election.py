import numpy as np

from constituent import Constituent

class Election():
	"""
	Base election class

	Tracks candidates and constituents.

	Provides mode method (for vote counting) and conduct method
	(which asks each constituent to vote, takes the mode and 
	summarizes the outcome)
	"""

	def __init__(self):
		self.constituents = None
		self.candidates = None

	def mode(self, votes):
		"""
		Glorified vote counting

		:param votes: the array of votes
	    :type votes: np.array
	    :return: the mode of the constituent votes (a candidate)
	    :rtype: tuple
		"""
		v, c = np.unique(votes, return_counts=True)
		mode = c.argmax()
		return v[mode], c[mode]

	def conduct(self):
		votes = [c.vote(self.constituents, self.candidates) for c in self.constituents]
		winner, count = self.mode([v.constituent_id for v in votes])
		self.summarize(winner, count)

	def summarize(self, winner, count):
		raise NotImplemented()