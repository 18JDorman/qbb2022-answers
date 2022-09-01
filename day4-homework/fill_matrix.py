#!/usr/bin/env python

import numpy
from scipy.stats import binomtest
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multitest import multipletests
import binomial_power_interactive_lecture

probabilities = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
tosses = numpy.array([10, 50, 100, 250, 500, 1000])

new_twodim_arr = numpy.zeros((len(probabilities), len(tosses)))
for i, prob in enumerate(probabilities):
    for j,toss in enumerate(tosses):
        power = binomial_power_interactive_lecture.run_experiment(prob, toss)
        new_twodim_arr[i,j] = power

print(new_twodim_arr)