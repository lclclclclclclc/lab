#! /usr/bin/env python

# script to group individuals in a fasta by defined group.
# in progress, basic

#import csv, re
from Bio import SeqIO

# Make a dictionary out of a table with IDs and groupings
#bins = open("testfile.txt", "rb")
#bindict = csv.DictReader(bins, delimiter="\t")


# Read in fasta
records = SeqIO.index("scar298anl.fas", "fasta")

# Read in table of individuals
tmpseqs = open("texas1.txt").read()
wantedseqs = tmpseqs.split("\n")

outfile=open("texas1_s298.fas","w+")

for x in wantedseqs:
#Diploid version
    avers = '%s_1' % x
    bvers = '%s_2' % x
    if avers in records.keys():
        outfile.write('>%s\n%s\n\n' % (avers, records[avers].seq))
    if bvers in records.keys():
        outfile.write('>%s\n%s\n\n' % (bvers, records[bvers].seq))

# Haploid version
    # if x in records.keys():
    #     outfile.write('>%s\n%s\n\n' % (x, records[x].seq))
        
outfile.close()