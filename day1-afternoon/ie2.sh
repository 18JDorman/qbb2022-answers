# Goal: find number of SNPs in 1000genome project that intersects each gene and how many unique genes are represented

genefile=/Users/cmdb/data/bed_files/genes.bed
vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf

bedtools intersect -a $genefile -b $vcffile > intersect_out_ie2.bed

# Number of SNPs intersecting list of genes
wc -l intersect_out_ie2.bed

# Number of unique genes with SNPs
cut -f 4 intersect_out_ie2.bed | sort | uniq | wc -l

# Most common mutation from cytosine
#awk '/^#/{next} {print $4}' ~/data/vcf_files/random_snippet.vcf | sort | uniq -c
grep -v "#" ~/data/vcf_files/random_snippet.vcf | awk '{if ($4=="C") {print $5}}' | sort | uniq -c