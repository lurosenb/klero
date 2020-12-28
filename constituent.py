import numpy as np

class Constituent():
	"""
	Base constituent class

	We want to track the vote method and params for
	each constituent. We further track the fitness
	(to lead) method for each constituent.

	We also want to assign vote power (default 1).

	We can assign here whether a constituent is also a
	candidate.

	We call the given fitness method on initialization
	to assign a constituent fitness.
	"""

	def __init__(self, 
			constituent_id,
			vote_method, 
			vote_method_params, 
			fitness_method,
			fitness_method_params,
			candidates = None, 
			vote_power = 1.0,  
			is_candidate = False):
		self.constituent_id = constituent_id
		self.vote_method = vote_method
		self.vote_method_params = vote_method_params

		self.is_candidate = is_candidate
		self.vote_power = vote_power
		self.candidates = candidates
		self.fitness_method = fitness_method
		self.fitness = self.fitness_method(**fitness_method_params)

		self.chosen_candidate = None

	def vote(self, constituents, candidates):
		"""
		Glorified vote method

		:param constituents: an array of all the constituents
	    :type constituents: np.array
	    :param candidates: an array of all the candidates
	    :type candidates: np.array
	    :return: call the assigned vote method and return the candidate chosen
	    :rtype: tuple
		"""

		self.candidates = candidates
		self.chosen_candidate = self.vote_method(
			constituents = constituents, 
			candidates = candidates, 
			**self.vote_method_params)
		return self.chosen_candidate