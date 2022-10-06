 # Step 2
 plink --vcf genotypes.vcf --allow-extra-chr --pca 10 --out all_vcf
 'python gwas.py'
 
 # Step 3
 plink --vcf genotypes.vcf --freq
 
 # Step 4 
 plink --vcf genotypes.vcf --assoc --pheno CB1908_IC50.txt --allow-no-sex --covar all_vcf.eigenvec --linear
 plink --vcf genotypes.vcf --assoc --pheno GS451_IC50.txt --allow-no-sex --covar all_vcf.eigenvec --linear