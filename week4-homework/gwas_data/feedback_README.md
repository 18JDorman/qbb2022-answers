Really awesome work! This is just about perfect, just one very minor issue:

1. For your boxplot, it looks like you're actually plotting the *least* significant snp. Your grabbing the SNP with the minimum value in `pval_C` but that's actually the array with your logged pvals. So you're accidently finding the the SNP that's the least significant (that's why your boxplot makes it look like there's not a strong relationship). (-0.5 point)
2. This should actually affect the SNP you pull out as the most significant, so I would have expected your answer to question 7 to be wrong as well, but the genes you listed are what I would have expected. Curious if you had another way of finding the most significant SNP, maybe with a command line tool? (no points deducted)

Very well done.

(9.5/10)
