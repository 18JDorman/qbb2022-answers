# day 4 homework feedback

Great heatmaps!

Good observations/comments throughout your README! One small point is that for the real study, it's not necessarily that a sperm's allele is either wild type or mutant. Rather is it just allele version 1 or allele version 2 when the donor had two possible alleles (was a heterozygote for that allele)

In general, if you have a lot of code in a repo, try to add a note on how the code relates to each other (preferably in a README file); essentially, tell someone looking at your repo that `binomial_power_interactive_lecture.py` is the main script

The assignment does ask you to incorporate the nested for loop and storing the power within the `run_experiment()` function rather than calling that function repeatedly. What you've done works and leads to the same conclusions, but consider how you might edit the function to incorporate the new code. While your results will be the same every time your script is run, will your results be the same compared to someone who only calls the `run_experiment()` function once therefore only sets the random seed once?
