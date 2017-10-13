from search import *


# -------------------------------------------------------------------------

# TAI color
# sem cor = 0
# com cor > 0
def get_no_color():
	return 0


def no_color(c):
	return c == 0


def color(c):
	return c > 0


# -------------------------------------------------------------------------

# TAI pos
# Tuplo (l, c)
def make_pos(l, c):
	return (l, c)


def pos_l(pos):
	return pos[0]


def pos_c(pos):
	return pos[1]


# ----------------------------------------------------------------------------

# TAI group
# Lista de pecas adjacentes
# e.g. group = [(0,1),(1,1),(2,1),(2,2),(1,2),(0,2),(2,3),(2,4),(1,0)]
def make_group(board, l, c):
	return group_find_adj(board, board[l][c], l, c, [])


def group_find_adj(board, cor, l, c, adj):
	if board_is_position(board, l, c) and cor == board[l][c]:

		pos = make_pos(l, c)

		if pos not in adj:
			adj += [pos]

			# deCORando a COR. Get it?
			cor = board[l][c]
			board[l][c] = get_no_color()  # marcamos como visitado

			# Verificando pela ordem: sup, inf, esq, dir
			adj = group_find_adj(board, cor, l + 1, c, adj)
			adj = group_find_adj(board, cor, l - 1, c, adj)
			adj = group_find_adj(board, cor, l, c + 1, adj)
			adj = group_find_adj(board, cor, l, c - 1, adj)

	return adj


# --------------------------------------------------------------------------------

# TAI board
# Lista de listas de color
def board_clone(board):
	new_board = []
	for line in board:
		new_board += [list(line)]
	return new_board


def board_print(board):
	for line in board:
		print(line)


def board_lin(board):
	return len(board)


def board_col(board):
	return len(board[0])


def board_is_position(board, l, c):
	return 0 <= l < board_lin(board) and 0 <= c < board_col(board)


def board_find_groups(board):
	new_board = board_clone(board)
	lista_de_grupos = []  # tem que ter tamanho de numero de cores

	l_range = range(len(new_board))
	c_range = range(len(new_board[0]))

	for l in l_range:
		for c in c_range:

			if color(new_board[l][c]):
				lista_de_grupos += [make_group(new_board, l, c)]

	return lista_de_grupos


def board_shift_down(board, l, c):
	if board_is_position(board, l - 1, c) and no_color(board[l][c]):
		board[l][c] = board[l - 1][c]
		board[l - 1][c] = get_no_color()
		board_shift_down(board, l - 1, c)


def board_shift_left(board, l, c):
	if board_is_position(board, l, c + 1) and no_color(board[l][c]):
		board[l][c] = board[l][c + 1]
		board[l][c + 1] = get_no_color()
		board_shift_left(board, l - 1, c)


def board_remove_group(board, group):
	new_board = board_clone(board)

	# Sorting our group so we can accurately shift down while we remove each piece
	group.sort()

	# Clearing blanks
	for pos in group:
		l = pos_l(pos)
		c = pos_c(pos)

		new_board[l][c] = get_no_color()

		# Immediately shifting down
		board_shift_down(new_board, l, c)

	# Shifting left
	l = board_lin(new_board)-1
	for c in range(board_col(new_board)):
		board_shift_left(new_board, l, c)

	return new_board


def board_tile_count(board):
	tiles = board_lin(board) * board_col(board)

	for l in board:
		tiles -= l.count(get_no_color())

	return tiles


# -----------------------------------------------------------------------------------------

# TAI sg_state
# Classe que contem configuracao de uma board
class sg_state():
	# estado deve ser representado por pelo menos um slot
	# armazenada configuracao do tabuleiro a que o estado pertence

	__slots__ = ['board']

	def __init__(self, board):
		self.board = board

	# A*
	def __lt__(self, o_state):
		return board_tile_count(self.board) < board_tile_count(o_state.board)


# ---------------------------------------------------------------------------------------

# TAI same_game
# Herda da class Problem do ficheiro search.py
class same_game(Problem):
	"""Models a Same Game problem as a satisfaction problem.
	A solution cannot have pieces left on the board."""

	__slots__ = ['initial', 'goal']

	def __init__(self, board):
		self.initial = board

		# the goal is going to be a board full of zeros....
		self.goal = [[0] * board_lin(board) for i in range(board_col(board))]

	def actions(self, state):
		"""Return the actions that can be executed in the given
		state. The result would typically be a list, but if there are
		many actions, consider yielding them one at a time in an
		iterator, rather than building them all at once."""

		'''Uma accao deve ser um grupo de pecas a remover com uma cardinalidade maior ou igual a
		dois, na representacao definida acima.'''

		all_actions = board_find_groups(state.board)

		# delete the group of pieces with only one piece
		actions = list(filter(lambda lst: len(lst) > 1, all_actions))

		return actions

	def result(self, state, action):
		"""Return the state that results from executing the given
		action in the given state. The action must be one of
		self.actions(state)."""
		result = board_remove_group(state.board, action)
		return result

	def goal_test(self, state):
		"""Return True if the state is a goal. The default method compares the
		state to self.goal or checks for state in self.goal if it is a
		list, as specified in the constructor. Override this method if
		checking against a single self.goal is not enough."""
		return no_color(state.board[-1][0])

	def path_cost(self, c, state1, action, state2):
		"""Return the cost of a solution path that arrives at state2 from
		state1 via action, assuming cost c to get up to state1. If the problem
		is such that the path doesn't matter, this function will only look at
		state2.  If the path does matter, it will consider c and maybe state1
		and action. The default method costs 1 for every step in the path."""
		return c + 1

	def h(self, node):
		"""Needed for informed search."""
		# Number of misplaced tiles maybe
		# Number of alone pieces
		# Number of groups
		misplaced_tiles = board_tile_count(node.state.board)
		return misplaced_tiles

	# ----------------------------------------------------------------------------------


# Main---------------------------------------------------------------------

def main():
	exec(sys.argv[1])


if __name__ == "__main__":
	# execute only if run as a script
	main()
