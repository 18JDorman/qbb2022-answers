#!/usr/bin/env python3

import bed_parser #import parse_bed function
import sys #has functions to use
import statistics

if __name__ == "__main__":
    hg38Bed=bed_parser.parse_bed(sys.argv[1]) #import hg38 bed
    hg38Exons=[] #start list
    for each in hg38Bed: #add exon data to list
        hg38Exons.append(each[9])
    print(statistics.median(hg38Exons)) #use statistics function to find median