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
 ### Output
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
 