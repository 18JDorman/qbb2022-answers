 # Question 1.1
 We would need 50,000 reads.
 
 # Question 1.3
 I had 6528 positions with 0 and we would esxpect 6738 positions so epxectations are quite similar. 
 
 # Question 1.4
 We would expect fewer than 1 (~0.3) positions with coverage of 0. In fact there were 7 sites.
 
 # Question 2.1
 There are 4 contigs.
 
 # Question 2.2
 `grep -v '>' contigs.fasta | wc` then subtract the number of lines (to remove number of new line characters).
 The total length of the contigs is 234,467 bp.
 
 # Question 2.3
 The longest contig is 105830 bp.
 
 # Question 2.4
 Half the genome is 117,233 bp. The order of lengths is 105830, 47860, 41351 then 39426. 117,233 would fall with in the second contig.
 The N50 is 47860 bp
 
 # Question 3.1
 99.98% identity using dnadiff `../ref.fa scaffolds.fasta` and checking out.report
 
 # Question 3.2
 The length of the longest alignment is 207000 bp. 
 `nucmer ../ref.fa scaffolds.fasta`
 `show-coord out.delta`
 
 # Question 3.3
 There is 1 insertion in the assembly.
 
 # Question 4.1
 The large insertion is from 26788 to 27497 (ref 26790-26787).
 
 # Question 4.2 
 The insertion is 710 bp long.
 
 # Question 4.3 
 `samtools faidx asm/scaffolds.fasta NODE_1_length_234497_cov_20.506978:26788-27498 > insertion.fasta`
  ATACAATGCGTATTGTAGTATGGCCTTACGGGAGGGCAGACGGCAAAGAGTGATCACGTTC
  TATCGGATGCAAGGCACCGCTTTATCCATTAGCCTCTTATTGGAGGAGGGCATGGCATTC
  ATACCCAATGGCTCAATTCTTTTACTACAACATTGATAACTTATCCAAGTACTCTACGAC
  CAACCTGCAGAACGGCCCACCGGCCTAACGGCATACCTCACAACTACCCTGCTAAGGCGA
  GCACTCCAGCCAAGCAAGACCACATCCACCCAAGCCCACCTCATCGCCTCAGCCAATAGC
  GCTCAGACAAAAGGAACTTATTATTAACTGAAACGCTGTACTGCGGTAAGTCCTCAACGC
  CGACCAAACGAAACCAGCAGCGTAGTCCTATCGGACTCGCTTGCACACATAACACATGCT
  TGTAGTCTTGCACGACCCCAGGCGGACATGAGTTTCTGCTGGGCGGCGAGGAGTCGAAGC
  TGCGGGCATTCCTTTCCGAAAACATGAATTACTGCGGGTATGTCCGACCTCAAACATTCG
  TACCTGAGCATATTGCTCAAGTGAGCCAGTCGGCAATTCATATCCGAAAACATGACTGTC
  TTGCATAAGGCCTCTCTTACGAGCTGAGTGCACGAACCACGGAACAGCTTAGTCACTTAG
  AAGAGTACTCTATTCGGGACTTGAAGTACGCGTGCAATCGGGAACTAGTG
  
  # Question 4.4
  `python dna-decode.py -d --input insertion.fasta`
  Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens..