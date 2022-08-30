# Jack Dorman	8/23/22
#JHU CMDB BootCamp Code 0: recreate the tail bash function
#USAGE: python scriptname.py input_filename [number_lines_to_display]

import sys #import module
filename = sys.argv[1] #SET input filename
if len(sys.argv) > 2: #IF user-specified number of lines provided
  n_lines = int(sys.argv[2]) #SET the desired number of lines
else: #OTHERWISE
  n_lines = 10 #SET the desired number of lines to a default
vcf_list=[] #Create an empty list
for line in open(filename): #FOR every line in the open file
  vcf_list.append(line.strip('\r\n')) #Add each line to the empty list
cutoff=len(vcf_list)-n_lines #Set a cutoff 
for i, item in enumerate(vcf_list): #FOR every item in vcf list
  if i >= cutoff: #IF a desired line greater than or equal to the cutoff
    print(item)#.strip('\r\n')) #PRINT the line

# Excellent script. I appreciate the usage message and the pseudo-code turned
# comments. I only have two bits of feedback. The first is that putting in blank
# lines to break up your code into functional blocks will make it easier to
# read and comprehend. Second is that you could rewrite your last for loop
# to only go through the lines you want to print. It doesn't make much difference
# here but in cases where you are processing a giant file, avoiding the extra
# work can definitely speed things up. You could use something like
# for i in range(len(vcf_list) - n_lines, len(vcf_list)):
#   print(vcf_list[i])
# You seem to have a firm grasp of what you're doing. Keep it up! - Mike