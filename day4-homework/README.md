 # Day 4 Homework
 ## Exercise 1.A
 Probs becomes a list of floats going from 0.55 to 1 at a step interval of 0.05. Around() rounds off rhe values to 2 places. It makes the values more readable downstream. [::-1] reverses the order of the list. 
 
 ## Exercise 1.C
 P-value correction has a drastic impact on power, particularly with 10 tosses. After that, the impact is not as distinct particularly at the extremes of probabilities. When at one of the extremes (high probability or many tosses) the other variable has little to no impact. Beyond combinations of (50, 0.75), (100, 0.7), or (250, 0.6), increasing variables become redundant and there is little to no increase in power. 
 
 ## Exercise 1.D
 The goal of this experiment is to assess if Mendel's Law of Segregation holds at high resolution. They used singel-cell data from sperm to assess if certain alleles have a higher probability of being transmitted to offspring. Theoretically there should be an equal probability of inheriting either allele from a heterozygote but if there isn't, that allele can experience "transmisssion distortion."
 Unlike with coin toss simulation, even small populations of sperm can have power at relatively lower transmission  rates (~0.65). There is some similarity in that correction has drastic impacts on power. Prob_heads has the highest correlation to transmission rate whereas number of sperm corresponds to number of tosses. Transmission rate use a binomial test because a sperm's allele can be either wildtype or mutatnt (similar to how a coin can be heads or tails).