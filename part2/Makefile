ZIPFILE = T038.zip

all: p1 p2 p3

p1: P1/classsol.py
	python3 P1/testclasssol.py

p2: P2/regsol.py
	python3 P2/testregsol.py

p3: P3/RLsol.py
	python3 P3/testRLsol.py

install-deps:
	pip3 install numpy scipy scikit-learn

zip:
	zip -v $(ZIPFILE) *.pdf *.py
