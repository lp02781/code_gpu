
#https://www.geeksforgeeks.org/implementation-of-whale-optimization-algorithm/
#https://www.geeksforgeeks.org/whale-optimization-algorithm-woa/
import random
import math # cos() for Rastrigin
import copy # array-copying convenience
import sys # max float
import matplotlib.pyplot as plt

minx=[-9.0, -2.0, -4.0]
maxx=[6.0, 8.0, 2.0]

dim = 3

rnd = random.Random(0)
Xbest=[0.0 for i in range(dim)]
Xcurrent=[0.0 for i in range(dim)]

for i in range(dim):
	Xcurrent[i] = ((maxx[i] - minx[i]) * rnd.random() + minx[i])
	Xbest[i] = ((maxx[i] - minx[i]) * rnd.random() + minx[i])

fitness_best = -50

def fitness_sphere(position):
	fitness_value = 0.0
	for i in range(len(position)):
		xi = position[i]
		fitness_value += (xi * xi);
	return fitness_value;

Iter = 0
max_iter = 1000

record_n=[0.0 for i in range(max_iter)]
record_fitness=[0.0 for i in range(max_iter)]
record_el_1=[0.0 for i in range(max_iter)]
record_el_2=[0.0 for i in range(max_iter)]
record_el_3=[0.0 for i in range(max_iter)]


while Iter < max_iter:
	a=2*(1-Iter/max_iter)
	a2=-1+Iter*((-1)/max_iter)

	A = 2 * a * rnd.random() - a
	C = 2 * rnd.random()
	b = 1
	l = (a2-1)*rnd.random()+1

	D = [0.0 for i in range(dim)]
	D1 = [0.0 for i in range(dim)]
	
	for j in range(dim):
		p = rnd.random()
		if p < 0.5:
			if abs(A)>1:
				D[j] = abs(C * Xbest[j] - Xcurrent[j])
				Xcurrent[j] = Xbest[j] - A * D[j]
			else:
				Xcurrent[j] = ((maxx[j] - minx[j]) * rnd.random() + minx[j])  		
			
		else:		
			D1[j] = abs(Xbest[j] - Xcurrent[j])
			Xcurrent[j] = D1[j] * math.exp(b * l) * math.cos(2 * math.pi * l) + Xbest[j]	

		Xcurrent[j] = max(Xcurrent[j], minx[j])
		Xcurrent[j] = min(Xcurrent[j], maxx[j])
		
	fitness_current = fitness_sphere(Xcurrent)

	if(fitness_current>fitness_best):
		Xbest, Xcurrent = Xcurrent, Xbest
		fitness_best=fitness_current
		print("haha")
		print(fitness_current)
		record_n[Iter]=Iter
		record_fitness[Iter]=fitness_current
	else:
		print("hehe")
		print(fitness_best)
		record_n[Iter]=Iter
		record_fitness[Iter]=fitness_best

	record_el_1[Iter]=Xbest[0]
	record_el_2[Iter]=Xbest[1]
	record_el_3[Iter]=Xbest[2]
	print(Xbest)
	print()
	Iter += 1

plt.plot(record_n, record_fitness)
#plt.plot(record_n, record_el_1)
#plt.plot(record_n, record_el_2)
#plt.plot(record_n, record_el_3)

plt.show()


