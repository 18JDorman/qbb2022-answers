# Part 1
```
medaka_variant -i methylation.bam -f hg38.fa -r chr11:1900000-2800000 -p region_1.vcf -o region_1
medaka_variant -i methylation.bam -f hg38.fa -r chr14:100700000-100990000 -p region_2.vcf -o region_2
medaka_variant -i methylation.bam -f hg38.fa -r chr15:23600000-25900000 -p region_3.vcf -o region_3
medaka_variant -i methylation.bam -f hg38.fa -r chr20:58800000-58912000 -p region_4.vcf -o region_4
```

# Part 2
```
whatshap haplotag -o region1_hap.bam -r hg38.fa --regions chr11:1900000:2800000 --output-haplotag-list region1_haplotagList region_1/region_1.vcf.gz methylation.bam
whatshap haplotag -o region2_hap.bam -r hg38.fa --regions chr14:100700000:100990000 --output-haplotag-list region2_haplotagList region_2/region_2.vcf.gz methylation.bam
whatshap haplotag -o region3_hap.bam -r hg38.fa --regions chr15:23600000:25900000 --output-haplotag-list region3_haplotagList region_3/region_3.vcf.gz methylation.bam
whatshap haplotag -o region4_hap.bam -r hg38.fa --regions chr20:58800000:58912000 --output-haplotag-list region4_haplotagList region_4/region_4.vcf.gz methylation.bam
```

# Part 3
```
whatshap split --output-h1 region1_hap1.bam --output-h2 region1_hap2.bam region1_hap.bam region1_haplotagList
whatshap split --output-h1 region2_hap1.bam --output-h2 region2_hap2.bam region2_hap.bam region2_haplotagList
whatshap split --output-h1 region3_hap1.bam --output-h2 region3_hap2.bam region3_hap.bam region3_haplotagList
whatshap split --output-h1 region4_hap1.bam --output-h2 region4_hap2.bam region4_hap.bam region4_haplotagList
samtools cat *_hap1.bam > Hap1s.bam
samtools cat *_hap2.bam > Hap2s.bam
samtools index -b Hap1s.bam
samtools index -b Hap2s.bam
```

# Part 6
No because the software does not know which methylation patterns correspond to maternal or paternal genotypes so has not way to group them across phasings. This is reflected in the data where sometimes H1 has the maternal genotype and sometimes that paternal.