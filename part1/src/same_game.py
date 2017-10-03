from search import Problem

# TAI color
# sem cor = 0
# com cor > 0
def get_no_color():
	return 0
def no_color(c):
	return c==0
def color(c):
	return c > 0

# TAI pos
# Tuplo (l, c)
def make_pos(l, c):
	return (l, c)
def pos_l(pos):
	return pos[0]
def pos_c(pos):
	return pos[1]

# TAI group
# Lista de pecas adjacentes
# e.g. group = [(0,1),(1,1),(2,1),(2,2),(1,2),(0,2),(2,3),(2,4),(1,0)]
def make_group(listas):
	pass


# TAI board
# Lista de listas de color
# e.g. board = [[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]]
#
# e.g list of groups = [[(0,0)],[(0,1),(1,1),(2,1),(2,2),(1,2),(0,2),(2,3),(2,4),(1,0)], [(0,3),(0,4),(1,4)],[(1,3)],[(2,0),(3,0),(3,1),(3,2),(3,3),(3,4)]]
#
def board_find_groups(board):
	pass

def board_remove_group(board, group):
	pass


# TAI sg_state
# Classe que contem configuracao de uma board
# TODO

# TAI same_game
class same_game(Problem):
	"""Models a Same Game problem as a satisfaction problem.
	A solution cannot have pieces left on the board."""

	def __init__(self, board):
		pass

	def actions(self, state):
		pass
	def result(self, state, action):
		pass
	def goal_test(self, state):
		pass
	def path_cost(self, c, state1, action, state2):
		pass
	def h(self, node):
		"""Needed for informed search."""
		pass
