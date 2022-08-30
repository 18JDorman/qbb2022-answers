#!/usr/bin/env python3

import sys

def parse_vcf(fname): #start the function
    vcf = [] #create empty lists and dictionaries
    info_description = {}
    info_type = {}
    format_description = {}
    type_map = { #the terms in vcf which need to be converted to a name python can recognize as a function
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0 #start error counter

    try:
        fs = open(fname) #open the file
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr) #give an error if the file isn't there

    for h, line in enumerate(fs): #start a for loop over each line in the file paired with its index
        if line.startswith("#"): #look for header lines
            try:
                #the goal of this block is to parse the format header into a dictionary
                if line.startswith("##FORMAT"): #parse up the format header
                    fields = line.split("=<")[1].rstrip(">\r\n") + "," #break up the format line 
                    i = 0 #start counters
                    start = 0
                    in_string = False #start a boolean variable to determine where to stop
                    #this while loop goes until i reaches the end of fields
                    while i < len(fields):
                        if fields[i] == "," and not in_string: #
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        #this block works on the non-header section (that contains data)
        else:
            try:
                fields = line.rstrip().split("\t") #split up line by tab
                fields[1] = int(fields[1]) #convert first line entry to int
                if fields[5] != ".": #make sure 5 doesn't have "." entered
                    fields[5] = float(fields[5]) #converts entry to float
                info = {} #start a dictionary
                for entry in fields[7].split(";"): #split up 7th line entry by semi-colon
                    temp = entry.split("=") #each entry in split line 7 loaded to a temp variable
                    if len(temp) == 1: #if line has only one entry in it
                        info[temp[0]] = None #use it as a key but give it no value in the dictionary
                    else: #all others will have a length of 2
                        name, value = temp #put both entries into separate variables
                        Type = info_type[name] #these two lines replace vcf format with python format
                        info[name] = type_map[Type](value)
                fields[7] = info #put newly formatted data into fields at 7
                if len(fields) > 8: #if there are at least 9 entries in fields
                    fields[8] = fields[8].split(":") #split at index 8 by colon
                    if len(fields[8]) > 1: #if there are mutliple entries in the list at index 8
                        for i in range(9, len(fields)): #loop everything from position 9 and on
                            fields[i] = fields[i].split(':') #split each entry by colon
                    else:
                        fields[8] = fields[8][0] #if there's only one entry at position 8, take the first position at the list in 8
                vcf.append(fields) #add entry to total list
            except:
                malformed += 1 #if there's an error at that line, add one
    vcf[0][7] = info_description #add info header data to vcf
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description #add format header data to vcf
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr) #print one error message if there are errors encountered
    return vcf #vcf list is returned

if __name__ == "__main__": #only do this in this script
    fname = sys.argv[1] #take the file name from the command line second entry
    vcf = parse_vcf(fname) #run parse function
    for i in range(10): #print first 10 entries 
        print(vcf[i])
