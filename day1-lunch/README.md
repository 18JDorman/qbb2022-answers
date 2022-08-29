 # QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn more python techniques for genomic analysis.
 
 # Exercise 2.C
 ```
 cd ~/qbb2022-answers/day1-lunch
 wc -l exons.chr21.bed
 wc -l genes.chr21.bed 
 ```
 ```
 Number of lines in genes.chr21.bed=219
 Number of lines in exons.chr21.bed=13653
 Average number of exons per gene=13563/219=62.3
 ```
 
 # Exercise 2.C
 You would need to use the start and stop positions from the gene bed file as conditions to filter the exons bed file. For each gene, you would subset the exons by the number of exons in between each gene bed file range. Then you could use wc on each exon subset, output that to a file, sort that file, and take the values in the middle of the file.
 
 # Exercise 3.B
 `sort -k 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | cut -f 4 | uniq -c`
 ```
  Count State
  305 1
   17 10
   17 11
   30 12
   62 13
  228 14
  992 15
  678 2
   79 3
  377 4
  808 5
  148 6
 1050 7
  156 8
  654 9
```

 # Exercise 3.C
 For each state, you could subset the bed file by lines belonging to that state. Then on each subset, you could loop through each line, take the difference between each start and stop point, and sum each of those values. Then choose the max sum.
 
 # Exercise 4.B
 ```
 cut -f 3 integrated_call_samples.panel | grep AFR | wc -l
 1044
 ```
 
 # Exercise 4.C
 You could run uniq on a sorted column 3, output that to a list of some kind, then use a for loop to run through each list entry, and run the same grep-wc pipe for each. 
 
 # Exercise 5.B
 `cut -f 1-8,13 random_snippet.vcf > HG00100.vcf`
 
 # Exercise 5.C
 `cut -f 9 HG00100.vcf | sort | uniq -c`
 ```
 Count Value
 9514 0|0
  127 0|1
  178 1|0
  181 1|1
 ```
 # Exercise 5.D
 `grep AF=1 HG00100.vcf | wc -l`
 ```
 34
 ```
 
 # Exercise 5.E
 Six times, AF, EAS_AF, EUR_AF, AFR_AF, AMR_AF, and SAS_AF
 
 # Exercise 5.F
 You could extract column 8 and output that to a separate file. Then on that file you could separate values by ';' and extract whatever column that would put AFR-AF in (column 7 I believe).
 
 # Just for Fun.A
 `cut -f 4,5 random_snippet.vcf | sort | uniq -c`
 ```
  354 A	C
 1315 A	G
  358 A	T
  484 C	A
  384 C	G
 2113 C	T
 2041 G	A
  405 G	C
  485 G	T
  358 T A
  1317 T C
  386 T G
  The most common mutation is C to T
  ```
 # Just for Fun.B
 `cut -f 8 random_snippet.vcf | cut -d ';' -f 7`
 
 # Just for Fun.C
 `cut -f 8 random_snippet.vcf | cut -d ';' -f 7 | sort | uniq | wc -l`
 There are 102 values including 0 but subtracting 19 from the output of the previous command (since the header and comments are included in the count).
 
 # Just for Fun.D
 `cut -f 8 random_snippet.vcf | cut -d ';' -f 11 | sort | uniq`
 There is only one value for NC (2548).
 