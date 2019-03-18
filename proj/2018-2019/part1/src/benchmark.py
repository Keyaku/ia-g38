from solitaire import *
import time

board_30 = [
    ["O","O","O","X","X"],
    ["O","O","O","O","O"],
    ["O","_","O","_","O"],
    ["O","O","O","O","O"]
]
board_30_name = "test30"

board_32 = [
	["O","O","O","X","X","X"],
	["O","_","O","O","O","O"],
	["O","O","O","O","O","O"],
	["O","O","O","O","O","O"]
]
board_32_name = "test32"



# -------------------------------------------------------------------------
# Private Mooshak Functions
def greedy_search(problem, h=None):
    """f(n) = h(n)"""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, h)
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Tests from paper
tests_paper = {
	'test01' : [ # Tabuleiro de 5x5
		["_","O","O","O","_"],
		["O","_","O","_","O"],
		["_","O","_","O","_"],
		["O","_","O","_","_"],
		["_","O","_","_","_"]
	],
	'test02' : [ # Tabuleiro de 4x4
		["O","O","O","X"],
		["O","O","O","O"],
		["O","_","O","O"],
		["O","O","O","O"]
	],
	'test03' : [ # Tabuleiro de 4x5
		["O","O","O","X","X"],
		["O","O","O","O","O"],
		["O","_","O","_","O"],
		["O","O","O","O","O"]
	],
	'test04' : [ # Tabuleiro de 4x6
		["O","O","O","X","X","X"],
		["O","_","O","O","O","O"],
		["O","O","O","O","O","O"],
		["O","O","O","O","O","O"]
	]
}

test_04 = [
	["_","_","_","X","X","X"],
	["_","_","O","_","_","_"],
	["O","O","O","O","O","_"],
	["O","O","O","O","O","_"]
]

# for search in [
# depth_first_graph_search,
# # greedy_search,
# # astar_search
# ]:
# 	start_time = time.time()
# 	compare_searchers(
# 	problems=[ solitaire(test_04) ],
# 	header=['Searcher', "test_04" ],
# 	searchers=[search])
# 	end_time = time.time()
# 	print("Time Elapsed:", end_time - start_time)
# 	print()
# sys.exit()
# -------------------------------------------------------------------------



for test_name in tests_paper:
	test = tests_paper[test_name]

	for search in [ depth_first_graph_search, greedy_search, astar_search ]:
		start_time = time.time()
		compare_searchers(
		problems=[ solitaire(test) ],
		header=['Searcher', test_name ],
		searchers=[search])
		end_time = time.time()
		print("Time Elapsed:", end_time - start_time)
		print()
	print("----------------------------------\n")
