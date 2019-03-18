BN_files = BN-TestSet2.py
BN_original = $(addprefix ../tests/BN-TestSet2/, $(BN_files))
RL_files = RL-TestSet2.py Q2.npz traj2.npz
RL_original = $(addprefix ../tests/RL-TestSet2/, $(RL_files))

REPORT = ../T005.pdf

all: bn rl

bn:
	cp $(BN_original) .
	python3 BN-TestSet2.py; rm -f $(BN_files)

rl:
	cp $(RL_original) .
	python3 RL-TestSet2.py; rm -f $(RL_files)

zip: BN.py RL.py $(REPORT)
	zip ../T005.zip $^

.PHONY: zip
