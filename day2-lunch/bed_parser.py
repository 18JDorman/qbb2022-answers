#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    ErrorCount = []
    field_types = [str, int, int, str, float, str, int, int, 'place1', 'place2', 'place3', 'place4'] #make sure list is 12 items
    for i, line in enumerate(fs):
        if line.startswith("#"): #skip headers
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3 or fieldN == 10 or fieldN == 11: #if there are less than 3 fields or 10 or 11, add error
            ErrorCount.append(i)
            continue
        try:
            for j in range(min(fieldN, len(field_types))): #pick either the length of the field or number of types
                if fields[j] != ".": #skip entries with .
                    if j == 9: #convert position 9 to int
                        fields[j] = int(fields[j])
                    elif j == 8: #only split position 8 by comma
                        fields[j]=fields[j].split(',')
                        if len(fields[j]) != 3: #if there are not exactly 3 entries after splitting, add error
                            ErrorCount.append(i)
                            continue
                    elif (j == 10) or (j == 11): #for index 10 and 11, split by comma and remove last comma
                        fields[j] = fields[j].rstrip(',').split(',')
                        if len(fields[j]) != fields[9] or len(fields[j]) != fields[9]: #if blockSize or blockStarts doesn't match blockCount, add error
                            ErrorCount.append(i)
                            continue
                    else: #for all other entries, follow formatting of field_types which will go up to string placeholders
                        fields[j] = field_types[j](fields[j])                    
            bed.append(fields)
        except:
            ErrorCount.append(i)
        AllErr = len(set(ErrorCount)) #take unique ids of lines with error
    fs.close()
    print(f"The number of malformation errors is: {AllErr}") #print number of errors
    return bed

if __name__ == "__main__": #run the function on the command line file
    fname = sys.argv[1]
    bed = parse_bed(fname)
