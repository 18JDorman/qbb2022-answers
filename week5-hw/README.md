## Part 1
### Step 1
```
for each in *.bam
do 
samtools view -b -q 10 $each > ${each}_filt
done
```

### Step 2
```
macs2 callpeak -t D2_Sox2_R1.bam_filt -c D2_Sox2_R1_input.bam_filt -f BAM -B -g 8.3e+7 --outdir Sox2_R1
macs2 callpeak -t D2_Sox2_R2.bam_filt -c D2_Sox2_R2_input.bam_filt -f BAM -B -g 8.3e+7 --outdir Sox2_R2
```

### Step 3
`bedtools intersect -a Sox2_R1/NA_peaks.narrowPeak -b Sox2_R2/NA_peaks.narrowPeak > commonPeaks.bed`

### Step 4
```
bedtools intersect -a D2_Klf4_peaks.bed -b commonPeaks.bed > Klf4_Sox2_peaks.bed
wc -l Klf4_Sox2_peaks.bed
wc -l D2_Klf4_peaks.bed
```
There are 40 overlapping peaks and 60 total peaks for Klf4 so ~66% of peaks colocalize with Sox2.

### Step 5
Run the python scripts on all 4 bdg files
```
for each in *.bdg
do
python scale_bdg.py $each ${each}_filt
done
```

Crop all filtered bdg files
```
for each in *.bdg_filt
do
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' $each > ${each}_crop
done
```

Run Python script to get plots
`python peak_bar.py *.bdg_filt_crop`

## Part2
### Steps 1,2,3
`sort -k5,5rn commonPeaks.bed | head -n 300 | awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > Sox2_commonP_form`

### Step 4
`samtools faidx mm10.fa -r Sox2_commonP_form > Sox2_peaks.fa`

### Step 5
`meme-chip -maxw 7 Sox2_peaks.fa`

## Part 3
```
tomtom memechip_out/combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
grep 'SOX2' tomtom_out/tomtom.tsv > SOX2_KLF4_Hits.tsv
grep 'KLF4' tomtom_out/tomtom.tsv >> SOX2_KLF4_Hits.tsv
```

