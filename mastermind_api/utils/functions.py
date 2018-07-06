def whitePegs(riddle, guess):
	"""
	\b Function used to calculate the number of white pegs or pegs in general, 
	they will remain white after substract the black pegs
	\param: riddle (\c list) the riddle to solve
	\param: guess (\c list) the guess to compare with the riddle   
	"""
	
	pegs = 0
	riddle_aux = riddle[:]
	for i in guess:
		if i in riddle_aux:
			riddle_aux.remove(i)
			pegs += 1
	return pegs


def blackPegs(riddle, guess):
	"""
	\b Function used to calculate the number of black pegs 
	\param: riddle (\c list) the riddle to solve
	\param: guess (\c list) the guess to compare with the riddle   
	"""

	pegs = 0
	for i in range(len(riddle)):
		if riddle[i] == guess[i]:
			pegs += 1
	return pegs


def mastermindAlgorithm(riddle, guess):
	"""
	\b Funstion used to return the number of white and black pegs from an mastermind guess
	\param, riddle (\c list) the riddle to solve
	\param, guess (\c list) the guess to compare with the riddle   
	"""
	
	white_pegs = whitePegs(riddle, guess)
	black_pegs = blackPegs(riddle, guess)
	white_pegs = white_pegs - black_pegs
	return white_pegs, black_pegs
