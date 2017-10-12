from search import *


# Main---------------------------------------------------------------------

def main():
	return  # FIXME: remove this when all our global methods are complete
	initial_board = eval(input())

	if is_board(initial_board):
		game = same_game(initial_board)  # maybe


# de seguida chamamos uma procura e vemos os resultados


if __name__ == "__main__":
	# execute only if run as a script
	main()


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


def board_is_position(board, l, c):
	return 0 <= l < len(board) and 0 <= c < len(board[0])


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
		board = board_shift_down(board, l - 1, c)

	return board


def board_shift_left(board, l, c):
	if board_is_position(board, l, c - 1) and no_color(board[l][c - 1]):
		board[l][c] = board[l][c - 1]
		board[l][c - 1] = get_no_color()
		board = board_shift_left(board, l, c - 1)

	return board


def board_remove_group(board, group):
	new_board = board_clone(board)

	# Clearing blanks
	for pos in group:
		l = pos_l(pos)
		c = pos_c(pos)

		new_board[l][c] = get_no_color()

		# primeiro faz-se o shift_down
		new_board = board_shift_down(new_board, l, c)
	# TODO: fazer shift_left

	return new_board


def board_tile_count(board):
	tiles = len(board) * len(board[0])

	for l in board:
		tiles -= l.count(get_no_color())

	return tiles


def board_lin(board):
	return len(board)


def board_col(board):
	return len(board[0])

#-----------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# XXX: Testing grounds for Boards
#################################
# Testing board_find_groups()
my_board = [[1, 2, 2, 3, 3], [2, 2, 2, 1, 3], [1, 2, 2, 2, 2], [1, 1, 1, 1, 1]]
board_print(my_board)
g1 = board_find_groups(my_board)
g2 = [[(0, 0)], [(0, 1), (1, 1), (2, 1), (2, 2), (1, 2), (0, 2), (2, 3), (2, 4), (1, 0)], [(0, 3), (0, 4), (1, 4)],
      [(1, 3)], [(2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]]

if g1 == g2:
	print("Worked")
else:
	print(g1)
	print("!=")
	print(g2)

print("# ---------------------------------------------------------------------------")
# Testing board_remove_group()

new_board = [[0, 0, 0, 0, 0], [0, 2, 3, 3, 0], [1, 2, 1, 3, 0], [2, 2, 2, 2, 0]]
g3 = [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 0)]
board_print(new_board)
new_board = board_remove_group(new_board, g3)
result = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 3, 3, 0, 0], [1, 1, 3, 0, 0]]
print("\nRemoved group:", g3)
if new_board == result:
	print("Worked")
else:
	board_print(new_board)
	print("!=")
	board_print(result)


# -----------------------------------------------------------------------------------------

# TAI sg_state
# Classe que contem configuracao de uma board
class sg_state():
	# estado deve ser representado por pelo menos um slot
	# armazenada  configuracao do tabuleiro a que o estado pertence

	def __init__(self, board):
		self.board = board

	# A*
	def __lt__(self, o_state):
		pass


# ---------------------------------------------------------------------------------------

# TAI same_game
# Herda da class Problem do ficheiro search.py
class same_game(Problem):
	"""Models a Same Game problem as a satisfaction problem.
	A solution cannot have pieces left on the board."""

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

		last_line = state.board[-1]

		return last_line[0] == 0

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
