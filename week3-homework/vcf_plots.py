#!/usr/env/python3

import matplotlib.pyplot as plt
import math
import vcfParser

vcf = vcfParser.parse_vcf("yeast_ann.vcf")
depth=[]
qual=[]
freq=[]
eff=[]
for each in vcf[1:]:
    for thing in each[9:]:
        depth.append(thing[4])
        qual.append(thing[1])
    freq.append(each[7]['AF'])
    eff_ent=each[7]['ANN']
    effs=eff_ent.split('|')
    eff.append(effs[2])

eff_dic = {}
for each in eff:
    if each in eff_dic.keys():
        eff_dic[each] += 1
    else:
        eff_dic[each] = 1

depth = [int(d) for d in depth if d != '.']
qual = [float(d) for d in qual if d != '.']
freq = [float(d) for d in freq if d != '.']

fig, axs = plt.subplots(2,2)

axs[0,0].hist(depth, density=True)
axs[0,0].set_title("Distribution of Allele Depth")
axs[0,0].set_xlabel("Depth")
axs[0,0].set_ylabel("Density")
axs[0,0].set_yscale("log")
axs[0,1].hist(qual, density=True)
axs[0,1].set_title("Distribution of Allele Quality")
axs[0,1].set_xlabel("Quality Score")
axs[0,1].set_ylabel("Density")
axs[0,1].set_yscale("log")
axs[1,0].hist(freq, density=True)
axs[1,0].set_title("Distribution of Allele Frequency")
axs[1,0].set_xlabel("Frequency")
axs[1,0].set_ylabel("Density")
axs[1,1].bar(eff_dic.keys(), eff_dic.values())
axs[1,1].set_title("Effects of Alleles")
axs[1,1].set_xlabel("Effect of Allele")
axs[1,1].set_ylabel("Count")
plt.show()