#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

#pcas_vcf = np.genfromtxt('all_vcf.eigenvec', dtype = None, encoding = None, 
#                                names = ["Name1", "Name2", "PCA1", "PCA2", "PCA3"])
pca_meta = np.genfromtxt('joined_eigen_meta.txt', dtype = None, encoding = None, names = ["Name1", "Name2", "PCA1", "PCA2", "PCA3", "Pop", "Superpop", "Gender"])

fig, ax = plt.subplots()
genders = np.unique(pca_meta["Gender"])
print(genders)
for each in genders:
    x=[]
    y=[]
    for thing in pca_meta:
        if each == thing[7]:
            x.append(thing[2])
            y.append(thing[3])
    ax.scatter(x,y, label = each)
    ax.legend()
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
ax.set_title("PCA with Gender")
plt.show()

fig, ax = plt.subplots()
pops = np.unique(pca_meta["Pop"])
for each in pops:
    x=[]
    y=[]
    for thing in pca_meta:
        if each == thing[5]:
            x.append(thing[2])
            y.append(thing[3])
    ax.scatter(x,y, label = each)
    ax.legend()
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
ax.set_title("PCA with Populations")
plt.show()

fig, ax = plt.subplots()
superpops = np.unique(pca_meta["Superpop"])
for each in superpops:
    x=[]
    y=[]
    for thing in pca_meta:
        if each == thing[6]:
            x.append(thing[2])
            y.append(thing[3])
    ax.scatter(x,y, label = each)
    ax.legend()
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
ax.set_title("PCA with Superpopulations")
plt.show()

fig, ax = plt.subplots()
ax.scatter(pcas_vcf["PCA1"], pcas_vcf["PCA2"], c=pca_meta["Pop"])
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
plt.show()