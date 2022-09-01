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
 SYNOPSIS
 	Contains scripts to plot the probability of alleles present in given types of genes in specified regions of a genome.
 USAGE
 	bash do_all.sh <VCF file> <GTF file>
 DESCRIPTION
```
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
 ```


