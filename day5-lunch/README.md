 # Exercise 1
 First Unix:
 `cut -d "," -f 5-6 aau1043_dnm.csv | sort > dnm_list.txt`
 
 Then run dnm_list.py:
 Then Unix join:
 ```
 sort aau1043_parental_age.csv > aau1043_parental_age_sort.csv
 sort dnm_count_list.csv > dnm_count_list_sort.csv
 join -t ',' dnm_count_list_sort.csv aau1043_parental_age_sort.csv | sed '$d' > dnm_combo.csv
 ```
 Then run dnm_plot.py
 
 # Exercise 2
 There is a strong relationship between maternal age and de novo mutation (p=6.878208e-24). There is a relationship of 0.3776 de novo mutations per year.
 
 There is also a strong relationship between paternal age and de novo mutation (p=1.552294e-84). Offspring are likely to have 1.3538 de novo mutations for each year of the father. 
 
 There is a significant diference between dnm from the mother and the father (p=1.1245140794572799e-204)
 
 I'd predict 78.6932 de novo mutations inherited from the father. 