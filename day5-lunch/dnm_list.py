#!/usr/bin/env python3

import numpy as np

dnm_list = np.genfromtxt("dnm_list.txt", delimiter = ",", dtype = None, encoding = None, names = ["proband", "parent"])
#print(dnm_list)
probandList = np.unique(dnm_list["proband"])
#print(probandList)
print("Proband_id,Mother_Count,Father_count")
for each in probandList[:len(probandList)-1]:
    m_count = 0
    d_count = 0
    for line in dnm_list:
        if each == line[0] and line[1] == 'mother':
            m_count += 1
        if each == line[0] and line[1] == 'father':
            #print(line[1])
            d_count += 1
    print(f"{each},{m_count},{d_count}")