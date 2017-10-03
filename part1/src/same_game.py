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
def make_group(board, l, c):
	return group_find_adj(board, board[l][c], l, c, [])

def group_find_adj(board, cor, l, c, adj):
	if board_is_pos(board, l, c) and cor == board[l][c]:
		pos = make_pos(l, c)
		if pos not in adj:
			adj += [pos]

			# deCORando a COR. Get it?
			cor = board[l][c]
			board[l][c] = get_no_color() # marcamos como visitado

			# Verificando pela ordem: sup, inf, esq, dir
			adj = group_find_adj(board, cor, l+1, c, adj)
			adj = group_find_adj(board, cor, l-1, c, adj)
			adj = group_find_adj(board, cor, l, c+1, adj)
			adj = group_find_adj(board, cor, l, c-1, adj)

	return adj


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

def board_is_pos(board, l, c):
	return 0 <= l < len(board) and 0 <= c < len(board[0])

def board_find_groups(board):
	new_board = board_clone(board)
	lista_de_grupos = [] # tem que ter tamanho de numero de cores

	b_range = range(len(new_board))
	for l in b_range:
		for c in b_range:
			if color(new_board[l][c]):
				lista_de_grupos += [make_group(new_board, l, c)]
			else:
				continue

	return lista_de_grupos

def board_remove_group(board, group):
	new_board = board_clone(board)

	for pos in group:
		l = pos_l(pos)
		c = pos_c(pos)

		new_board[l][c] = get_no_color()

	return new_board


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
