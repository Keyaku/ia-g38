# tp005 - 77906 António Sarmento - 83391 - Andreia Valente

from search import *


# TAI content
def c_peg():
	return "O"

def c_empty():
	return "_"

def c_blocked():
	return "X"

def is_empty(e):
	return e == c_empty()

def is_peg(e):
	return e == c_peg()

def is_blocked(e):
	return e == c_blocked()


# -------------------------------------------------------------------------

# TAI pos
# Tuplo (l, c)
def make_pos(l, c):
	return (l, c)

def pos_l(pos):
	return pos[0]

def pos_c(pos):
	return pos[1]


# -------------------------------------------------------------------------

# TAI move
# Lista [p_initial, p_final]
def make_move(i, f):
	return [i, f]

def move_initial(move):
	return move[0]

def move_final(move):
	return move[1]


# -------------------------------------------------------------------------

# TAI board
# Copies a board
def board_clone(board):
	return [list(line) for line in board]

# Returns number of lines
def board_lin(board):
	return len(board)

# Returns number of columns
def board_col(board):
	return len(board[0])

# Checks if the given position is within bounds and not blocked
def board_is_valid_position(board, l, c):
	return 0 <= l < board_lin(board) and 0 <= c < board_col(board)

# Returns a list of possible moves
def board_moves(board):
	moves = []

	for l in range(board_lin(board)):
		for c in range(board_col(board)):
			pos_i = make_pos(l, c)
			peg = board[l][c]

			if is_peg(peg):
				# Search up, down, left, right. In that order.
				search_pos = [
					make_pos(pos_l(pos_i), pos_c(pos_i)-2), # up
					make_pos(pos_l(pos_i), pos_c(pos_i)+2), # down
					make_pos(pos_l(pos_i)-2, pos_c(pos_i)), # left
					make_pos(pos_l(pos_i)+2, pos_c(pos_i))  # right
				]

				for pos_f in search_pos:
					if not board_is_valid_position(board, pos_l(pos_f), pos_c(pos_f)):
						continue # ignore if it's not a valid position (e.g. (-1, 0))

					l_mid = (pos_l(pos_i) + pos_l(pos_f)) >> 1 # / 2
					c_mid = (pos_c(pos_i) + pos_c(pos_f)) >> 1 # / 2
					if is_peg(board[l_mid][c_mid]) and is_empty(board[pos_l(pos_f)][pos_c(pos_f)]):
						moves += [make_move(pos_i, pos_f)]

	return moves

# Performs a move without verification
def board_perform_move(board, move):
	b_copy = board_clone(board)

	# Grabbing initial and final positions
	pos_i = move_initial(move)
	pos_f = move_final(move)

	# Grabbing middle position
	l_mid = (pos_l(pos_i) + pos_l(pos_f)) >> 1 # / 2
	c_mid = (pos_c(pos_i) + pos_c(pos_f)) >> 1 # / 2
	pos_m = make_pos(l_mid, c_mid)

	# Perform the move
	b_copy[pos_l(pos_i)][pos_c(pos_i)] = c_empty()
	b_copy[pos_l(pos_m)][pos_c(pos_m)] = c_empty()
	b_copy[pos_l(pos_f)][pos_c(pos_f)] = c_peg()

	return b_copy

# Counts number of pegs within the board
def board_peg_count(board):
	count = 0

	for line in board:
		count += line.count(c_peg())

	return count

# Prints a formatted board
def board_print(board):
	for line in board:
		print("[ ", end='')
		for e in line:
			print(e + ' ', end='')
		print("]")
	print(flush=True)

# Finds the first empty space in the board
def board_get_empty(board):
	for l in range(board_lin(board)):
		for c in range(board_col(board)):
			peg = board[l][c]
			if is_empty(peg):
				return l, c

	return 0, 0

# Sum of the distance between the first empty space found and the rest of the pegs
def manhattan_distance(board):
	distance = 0

	l_mid, c_mid = board_get_empty(board)
	minimum_cost = sys.maxsize # In order to subtract it to the final heuristic value

	for l in range(board_lin(board)):
		for c in range(board_col(board)):
			peg = board[l][c]
			if is_peg(peg):
				dx = abs(l - l_mid)
				dy = abs(c - c_mid)

				minimum_cost = min(minimum_cost, dx + dy)
				distance += dx + dy

	return distance - minimum_cost

# -------------------------------------------------------------------------

# TAI sol_state
class sol_state():
	__slots__ = ['board', 'peg_count']

	def __init__(self, board):
		self.board = board
		self.peg_count = board_peg_count(board)

	# For the A* search. Should be a lightweight comparison.
	def __lt__(self, o_state):
		return self.peg_count > o_state.peg_count

# -------------------------------------------------------------------------

class solitaire(Problem):
	"""Models a Solitaire problem as a satisfaction problem.
		A solution cannot have more than 1 peg left on the board."""

	def __init__(self, board):
		"""The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
		self.initial = sol_state(board)

	def actions(self, state):
		"""Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
		return board_moves(state.board)

	def result(self, state, action):
		"""Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
		return sol_state(board_perform_move(state.board, action))

	def goal_test(self, state):
		"""Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""

		"""Peg count must be == 1, at any position"""
		return state.peg_count == 1

	def path_cost(self, c, state1, action, state2):
		"""Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
		return c + 1

	def h(self, node):
		"""Estimated cost of the cheapest path from the state at node n to
		a goal state.
		Needed for informed search."""
		return manhattan_distance(node.state.board)
