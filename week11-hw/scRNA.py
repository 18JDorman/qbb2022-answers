import scanpy as sc

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

#Step 1
sc.tl.pca(adata)
sc.pl.pca(adata)

sc.pp.recipe_zheng17(adata)

sc.tl.pca(adata)
sc.pl.pca(adata)

#Step 2
sc.pp.neighbors(adata)
sc.tl.leiden(adata)
sc.tl.umap(adata, maxiter=1000)
sc.pl.umap(adata, color='leiden')

sc.tl.tsne(adata)
sc.pl.tsne(adata, color='leiden', add_outline=True, legend_loc='on data')

#Step 3
sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)

sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save = "rank_genes.png")



#Step 4
genes = adata.var.gene_ids.index
print(genes[131:150])
ctss=microglia
col3a1=fibroblast
ackr3=endothelial cell
prox1=horizontal cells
Hbb-bt=neutrophils
Cd93=adipocytes
markers = ['Ctss', 'Col3a1', 'Ackr3', 'Prox1', 'Hbb-bt', 'Cd93']
for each in markers:
    sc.pl.tsne(adata, color=each)
    
cell_labels = {
    '0': '',
    '1': 'endothelial_cell',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': '',
    '10': '',
    '11': '',
    '12': 'horizontal_cell',
    '13': '',
    '14': 'neutrophil',
    '15': '',
    '16': '',
    '17': '',
    '18': '',
    '19': '',
    '20': 'adipocyte',
    '21': '',
    '22': 'fibroblast',
    '23': 'microglia',
    '24': '',
    '25': '',
    '26': ''
}

adata.obs['cell type'] = adata.obs['leiden'].map(cell_labels).astype('category')
sc.pl.tsne(adata, color='cell type', legend_loc='on data')