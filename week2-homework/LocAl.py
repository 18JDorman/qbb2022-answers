#!/usr/bin/env

import numpy as np
import sys
from fasta import readFASTA
import pandas as pd

# Read in FASTA Seqs using readFASTA
filename = sys.argv[1]

input_sequences = readFASTA(open(filename))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

# Import scores from command line
# For proteins, use gap -10; for nucleotides use gap -300
file = open(sys.argv[2], mode='r')
score_mat = []
for line in file:
    fields = line.rstrip().split()
    score_mat.append(fields)
col_names=score_mat[0]
row_names=[]
score_matVals=[]
for each in score_mat[1:]:
    row_names.append(each[0])
    score_matVals.append(each[1:])
score_df = pd.DataFrame(score_matVals, columns = col_names, index = row_names)
gap_penalty = float(sys.argv[3])

# Initialize F-Matrix and populate first row and column with gap penalties
F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
trace_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))

for i in range(len(sequence1)+1):
    F_matrix[i,0] = i*gap_penalty

for j in range(len(sequence2)+1):
    F_matrix[0,j] = j*gap_penalty

# Populate F-Matrix with scores
for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
        score=int(score_df.loc[sequence1[i-1], sequence2[j-1]])
        d = F_matrix[i-1, j-1] + score
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty
        F_matrix[i,j] = max(d,h,v)
        if F_matrix[i,j] == d:
            trace_matrix[i,j] = 0
        elif F_matrix[i,j] == h:
            trace_matrix[i,j] = 1
        else:
            trace_matrix[i,j] = 2

# Move through traceback matrix and record decisions
choice = []
i = len(sequence1)
j = len(sequence2)

while i >= 0 and j >= 0:
    choice.append(trace_matrix[i,j])
    if trace_matrix[i,j] == 0:
        i -= 1
        j -= 1
    elif trace_matrix[i,j] == 1:
        j -= 1
    else:
        i -= 1

# Decide alginment
align1 = []
align2 = []
choice.reverse()
i = 0
j = 0
for each in choice[1:]:
    if each == 0:
        align1.append(sequence1[i])
        align2.append(sequence2[j])
        i += 1
        j += 1
    elif each == 1:
        align1.append('-')
        align2.append(sequence2[j])
        j += 1
    else:
        align1.append(sequence1[i])
        align2.append('-')
        i += 1
        
# Print out alignment as well as scores and gaps
align1 = ''.join(align1)
align2 = ''.join(align2)
score = F_matrix[len(sequence1), len(sequence2)]
print(score)
#print("Sequence 1:",align1)
#print("Sequence 2:",align2)
gaps1 = 0
for each in align1:
    if each == '-':
        gaps1 += 1
gaps2 = 0
for each in align2:
    if each == '-':
        gaps2 += 1
print(f"Sequence 1 has {gaps1} gaps while Sequence 2 has {gaps2}")
print(f"The alignment score is {score}")
        