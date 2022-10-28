#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

in1_fname = sys.argv[1]
data = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))

data_pos = numpy.where( (data['F1'] >= 54878) & (data['F2'] <= 54951) )
data_filtered = (data[data_pos])
data_filtered['score'] = numpy.log( data_filtered['score'])
data_filtered['F1'] = data_filtered['F1'] - 54878
data_filtered['F2'] = data_filtered['F2'] - 54878

data_filtered['score'] =  data_filtered['score'] - numpy.min(data_filtered['score'])

mat = numpy.zeros( [54951 - 54878 + 1, 54951 - 54878 + 1] )
mat[data_filtered['F1'], data_filtered['F2']] = data_filtered['score']
mat[data_filtered['F2'], data_filtered['F1']] = data_filtered['score']

insulation_scores = []
nt_list = []
for i in range(5, 54951 - 54878 + 1) :
    insulation_scores.append(numpy.mean(mat[(i - 5):i, i:(i + 5)]))

nt_list = numpy.linspace(10400000, 13400000, len(insulation_scores))
fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
ax[0].axis('off')
plt.margins(x=0)
ax[1].set_xlim(10400000, 13400000)
plt.subplots_adjust(left=0.15,
                bottom=0.1,
                right=1.0,
                top=1.0,
                wspace=0.4,
                hspace=0.0)
ax[0].imshow(mat,cmap='magma')
ax[1].scatter(nt_list, insulation_scores)
fig.tight_layout()
plt.show()