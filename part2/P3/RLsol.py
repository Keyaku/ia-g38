# 84738 Lucia Lisboa
# 77906 Antonio Sarmento
# Grupo: 38

import numpy as np

# Calculo da politica
def Q2pol(Q, eta=5):
	pol = np.zeros(Q.shape)

	# Em cada linha da matriz Q escolhemos o maior elemento
	# Na posicao do maior elemento coloca-se "1" na matriz pol
	for line,values in enumerate(Q):
		idx = np.argmax(values)
		pol[line, idx] = 1

	return pol

#--------------------------------------------------------------------------------------------------------------------
# Implementacao do algoritmo Q-learning
# gamma = discount factor 0 < gamma < 1
# alpha = learning rate   0 < alpha < 1
class myRL:

	def __init__(self, nS, nA, gamma):
		self.nS = nS  # numero de linhas -> numero de estados
		self.nA = nA  # numero de colunas -> numero de accoes
		self.gamma = gamma
		self.Q = np.zeros((nS,nA))

	# Calcular os valores de Q para cada accao
	# Trace e' uma matriz
	# Cada linha = [estado inicial acao estado final recompensa]
	def traces2Q(self, trace):
		self.Q = np.zeros((self.nS, self.nA))
		tempQ  = np.zeros((self.nS, self.nA))

		alpha = 0.1

		#Vai convergir para um numero
		while True:
			for ele in trace:

				state  = int(ele[0])
				action = int(ele[1])
				next_state = int(ele[2])
				reward = ele[3]

				tempQ[state, action] += alpha * (reward + self.gamma * max(tempQ[next_state, :]) - tempQ[state, action])

			dif = np.linalg.norm(self.Q-tempQ)
			self.Q = np.copy(tempQ)

			if dif < 1e-2:
				break

		return self.Q
