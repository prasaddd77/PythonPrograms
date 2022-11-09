# from scipy.linalg import *
# import numpy as np
# a = np.array([[9,6,-5,2],[4,5,-7,3],[-3,-4,2,-5],[6,1,9,-5]])
# b = np.array([17,10,20,23])
# x=solve(a,b)
# print(x)


import matplotlib.pyplot as plt
import numpy as np
barWidth = 0.4
x = ["United States", "China","Great Britain","Russia", "Germany", "Japan"]
y = [57,48,39,25,20,10]
z = [28,30,21,25,18,16]
ticks = np.arange(len(x))
print(ticks)
plt.bar(ticks-barWidth/2,y,width=barWidth,edgeColor='black',label='Gold Medals')
plt.bar(ticks-barWidth/2,z,width=barWidth,edgeColor='black',label='Silver Medals')
plt.xticks(ticks,x)
plt.title("Performance in Olympics")
plt.xlabel("Country")
plt.ylabel("Medals")
plt.legend()

