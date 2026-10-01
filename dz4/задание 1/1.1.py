import matplotlib.pyplot as plt
from random import *
x = [0]
for N in range(1,1001):
    f = randint(0,1)
    if f == 0:
        x.append(x[N-1] - 1)
    else:
        x.append(x[N-1] + 1)
N = [i for i in range(0,1001)]
plt.figure(figsize=(8,5), dpi = 100)
plt.plot(N, x, label = "x(N)")
plt.xlabel("N")
plt.ylabel("x")
plt.show()