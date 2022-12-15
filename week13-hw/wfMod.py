#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Step 1
def wf_sim(al_freq, pop):
    al_freq_list = [al_freq]
    while (al_freq != 1) and (al_freq != 0):
        sample = np.random.binomial(n=pop, p=al_freq)
        al_freq = sample/pop
        al_freq_list.append(al_freq)
    return al_freq_list

allele=wf_sim(0.9, 1000)

#Step 2
def lineplot(allele):
    x=range(len(allele))
    plt.plot(x, allele)
    plt.xlabel('Generation')
    plt.ylabel('Allele Frequency')
    plt.title('Allele Frequency of 0.9 and Population of 1000')
    plt.show()

lineplot(allele)

#Step 3
sims = []
for each in range(1000):
    sims.append(len(wf_sim(0.5, 100)))

plt.hist(sims)
plt.xlabel('Generations to Fix')
plt.ylabel('Count')
plt.show()

#Step 4
fix_time = []
x=[100, 1000, 10000, 100000, 1000000, 10000000]
for each in x:
    fix_time.append(len(wf_sim(0.5, each)))
plt.plot(x, fix_time)
plt.xlabel('Population')
plt.ylabel('Time to Fix')
plt.show()

#Step 5
df = {'AlFreq': [], 'FixTimes': []}
fix_time_df =  pd.DataFrame(df)
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
for each in x:
    df = {'AlFreq': [each]*100, 'FixTimes': np.zeros(100)}
    fixed = pd.DataFrame(df)
    for thing in range(100):
        fixed.loc[thing, 'FixTimes']=len(wf_sim(each, 1000))
    fix_time_df = pd.concat([fix_time_df, fixed], axis=0)
    
sns.stripplot(y="FixTimes", x="AlFreq", data=fix_time_df)
plt.title('Population Size of 1000')
plt.show()
