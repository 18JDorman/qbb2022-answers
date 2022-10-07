#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Step 2
pca_vals = np.genfromtxt('all_vcf.eigenvec', dtype = None, encoding = None, 
                            names = ["Name1", "Name2", "PCA1", "PCA2", "PCA3", "PCA4","PCA5", "PCA6", "PCA7", "PCA8", "PCA9", "PCA10"])
maf = np.genfromtxt('plink.frq', dtype = None, encoding = None)
x = []
y = []
for each in pca_vals:
    x.append(each[2])
    y.append(each[3])
fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
ax.set_title("PCA")
fig.savefig("PCA.png")
#plt.show()

# Step 3
maf_val = []
for each in maf[1:]:
    maf_val.append(float(each[4]))

fig, ax = plt.subplots()
ax.hist(maf_val)
ax.set_ylabel("Count")
ax.set_xlabel("Allele Freq")
ax.set_title("Allele Frequency Distribution")
fig.savefig("Freq_Hist.png")
#plt.show()

# Step 5 for GS451
file = open("GS451.assoc.linear")
bp_G = []
pval_G = []
chrom_G = []
pvalRaw_G = []
for line in file:
    new = line.rstrip("\n").split() 
    if new[4] == "ADD": 
        bp_G.append(int(new[2])) 
        pval_G.append(-1 * np.log10(float(new[8])))
        pvalRaw_G.append(float(new[8]))
        chrom_G.append(int(new[0])) 
pos_G = []
for i, item in enumerate(bp_G):
    pos_G.append(i)

sigpval_G = []
sigpos_G = []
for p, item in enumerate(pval_G): 
    if item > 5:
        sigpval_G.append(item)
        sigpos_G.append(pos_G[p]) 
xtick_G = []
for i in range(1, 23):
    first_pos = None
    last_pos = None
    for c, item in enumerate(chrom_G):
        if item == i:
            if first_pos == None:
                first_pos = c
            if last_pos == None or c > last_pos: 
                last_pos = c
    middle = (last_pos + first_pos)/2
    xtick_G.append(middle)

fig, ax = plt.subplots(figsize = (10, 6)) 
ax.scatter(pos_G, pval_G)
ax.scatter(sigpos_G, sigpval_G, color = "red")
ax.set_xticks(xtick_G)
ax.set_xticklabels(range(1, 23))
ax.set_xlabel("Chrom Position")
ax.set_ylabel("-log10(pval)")
ax.set_title("Manhattan GS451")
fig.savefig("GS451_Manhat.png")
#plt.show()

# Step 5 for CB1908
file = open("CB1908.assoc.linear")
bp_C =[]
pval_C = []
chrom_C = []
snp_C = []
pvalRaw_C = []
for line in file:
    new = line.rstrip("\n").split() 
    if new[4] == "ADD": 
        bp_C.append(int(new[2])) 
        pval_C.append(-1 * np.log10(float(new[8])))
        pvalRaw_C.append(float(new[8]))
        chrom_C.append(int(new[0])) 
        snp_C.append(new[1])

pos_C = []
for i, item in enumerate(bp_C):
    pos_C.append(i)

sigpval_C = []
sigpos_C = []
for p, item in enumerate(pval_C): 
    if item > 5:
        sigpval_C.append(item)
        sigpos_C.append(pos_C[p]) 
xtick_C = []
for i in range(1, 23):
    first_pos = None
    last_pos = None
    for c, item in enumerate(chrom_C):
        if item == i:
            if first_pos == None:
                first_pos = c
            if last_pos == None or c > last_pos: 
                last_pos = c
    middle = (last_pos + first_pos)/2
    xtick_C.append(middle)

fig, ax = plt.subplots(figsize = (10, 6)) 
ax.scatter(pos_C, pval_C)
ax.scatter(sigpos_C, sigpval_C, color = "red")
ax.set_xticks(xtick_C)
ax.set_xticklabels(range(1, 23))
ax.set_xlabel("Chrom Position")
ax.set_ylabel("-log10(pval)")
ax.set_title("Manhattan CB1908")
fig.savefig("CB1908_Manhat.png")
#plt.show()

print(min(pvalRaw_G))
print(min(pvalRaw_C))

# Step 6
ref = []
het = []
alt = []
min_val = min(pval_C) 
position = pval_C.index(min_val) 
significant = snp_C[position] 
sigbp = bp_C[position]
sigchrom = chrom_C[position]
genotypes = []
sampleid = []

gen_file = open("genotypes.vcf")
phen_file = open("CB1908_IC50.txt")
for i in gen_file:
    if i.startswith("##"): 
        continue
    gen_list = i.rstrip("\n").split("\t")
    if gen_list[2] == significant:
        genotypes = gen_list[9:]
    if i.startswith("#"):
        sampleid = gen_list[9:]
new_dict = dict(zip(sampleid, genotypes))
for i in phen_file:
    if i.startswith("F"):
        continue
    phen_list = i.rstrip("\n").split("\t")
    id_A = phen_list[0]
    id_B = phen_list[1]
    combined =id_A + "_" + id_B
    if phen_list[2] == "NA":
        continue
    sample_val =float(phen_list[2])
    gt = new_dict[combined]
    if gt == "0/0":
        ref.append(sample_val)
    if gt == "0/1":
        het.append(sample_val)
    if gt == "1/1":
        alt.append(sample_val)

fig, ax = plt.subplots()
ax.boxplot([ref, het, alt])
ax.set_xlabel("Genotype")
ax.set_ylabel("Phenotype")
plt.xticks([1, 2, 3], ["Hom_Ref", "Het", "Hom_Alt"])
fig.savefig("CB1908_box.png")
plt.show()
