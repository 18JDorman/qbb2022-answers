 # Step 2
 plink --vcf genotypes.vcf --allow-extra-chr --pca 10 --out all_vcf
 'python gwas.py'
 
 # Step 3
 plink --vcf genotypes.vcf --freq
 
 # Step 4 
plink --vcf genotypes.vcf --assoc --pheno CB1908_IC50.txt --allow-no-sex --covar all_vcf.eigenvec --linear --out CB1908
plink --vcf genotypes.vcf --assoc --pheno GS451_IC50.txt --allow-no-sex --covar all_vcf.eigenvec --linear --out GS451

 # Step 7
Used the p-values printed from my python script and used the following to get SNP info:
```
grep '1.43e-07' GS451.assoc.linear 
grep '8.199e-12' CB1908.assoc.linear 
```
For GS451, a mutation in the ZNF826 gene is most associated with lymphocytopenia. This protein is a Zinc Finger Protein.
For CB1908, a mutation in the DIP2B gene which is believed to be associated with DNA methylation. 
