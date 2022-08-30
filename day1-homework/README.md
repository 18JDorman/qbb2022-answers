 # QBB2022 - Day 1 - Homework Exercises Submission
 
 ## Exercise 1
 ### Error:
 ```
 Considering  A
 awk: illegal field $(), name "nuc"
  input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
  source line number 1
 Considering  C
 awk: illegal field $(), name "nuc"
  input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
  source line number 1
 Considering  G
 awk: illegal field $(), name "nuc"
  input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
  source line number 1
 Considering  T
 awk: illegal field $(), name "nuc"
  input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
  source line number 1\
 ```
 ### Correct Code:
 ```
 for nuc in A C G T
 do
   echo "Considering " $nuc
   awk -v nucl=$nuc '/^#/{next} {if ($4 == nucl) {print $5}}' $1 | sort | uniq -c
 done
 ```
 ### Output:
 ```
 Considering  A
  354 C
 1315 G
  358 T
 Considering  C
  484 A
  384 G
 2113 T
 Considering  G
 2041 A
  405 C
  485 T
 Considering  T
  358 A
 1317 C
  386 G
  
  This makes biological sense as transitions are far more probable than transversions.
  ```
  ## Exercise 2
  ### Code:
  ```
  grep -Ew '1|2|10|11' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > promoters.bed #I selected all regions with a TSS
  bedtools intersect -a ~/data/vcf_files/random_snippet.vcf -b ./promoters.bed > intersect_out_ex2.bed
  grep -v "#" intersect_out_ex2.bed | awk '{if ($4=="C") {print $5}}' | sort | uniq -c
  ```
  ### Output:
  ```
  12 A
  11 G
  39 T
  ```
  ### Significance:
  I took a conservative approach and chose only TSS's as those are the only that to me are unambiguously promoters. These are not well defined since they are named by features but without a clear definition of what features constitute a promoter. In addition, most seem to be in exact mutliples of 200. That is quite arbitrary and is likely not relfective of natural states.
  The bias towards transitions does not seem as extreme as in the promoters as the overall genome (1:~3 instead of 1:~5) so I would hypothesize that the promoters are under greater selective pressure and are broadly more intolerant to mutation.
  
  ## Exercise 3
  ### Code Summary
  The first line, awk, converts the vcf file to a bed file which closest needs to function. The second line, sort, reorders the genes bed so that they are in order by chromosome and start position. Finally, bedtools performs the closest function with the variant and gene beds. Bedtools closest requires both bed files to be sorted by chromosome and start position to function.
  ### Error 1:
  ```
  Error: unable to open file or unable to determine types for file variants.bed
  ```
  ### Solution 1:
  Include tab delimiting in the new bed file via the awk function
  
  ### Error 2:
  ```
  Error: Sorted input specified, but the file variants.bed has the following out of order record
  chr21	5218156	5218157
  ```
  ### Solution 2:
  Sort the variants bed just as the genes bed was sorted.
  
  ### Variants:
  ```
  Number of variants using wc: 10293
  Number of unique genes using cut -f 7 intersect_out_ex2.bed | sort | uniq | wc -l: 200
  Variants per gene: 51.5
  ```
  
  ## Exercise 4
  ### Code Summary:
  Line one gets the intersection of genes with H3K27ac only. Line two finds intersections with just H3K9me3. Line three uses grep to exlucde entries from H3K27ac output in H3K9me3 output.
  
  ### Syntax:
  The syntax error is that the bedtools functions reference files that are not in the directory where the script is operated. The solution is to include the paths into the script. The logic error is that the acetylation output is being used to exclude methylation genes but we are interested in what is only in the acetylation output. The solution is to flip the two input orders. 

