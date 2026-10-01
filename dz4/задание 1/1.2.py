import matplotlib.pyplot as plt
import numpy as np
from random import *
res = []
for ch in range(1000):
    x = [0]
    for N in range(1,1001):
        f = randint(0,1)
        if f == 0:
            x.append(x[N-1] - 1)
        else:
            x.append(x[N-1] + 1)
    res.append(x[-1])
plt.figure(figsize=(8,5), dpi = 100)
plt.hist(res, 80)
sigma = []
N = []
nehehe = np.array(res)
for n in range(1,1000):
    mimimi = res[:n+1]
    sr = sum(mimimi)/len(mimimi)
    s = sum([(sr-i)**2 for i in mimimi])
    sigma.append((s/(len(mimimi)*(len(mimimi)-1))*s)**0.5)
    N.append(len(mimimi))
plt.figure(figsize = (8,5), dpi = 100)
plt.plot(N, sigma, linestyle = '',marker = 'o', label = 'slpw')    
plt.show()
