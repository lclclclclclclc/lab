#!/usr/bin/python

# Takes output from collapsing haplotypes and makes codes alleles as numbers for multiple loci
# Use: ./sciptcall outfile eachlocustxt

import re, os, sys

files=sys.argv[2:]
outfile=open(sys.argv[1],"w+")
#outfile.write('sample\t'+'\t'.join(files)+'\n')

alldat={}
for file in files:
    # This creates a dictionary for that file.
    datin = open(file+'.hapkey.txt', "r")
    hapline = datin.readlines()
    haplotypes={}
    for i in range(0, len(hapline)):
        if i < 10:
            hapnum = '0'+str(i)
        else:
            hapnum = str(i)
        
        line = hapline[i].strip('\]\n')
        lineparts = re.split("[,:'\]\[ ]+", line)
        samples = lineparts[2:(len(lineparts)-1)]
        for x in samples:
            x=x[0:-2]
            if x not in haplotypes:
                haplotypes[x] = hapnum
            else:
                haplotypes[x] += ':'+hapnum
    alldat[file]=haplotypes

nameslist=[]
for locus in files:
    nameslist+=list(alldat[locus].keys())
uniquenames=sorted(list(set(nameslist)))

outfile.write('sample\t'+'\t'.join(list(alldat.keys()))+'\n')
for n in uniquenames:
    print n
    tmpdict={}
    for l in files:
        dat=alldat[l]
        if n in dat:
            tmpdict[l]=dat[n]
        else:
            tmpdict[l]='NA:NA'
    towrite = '%s\t%s\n' % (n, '\t'.join(tmpdict.values()))
    print tmpdict
    del tmpdict
    outfile.write(towrite)
outfile.close()
