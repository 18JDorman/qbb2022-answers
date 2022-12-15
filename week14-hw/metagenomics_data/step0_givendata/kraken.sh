for each in 'SRR492183' 'SRR492186' 'SRR492188' 'SRR492189' 'SRR492190' 'SRR492193' 'SRR492194' 'SRR492197'
do
#	python textEdit.py ${each}.kraken $each
#	ktImportText -q ${each}_krona.txt -o ${each}_krona.html
#	bwa mem -t 4 assembly.fasta READS/${each}_1.fastq READS/${each}_2.fastq > ${each}.sam
	samtools sort ${each}.sam -O bam -o ${each}.bam
done