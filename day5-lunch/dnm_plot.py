#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats

dnm_combo = np.genfromtxt("dnm_combo.csv", delimiter = ",", dtype = None, encoding = None, 
                        names = ["Proband_id","Mother_count","Father_count","Father_age","Mother_age"])

# Mom age vs dNM
fig, ax = plt.subplots()
ax.scatter(dnm_combo["Mother_age"], dnm_combo["Mother_count"])
ax.set_title("Mother Age vs dNM")
ax.set_ylabel("Mother Age")
ax.set_xlabel("de Novo Mutation Count")
#plt.savefig("ex2_a_momAge.png")

# Dad age vs dNM
fig, ax = plt.subplots()
ax.scatter(dnm_combo["Father_age"], dnm_combo["Father_count"])
ax.set_title("Father Age vs dNM")
ax.set_ylabel("Father Age")
ax.set_xlabel("de Novo Mutation Count")
#plt.savefig("ex2_b_dadAge.png")

# Mom OLS
mom_model = smf.ols(formula = "Mother_count ~ 1 + Mother_age", data = dnm_combo).fit()
#print(mom_model.summary())
#print(mom_model.pvalues)

# Dad OLS
dad_model = smf.ols(formula = "Father_count ~ 1 + Father_age", data = dnm_combo).fit()
#print(dad_model.summary())
#print(dad_model.pvalues)

# DNM Histogram
fig1, ax3 = plt.subplots()
ax3.hist(dnm_combo["Father_count"], alpha = 0.5, label = "Father")
ax3.hist(dnm_combo["Mother_count"], alpha = 0.5, label = "Mother")
ax3.set_xlabel("Mutations per Proband")
ax3.set_ylabel("Number of Probands")
ax3.legend()
ax3.set_title("Distribution of dNMs per Proband")
#plt.savefig("ex2_c_dnmHist.png")

# Maternally vs paternally
#print(stats.ttest_rel(dnm_combo["Mother_count"], dnm_combo["Father_count"]))

# Prediction
print(10.3263 + 50.5 * 1.3538)