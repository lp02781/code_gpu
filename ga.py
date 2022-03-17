#https://pypi.org/project/geneticalgorithm/#:~:text=geneticalgorithm%20is%20a%20Python%20library,algorithm%20(GA)%20in%20Python.
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def f(X):
    pen=0
    if X[0]+X[1]<2:
        pen=500+1000*(2-X[0]-X[1])
    return np.sum(X)+pen

varbound=np.array([[0,10]]*3)

model=ga(function=f,dimension=3,variable_type='real',variable_boundaries=varbound)

model.run()