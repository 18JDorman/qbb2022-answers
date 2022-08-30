#!/usr/bin/env python3
# Usage: ./random_snippet_update.py random_snippet.vcf dbSNP_snippet.vcf

import vcfParser #import vcfParser function
import sys #import sys

if __name__ == "__main__":
    ran_snp = vcfParser.parse_vcf(sys.argv[1]) #take random snip vcf
    db_snp = vcfParser.parse_vcf(sys.argv[2]) #take dbSNP vcf
    db_snp_IDs=[] #start all lists
    db_snp_POS=[]
    filt_ran_snp=[]
    for each in db_snp[1:]: #skip the first line which has headers
        db_snp_IDs.append(each[2]) #append only ID to list
    for each in db_snp[1:]: #also skipping header
        db_snp_POS.append(each[1]) #append only position
    SNP_ID = {} #create dict
    for pos in db_snp_POS: #go through position data
        for ids in db_snp_IDs: #go through id data
            SNP_ID[pos]=ids #give a id for a given pos
            db_snp_IDs.remove(ids) #remove that ids from the list
            break #go to the next pos
    for each in ran_snp: #go through random snp data
        if each[1] in SNP_ID.keys(): #if the position is a key in the dictionary
            each[2]=SNP_ID[each[1]] #replace the ID data with the dict value ID
            filt_ran_snp.append(each) #add that to a new list
        else: #otherwise the position is not there so add the line unmodified
            filt_ran_snp.append(each)
    count = 0 #start the sount
    for each in filt_ran_snp: #go through the filtered data
        if each[2] == '.': #if the ID is a period
            count += 1 #increase the counter
    print(count) #print the count