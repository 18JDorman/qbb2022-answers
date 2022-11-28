import scanpy as sc

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

#Step 1
sc.tl.pca(adata)
#sc.pl.pca(adata)

sc.pp.recipe_zheng17(adata)

sc.tl.pca(adata)
#sc.pl.pca(adata)

#Step 2
sc.pp.neighbors(adata)
sc.tl.leiden(adata)
#sc.tl.umap(adata, maxiter=1000)
#sc.pl.umap(adata, color='leiden')

#sc.tl.tsne(adata)
#sc.pl.tsne(adata, color='leiden')

#Step 3
sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)

sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)
