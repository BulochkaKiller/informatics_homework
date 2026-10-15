import matplotlib.pyplot as plt
import numpy as np
from random import *
res = []
steps = []
for ch in range(1000):
    x = [0]
    for N in range(1,1001):
        f = randint(0,1)
        if f == 0:
            x.append(x[N-1] - 1)
        else:
            x.append(x[N-1] + 1)
    res.append(x[-1])
    steps.append(x)
plt.figure(figsize=(8,5), dpi = 100)
plt.hist(res, 80)
sigma = []
N = [i for i in range(1,1001)] #надо найти сигму для каждого номера шага
for n in range(1,1001):
    time_sr1 = 0
    for i in range(1000):
        time_sr1 += steps[i][n-1]
    time_sr = time_sr1/1000
    time =0
    for t in range(1000):
        time += (steps[t][n-1] - time_sr)**2       
    s = (1/(n**2)*time)**0.5
    sigma.append(s)
plt.figure(figsize = (8,5), dpi = 100)
plt.plot(N, sigma, linestyle = '',marker = 'o', label = 'sigmagraf')  
  
plt.show()

