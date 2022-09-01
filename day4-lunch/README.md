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