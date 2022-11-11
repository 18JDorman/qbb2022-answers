#!/usr/bin/env python3

import numpy as np
import numpy.lib.recfunctions as rfn
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats import multitest

# Step 0
input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = list(input_arr.dtype.names)
row_names = input_arr[col_names[0]]
fpkm_val = input_arr[col_names[1:]]
names = col_names[1:]
fpkm_values_2d = rfn.structured_to_unstructured(fpkm_val, dtype=float)
meds = np.median(fpkm_values_2d, axis=1)
fpkm_values_2d_sub = fpkm_values_2d[np.where(meds>0)]
fpkm_values_2d_log = np.log2(fpkm_values_2d_sub + 0.1)

# Step 1
link1 = linkage(fpkm_values_2d_log)
index1 = leaves_list(link1)
link2 = linkage(fpkm_values_2d_log.T)
index2 = leaves_list(link2)

rearr = fpkm_values_2d_log[index1,:]
rearr = rearr[:,index2]

fig, ax = plt.subplots()
plt.imshow(rearr, interpolation ='nearest', aspect = 'auto')
ax.set_xticks(np.arange(len(names)))
ax.set_xticklabels(np.array(names)[index2], rotation=90)
plt.colorbar()
#plt.show()

fig, ax = plt.subplots()
dendrogram(link2, distance_sort='ascending', labels=names, leaf_rotation=45)
plt.tight_layout()
#plt.show()

# Step 2
pvals = []
betas = []
for each in range(fpkm_values_2d_log.shape[0]):
    tuples = []
    for thing in range(len(names)):
        fpkm = fpkm_values_2d_log[each, thing]
        one_name = names[thing]
        name_split = one_name.split('_')
        stage = name_split[1]
        sex = name_split[0]
        tuples.append((fpkm, sex, stage))
    big_df = np.array(tuples, dtype=[('fpkm', float), ('sex', 'S6'), ('stage', int)])
    fit = smf.ols('fpkm ~ stage', data = big_df).fit()
    p_val = fit.pvalues['stage']
    beta = fit.params['stage']
    pvals.append(p_val)
    betas.append(beta)

fig, ax = plt.subplots()
sm.qqplot(np.array(pvals), dist=stats.uniform, line='45')
plt.show()

fdrs = multitest.multipletests(pvals, alpha=0.1, method='fdr_bh')
pvals = fdrs[0]
sigs = fpkm_values_2d_sub[pvals]

pvals2 = []
betas2 = []
for each in range(fpkm_values_2d_log.shape[0]):
    tuples = []
    for thing in range(len(names)):
        fpkm = fpkm_values_2d_log[each, thing]
        one_name = names[thing]
        name_split = one_name.split('_')
        stage = name_split[1]
        sex = name_split[0]
        tuples.append((fpkm, sex, stage))
    big_df = np.array(tuples, dtype=[('fpkm', float), ('sex', 'S6'), ('stage', int)])
    fit = smf.ols('fpkm ~ stage', data = big_df).fit()
    p_val2 = fit.pvalues['stage']
    beta2 = fit.params['stage']
    pvals2.append(p_val2)
    betas2.append(beta2)

fdrs2 = multitest.multipletests(pvals, alpha=0.1, method='fdr_bh')
pvals2 = fdrs2[0]
sigs2 = fpkm_values_2d_sub[pvals2]

commons = set(sigs) & set(sigs2)
num_transcripts = len(commons)
num_trans_nosex = len(sigs)
comparison = num_transcripts / num_trans_nosex * 100

colors = []
for each in pvals2:
    if each == True:
        colors.append('red')
    else:
        colors.append('black')

fig, ax = plt.subplots()
ax.scatter(betas2, -np.log10(pvals2), color = colors)
plt.show()