import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
'''with open('iris_data.csv') as f:
    fil = csv.reader(f)
    for s in fil:
        arr.append(s)
arr.pop(0)'''
df = pd.read_csv('iris_data.csv')

SepalLengthCm = df["SepalLengthCm"]
SepalWidthCm =df["SepalWidthCm"]
PetalLengthCm =df["PetalLengthCm"]
PetalWidthCm = df["PetalWidthCm"]



plt.figure(figsize = (8,5), dpi = 100)
plt.plot(SepalLengthCm, SepalWidthCm, linestyle = '',marker = 'o', label = 'slsw')
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')


plt.figure(figsize = (8,5), dpi = 100)
plt.plot(SepalLengthCm, PetalLengthCm, linestyle = '',marker = 'o', label = 'slpl')
k2 = np.polyfit(SepalLengthCm, PetalLengthCm,1)
y2 = [i*k2[0] + k2[1] for i in SepalLengthCm]
plt.plot(SepalLengthCm, y2, label = 'slplkkk')
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalLengthCm')


plt.figure(figsize = (8,5), dpi = 100)
plt.plot(SepalLengthCm, PetalWidthCm, linestyle = '',marker = 'o', label = 'slpw')
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalWidthCm')


plt.figure(figsize = (8,5), dpi = 100)
plt.plot(SepalWidthCm, PetalLengthCm, linestyle = '',marker = 'o', label = 'swpwl')
plt.xlabel('SepalWidthCm')
plt.ylabel('PetalLengthCm')


plt.figure(figsize = (8,5), dpi = 100)
plt.plot(SepalWidthCm, PetalWidthCm, linestyle = '',marker = 'o', label = 'swpw')
plt.xlabel('SepalWidthCm')
plt.ylabel('PetalWidthCm')


plt.figure(figsize = (8,5), dpi = 100)
plt.plot(PetalLengthCm, PetalWidthCm, linestyle = '',marker = 'o', label = 'plpw')
k6 = np.polyfit(PetalLengthCm, PetalWidthCm,1)
y6 = [i*k6[0] + k6[1] for i in PetalLengthCm]
plt.plot(PetalLengthCm, y6, label = 'slplkkkkk')
plt.xlabel('PetalLengthCm')
plt.ylabel('PetalWidthCm')
plt.show()


