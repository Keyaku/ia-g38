CMD = -c "from "
ZIPFILE = T038.zip

all: p1 p2 p3

p1: P1/classsol.py
	cd P1 && python3 testclasssol.py

p2: P2/regsol.py
	cd P2 && python3 testregsol.py

p3: P3/RLsol.py
	cd P3 && python3 testRLsol.py

install-deps:
	pip3 install numpy scipy scikit-learn matplotlib joblib

zip:
	zip -v $(ZIPFILE) *.pdf *.py
