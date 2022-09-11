#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Coverage of 5x
cov_array = np.zeros(1000000)
for i in range(50000):
    start = np.random.randint(0, high=999900)
    for h in range(start, start+100):
        cov_array[h] += 1

fig, ax = plt.subplots()
x = np.arange(0, 20, 1)
y = poisson.pmf(x, 5, 0)*1000000
ax.plot(x, y)
ax.hist(cov_array)
ax.set_ylabel("Count")
ax.set_xlabel("Coverage")
plt.savefig("Cov5x.png")

count = 0
for each in cov_array:
    if each == 0:
        count += 1
#print(count)

#print(y)

# Coverage of 15x
cov_array_2 = np.zeros(1000000)
for i in range(150000):
    start = np.random.randint(0, high=999900)
    for h in range(start, start+100):
        cov_array_2[h] += 1

fig, ax = plt.subplots()
x_2 = np.arange(0, 40, 1)
y_2 = poisson.pmf(x_2, 15, 0)*1000000
ax.plot(x_2, y_2)
ax.hist(cov_array_2)
ax.set_ylabel("Count")
ax.set_xlabel("Coverage")
plt.savefig("Cov15x.png")

count_2 = 0
for each in cov_array_2:
    if each == 0:
        count_2 += 1
print(count_2)

print(y_2)