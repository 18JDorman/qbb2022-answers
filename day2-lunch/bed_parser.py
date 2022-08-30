#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    ErrorCount = []
    field_types = [str, int, int, str, float, str, int, int, 'place1', 'place2', 'place3', 'place4']
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3 or fieldN == 10 or fieldN == 11:
            ErrorCount.append(i)
            continue
        try:
            for j in range(min(fieldN, len(field_types))):
                if fields[j] != ".":
                    if j == 9:
                        fields[j] = int(fields[j])
                    elif j == 8:
                        fields[j]=fields[j].split(',')
                        if len(fields[j]) != 3:
                            ErrorCount.append(i)
                            continue
                    elif (j == 10) or (j == 11):
                        fields[j] = fields[j].rstrip(',').split(',')
                        if len(fields[j]) != fields[9] or len(fields[j]) != fields[9]:
                            #print(f"blockSizes or blockStarts of line {i} does not equal blockCount.")
                            ErrorCount.append(i)
                            continue
                    else:
                        fields[j] = field_types[j](fields[j])                    
            bed.append(fields)
        except:
            ErrorCount.append(i)
        AllErr = len(set(ErrorCount))
    fs.close()
    print(f"The number of malformation errors is: {AllErr}")
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
