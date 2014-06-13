#!/usr/bin/python

# 130707 Lauren Chan
# Runs mrmodeltest2 and pulls out the best-fit AIC scorefiles.
# Run with file prefixes for _mrmodel.scores files
# eg. get_scores.py -o score_sum.out bfib cytb_all ghr cytb_pos1

import re, os
from sys import argv
from optparse import OptionParser

parser=OptionParser()
usage = "usage: %prog [options] argv"
parser.add_option("-o", "--outfile", type="string", help="output filename", dest="out")

(options, args) = parser.parse_args()

#userParam = argv[1:]
if options.out:
    outfile = open(options.out,"w")
    outname = options.out
else:
    outfile = open("score_summary.txt", "w")
    outname = "score_summary.txt"
    
for k in args:
    os.system('mrmodeltest2 < %s_mrmodel.scores > %s_mrmodel.out' % (k,k))
    tmpfile = open(k+'_mrmodel.out', "r")
    lines = tmpfile.readlines()
    for i in range(0, len(lines)):
        line = lines[i] 
        if re.search('^MrBayes settings for the best-fit model \\(([A-Z+]+)\\) selected by AIC in MrModeltest 2.3', line):
            tmp = re.split("[()]", line)
            outfile.write(k+'\n')
            outfile.write(tmp[1]+'\n')    
            outfile.write(lines[i+4].strip('\t'))
            outfile.write(lines[i+5].strip('\t')+'\n')
print 'Best-fit AIC models written to %s.' % outname
outfile.close()