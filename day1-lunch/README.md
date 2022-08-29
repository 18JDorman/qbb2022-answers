 # QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn more python techniques for genomic analysis.
 
 # Exercise 2 Commands
 cd ~/qbb2022-answers/day1-lunch
 
 wc -l exons.chr21.bed
 
 wc -l genes.chr21.bed 
 
 # Exercise 2 Output
 Number of lines in genes.chr21.bed=219
 
 Number of lines in exons.chr21.bed=13653
 
 Average number of exons per gene=13563/219=62.3
 
 # Exercise 2 Median
 You would need to use the start and stop positions from the gene bed file as conditions to filter the exons bed file. For each gene, you would subset the exons by the number of exons in between each gene bed file range. Then you could use wc on each exon subset, output that to a file, sort that file, and take the values in the middle of the file.