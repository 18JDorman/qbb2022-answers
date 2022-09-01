 # Day 4 Lunch Exercises
 
 ## Exercise 1
 ```
 *** Subsetting .vcf for each feature
 --- Subsetting exons.chr21.bed.vcf
     + Covering 1107407 bp
 --- Subsetting processed_pseudogene.chr21.bed.vcf
     + Covering 956640 bp
 --- Subsetting protein_coding.chr21.bed.vcf
     + Covering 13780687 bp
 ```
 One strategy would be to visually compare the figs which could identify broad differences. For more specific confirmation, we could use wc on each figure to make sure they have the same values. Visually, they are similar but wc indicates there are some differences in the actual files.
 I'd be interested in the miRNA, lncRNA entries as those have a lot of biological relevance but are excluded in the primary run. Another would be artifact as I'd be curious to learn more about what exactly those features are. 
 
 ## Exercise 2
 The vast majority of SNPs are rare regardless of what type of gene it's present in. 
 
 ## Exercise 3
 ```
 SYNOPSIS
 	Contains scripts to plot the probability of alleles present in given types of genes in specified regions of a genome.
 USAGE
 	bash do_all.sh <VCF file> <GTF file>
 DEPENDENCIES
	bedtools                  2.30.0  
	blas                      1.0     
	brotli                    1.0.9   
	bzip2                     1.0.8   
	ca-certificates           2022.4.2
	certifi                   2022.6.1
	cycler                    0.11.0  
	fonttools                 4.25.0  
	freetype                  2.11.0  
	giflib                    5.2.1   
	intel-openmp              2021.4.0
	jpeg                      9e      
	kiwisolver                1.4.2   
	lcms2                     2.12    
	libcxx                    14.0.6  
	libffi                    3.3     
	libpng                    1.6.37  
	libtiff                   4.2.0   
	libwebp                   1.2.2   
	libwebp-base              1.2.2   
	libzlib                   1.2.12  
	lz4-c                     1.9.3   
	matplotlib                3.5.1   
	matplotlib-base           3.5.1   
	mkl                       2021.4.0
	mkl-service               2.4.0   
	mkl_fft                   1.3.1   
	mkl_random                1.2.2   
	munkres                   1.1.4   
	ncurses                   6.3     
	numpy                     1.22.3  
	numpy-base                1.22.3  
	openssl                   1.1.1o  
	packaging                 21.3    
	pillow                    9.0.1   
	pip                       21.2.4  
	pyparsing                 3.0.4   
	python                    3.10.4  
	python-dateutil           2.8.2   
	readline                  8.1.2   
	setuptools                61.2.0  
	six                       1.16.0  
	sqlite                    3.38.5  
	tk                        8.6.12  
	tornado                   6.1     
	tzdata                    2022a   
	wheel                     0.37.1  
	xz                        5.2.5   
	zlib                      1.2.12  
	zstd                      1.5.2
 DESCRIPTION
	1. Check for presence of VCF and GTF files and provide error message if not present
    2. Generate a BED file of the relevant gene features from the GTF file
			Isolate genomic region of interest (eg. chromosome 21) from the GTF file and output to a new GTF file.
			Provide the gene features of interest in the for loop then isolate the lines containing those "gene_type"s from the GTF file. 
			Convert that data to a bed file using awk.
	3. Use bedtools to calculate and print the size of the genome that each gene feature of interest covers. 
			Then subset the vcf file for the SNPs that occur in the gene features of interest also using bedtools.
	4. For each gene feature, plot the probability density of SNPs occuring in each gene feature of interest.
			Loop through the vcf subsetted file and isolate the allele count values for each SNP.
			Use numpy to log transform that data and then use matplotlib hist() to plot a histogram of that data in a probabiity density.
			Save that figure as a separate file for each gene feature. 
 OUTPUT
 	Subsetted .bed, .vcf, and .png files of hitograms for each gene feature. Also outputs a subsetted .gtf file of the genome region of interest.
 ```
 


