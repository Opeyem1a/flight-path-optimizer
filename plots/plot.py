import math
import dill

import matplotlib.pyplot as plt
import numpy as np


with open('times-again.pkl', 'rb') as f:
    times = dill.load(f)

r = range(5, 365, 10)
times_x = []
times_y = []

for i in r:
    times_x.append(i)

for time in times:
    times_y.append(0 - time)

plt.plot(times_x, times_y, label='Actual')
plt.title('Better Algorithm')
plt.xlabel('V (number of airports)')
plt.ylabel('t (execution time in seconds)')

x = []
y = []
for i in r:
    x.append(i)
    y.append(0.00000000006*5000*(i**2))

plt.plot(x, y, label='Predicted - O(bV^2)')

x = []
y = []
for i in r:
    x.append(i)
    y.append(0.000000001*5000*i*math.log(i))

plt.plot(x, y, label='Predicted - O(bVlog(V))')


# edges = 205939
plt.legend()
plt.show()
