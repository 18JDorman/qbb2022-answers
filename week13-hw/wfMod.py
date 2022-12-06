#!/usr/bin/env python3

import numpy as np

def wf_sim(al_freq, pop):
    al_freq_list = []
    while al_freq != 1 or al_freq != 0:
        num_al = al_freq*pop
        p_A = num_al/(2*pop)
        sample = np.random.binomial(n=num_al, p=p_A)
        al_freq = sample/pop
        al_freq_list.append(al_freq)
    return al_freq_list

print(wf_sim(0.3, 100))