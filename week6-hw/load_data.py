#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors


# in1_fname should be ddCTCF
# in2_fname should be dCTCF
# bin_fname should be bed file with bin locations

in1_fname, in2_fname, bin_fname = sys.argv[1:4]
data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
    ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

chrom = b'chr15'
start = 11170245
end = 12070245
start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                     (frags['start'] <= start) &
                                     (frags['end'] > start))[0][0]]
end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                   (frags['start'] <= end) &
                                   (frags['end'] > end))[0][0]] + 1

def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2
    
def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat

# Begin my changes to script    
def filter_data(data):
    data_filt = data[numpy.where((data['F1'] >= start_bin) & (data['F2'] <= end_bin))]
    data_filt['score'] = numpy.log2(data_filt['score'])
    data_filt['score'] = data_filt['score'] - numpy.amin(data_filt['score'])
    mat=numpy.zeros((end_bin - start_bin+1, end_bin - start_bin+1))
    for i in range(len(data_filt['score'])):
        mat[data_filt['F1'][i] - start_bin, data_filt['F2'][i] - start_bin] = data_filt['score'][i]
        mat[data_filt['F2'][i] - start_bin, data_filt['F1'][i] - start_bin] = data_filt['score'][i]
    return mat

mat1 = filter_data(data1)
mat2 = filter_data(data2)
max_score = max(numpy.amax(mat1), numpy.amax(mat2))
mat1 = remove_dd_bg(mat1)
mat1 = smooth_matrix(mat1)
mat2 = remove_dd_bg(mat2)
mat2 = smooth_matrix(mat2)
mat3 = mat2-mat1

fig, ax = plt.subplots(3)
ax[0].imshow(mat1, vmax = max_score, cmap = 'magma')
ax[1].imshow(mat2, vmax = max_score, cmap = 'magma')
ax[2].imshow(mat3, cmap = 'seismic')
plt.show()
