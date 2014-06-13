#! /usr/bin/env python

# Parse sequences for multiple phylogroups.
import re, os, sys			# Needed for input and output
from Bio import SeqIO		# Needed for dealing with sequences

# Puts the sample names and groups IDs into dictionaries
def groups(filename):
	infile = open(filename, "r")
	headers = str(infile.readline())
	pg1_dict = {}
	pg2_dict = {}
	for line in infile:
		line = line.strip("\n")
		line = line.split("\t")
		pg1_dict[line[0]] = line[3]
		pg2_dict[line[0]] = line[4]
	return pg1_dict, pg2_dict

# Gets the sets of variables
def makeset(pg1, pg2):
	# Get set of PhyloGroups at each level
	pg1grps = set(pg1.values())				# Groups unique to this level
	pg2grps = set(pg2.values()) - pg1grps	# Groups unique to this level
	allgrps = pg1grps.union(pg2grps)		# All groups (no duplicates)
	return pg1grps, pg2grps, allgrps
	
# Sets the names the various locus specific files
def naming(locus, allgrps):
	of_names = {}
	ov_names = {}
	for x in allgrps:
		of_names[x] = 'PG_%s_%s.fas' % (x, locus)
		ov_names[x] = 'ov%s%s' % (x, locus)
 	return of_names, ov_names
	
def parsefasta(locus):
	fasfile = locus + '.fas'
	sequences = SeqIO.parse(fasfile, "fasta")
	of_names, ov_names = naming(locus, allg)
	for m in of_names:
		ofn = of_names[m]
		ovn = ov_names[m]
		exec('%s = open("%s", "w+")' % (ovn, ofn))
	for z in sequences:
		# note - for diploid use x[:-2] to get correct key for referencing dict
		# or, possibly use x.strip('_{1,2}')		
		# Figure out the right key for phased alleles
		if '-' in z.id:
			zkey = z.id[:-2]
		else:
			zkey = z.id

		memb = pg1_dict[zkey]
		exec('SeqIO.write(z, ov%s%s, "fasta")' % (memb, locus))
		if pg2_dict[zkey] in pg2g:
			memb = pg2_dict[zkey]
			exec('SeqIO.write(z, ov%s%s, "fasta")' % (memb, locus))
	exec('ov%s%s.close()' % (memb, locus))

############
# These are the dictionaries with the individuals and group membership
pg1_dict, pg2_dict = groups("phylogroups140612.txt")

# Determine the sets of phylogroups that will get sequences
pg1g, pg2g, allg = makeset(pg1_dict, pg2_dict)

# Need a for loop here to send all the loci to naming, get the different outfile names
# And then parses the correct locus. 
loci = ['mtdna', 'PRLR', 'R35', 'scar298', 'scar875']
for l in loci:
	parsefasta(l)
