#! /usr/bin/env python

# convert fasta files to nexus.

import datetime, sys
from Bio import AlignIO, SeqIO

def fas2nex(infile, outfile):
    ntax = len(SeqIO.index(infile, "fasta"))
    alignment = AlignIO.read(open(infile), "fasta")
    nchar = alignment.get_alignment_length()
    today = datetime.date.today()

    fastain = SeqIO.parse(infile, "fasta")      # Get data from Fasta file
    nexusout = open(outfile, "w")
    
    nexusout.write('#NEXUS\n')
    nexusout.write('[Converted from %s on %s]\n\n' % (infile, today))
    
    nexusout.write('Begin DATA;\n')
    nexusout.write('\tdimensions ntax=%i nchar=%i;\n' % (ntax, nchar))
    nexusout.write('\tformat datatype=DNA missing=? gap=-;\n\tmatrix\n')
    for i in fastain:
        nexusout.write('\t\t%s\t\t%s\n' % (i.name, i.seq))
    nexusout.write(';\nEND;')

userParameters=sys.argv[1:]
 
try:
    if len(userParameters)==1:
        fas2nex(userParameters[0], "outfile")
    elif len(userParameters)==2:
        fas2nex(userParameters[0], userParameters[1])
    else:
        print "Error 1"
except:
    print "Error 2"
    exit(0)
