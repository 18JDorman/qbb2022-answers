#Step 1
./kraken.sh in relavant directory with unused lines commented out
There is a dynamic competition for being the dominant taxa between Firmicutes and Actinobacteria. There was also a slight dynamic in the density of phage.

#Step 2
./kraken.sh in relavant directory with unused lines commented out
Metrics like gc content and/or contig size (assuming quality assembly) could be useful.

`jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
Output depth matrix to depth.txt`
`metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin`
#Step 3
3A: There are 6 bins.
3B: They cover ~4.8% of the assembly
```
grep '>' assembly.fasta | wc -l
grep '>' bins_dir/bin.1.fa | wc -l
grep '>' bins_dir/bin.2.fa | wc -l
grep '>' bins_dir/bin.3.fa | wc -l
grep '>' bins_dir/bin.4.fa | wc -l
grep '>' bins_dir/bin.5.fa | wc -l
grep '>' bins_dir/bin.6.fa | wc -l
```
3C: It makes sense given the fact that prokaryotic genomes are generally quite small. 
3D: One way is to count the number of contigs since fewer contigs correspond to more complete assemblies. To look for contamination, we could BLAST the assemblies and look at the diversity of hits.