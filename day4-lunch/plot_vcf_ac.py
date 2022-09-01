#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

ac = np.log1p(ac)
fig, ax = plt.subplots()
ax.hist( ac, density=True)
ax.set_ylabel("Probability Density")
ax.set_xlabel("log(Allele Count + 1)")
ax.set_title("Distribution of Log Transformed SNP Allele Counts")
fig.savefig( vcf + ".png" )

fs.close()

