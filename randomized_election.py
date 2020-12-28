import numpy as np

from constituent import Constituent
from election import Election

class RandomizedElection(Election):
	"""
	Simple base method:
	n constituents (def 100)
	c candidates (def 2)
	
	Initialize n constituents with the random vote and random fitness methods
	TODO: Initialize constituents intelligently according to distributions
	of interest, with attuned fitness

	Choose c candidates randomly
	TODO: Choose candidates cleverly based on test method
	"""

	def __init__(self, n=100, c=2):
		self.constituents = []
		# Initialization Method
		for i in range(n):
			self.constituents.append(Constituent(i, self.random_vote, {}, self.random_fitness, {}))

		self.constituents = np.array(self.constituents)

		# Candidate choice method
		self.candidates = np.random.choice(self.constituents.shape[0], c, replace=False)

	def random_vote(self, constituents, candidates):
		# Note: Perhaps toggle number of votes each constituent can cast?
		v = np.random.choice(candidates.shape[0], 1, replace=False)
		return constituents[v][0]

	def random_fitness(self):
		return np.random.rand()

	def summarize(self, winner, count):
		print("Candidates: " + str(self.candidates))
		print("Winner: " + str(self.candidates[winner]))
		print("Vote Tally: " + str(count))

class DemocraticElection(Election):
	def __init__(self):
		pass

	def voter_method_1(self):
		pass #guassian

	def summarize(self, winner, count):
		pass

class SortitionElection(Election):
	def __init__(self):
		pass

	def voter_method_2(self):
		pass #tail

	def summarize(self, winner, count):
		pass

if __name__ == "__main__":
	"""
	Here we conduct a simple randomized election
	"""

	election = RandomizedElection(1000,3)
	election.conduct()


