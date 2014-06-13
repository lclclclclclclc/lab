#! /usr/bin/env python

# A test of null values
# Use None instead of NULL. No '
# See syntax of the execute statement!

import re
from datetime import datetime
import MySQLdb

InFile = open("LMC2010.txt",'r')

def checknull(value):
    if not value:
        value = None
        return value
    else:
        return value

def parsedate(date):
    if note date:
        dateparsed = None
        return dateparsed
    else:
#       dateparsed = datetime.strptime(date, "%d-%b-%y")
        dateparsed = datetime.strptime(date, "%Y-%m-%d")
        return dateparsed.strftime("%Y-%m-%d")

def dealwithnums(x, d):
    try:
        return '%.*f' % (d, float(x))
    except:
        return None

def splitID(IDname):
    try:
        nameparts = IDname.split('.')
        return 'LMC2010', dealwithnums(nameparts[1],0)
    except:
        return None, None

conn = MySQLdb.connect(host = "localhost", user="root", passwd="", db="test_db")
conn.autocommit(True)
curs = conn.cursor()

LineNum = 0
for line in InFile:
    if LineNum > 0:
        line = line.strip('\n')
        elements = line.split('\t')

        sampleID = checknull(elements[0])
        have = 'yes' #checknull(elements[])
        collectorABBR, collectorNUM = splitID(elements[0])
        
        #collectorABBR = checknull(elements[])
        #collectorNUM = dealwithnums(elements[],0)
        collectionseriesABBR = None #checknull(elements[])
        collectionseriesNUM = None #dealwithnums(elements[],0)
        voucherABBR = None #checknull(elements[])
        voucherNUM = None #dealwithnums(elements[],0)
        disposition = None #checknull(elements[])
        collectornames = checknull(elements[2])
        genus = checknull(elements[3])
        species = checknull(elements[4])
        tissuetype = 'tail or toe' #checknull(elements[])
        samplemedium = 'EtOH' #checknull(elements[])
        samplenotes = checknull(elements[13])
        sex = checknull(elements[9])
        svl = None #dealwithnums(elements[],1)
        tail_length = None #dealwithnums(elements[],1)
        total_length = None #dealwithnums(elements[],1)
        latDD = dealwithnums(elements[6],6)
        longDD = dealwithnums(elements[8],6)
        descriptive = None #checknull(elements[])
        latNS = checknull(elements[5])
        longEW = checknull(elements[7])
        UTMzone = None #checknull(elements[])
        UTMeasting = None #dealwithnums(elements[],0)
        UTMnorthing = None #dealwithnums(elements[],0)
        township = None #checknull(elements[])
        otherlocality = None #checknull(elements[])
        county = None #checknull(elements[])
        state = 'New Mexico' #checknull(elements[])
        country = 'USA' #checknull(elements[])
        elevation = None #dealwithnums(elements[],0)
        elevation_units = None #checknull(elements[])
        date_collected = parsedate(elements[1])
        accuracy = None #checknull(elements[])
        collection_notes = None #checknull(elements[])
        datum = None #checknull(elements[])

        runline = 'curs.execute('
        insert = '"INSERT INTO samples \
            (sampleID, have, collectorABBR, collectorNUM, collectionseriesABBR, \
            collectionseriesNUM, voucherABBR, voucherNUM, disposition, collectornames, \
            genus, species, tissuetype, samplemedium, samplenotes, \
            sex, svl, tail_length, total_length, latDD, \
            longDD, descriptive, latNS, longEW, UTMzone, \
            UTMeasting, UTMnorthing, township, otherlocality, county, \
            state, country, elevation, elevation_units, date_collected, \
            accuracy, collection_notes, datum) \
            VALUES (%s,%s,%s,%s,%s,\
                %s,%s,%s,%s,%s,\
                %s,%s,%s,%s,%s,\
                %s,%s,%s,%s,%s,\
                %s,%s,%s,%s,%s,\
                %s,%s,%s,%s,%s,\
                %s,%s,%s,%s,%s,\
                %s,%s,%s)", \
            (sampleID, have, collectorABBR, collectorNUM, collectionseriesABBR, \
            collectionseriesNUM, voucherABBR, voucherNUM, disposition, collectornames, \
            genus, species, tissuetype, samplemedium, samplenotes, \
            sex, svl, tail_length, total_length, latDD, \
            longDD, descriptive, latNS, longEW, UTMzone, \
            UTMeasting, UTMnorthing, township, otherlocality, county, \
            state, country, elevation, elevation_units, date_collected, \
            accuracy, collection_notes, datum) '
        fullstmt = '%s%s) ' % (runline,insert)
        
        #CHECK VALUES:
#        print '(sampleID: %s,\n have: %s,\n collectorABBR: %s,\n collectorNUM: %s,\n collectionseriesABBR: %s,\n \
#collectionseriesNUM: %s,\n voucherABBR: %s,\n voucherNUM: %s,\n disposition: %s,\n collectornames: %s,\n \
#genus: %s,\n species: %s,\n tissuetype: %s,\n samplemedium: %s,\n samplenotes: %s,\n \
#sex: %s,\n svl: %s,\n tail_length: %s,\n total_length: %s,\n latDD: %s,\n \
#longDD: %s,\n descriptive: %s,\n latNS: %s,\n longEW: %s,\n UTMzone: %s,\n \
#UTMeasting: %s,\n UTMnorthing: %s,\n township: %s,\n otherlocality: %s,\n county: %s,\n \
#state: %s,\n country: %s,\n elevation: %s,\n elevation_units: %s,\n date_collected: %s,\n \
#accuracy: %s,\n collection_notes: %s,\n datum: %s)' % \
#(sampleID, have, collectorABBR, collectorNUM, collectionseriesABBR, \
#collectionseriesNUM, voucherABBR, voucherNUM, disposition, collectornames, \
#genus, species, tissuetype, samplemedium, samplenotes, \
#sex, svl, tail_length, total_length, latDD, \
#longDD, descriptive, latNS, longEW, UTMzone, \
#UTMeasting, UTMnorthing, township, otherlocality, county, \
#state, country, elevation, elevation_units, date_collected, \
#accuracy, collection_notes, datum)
        
        exec fullstmt
    LineNum += 1

InFile.close()
curs.close()
conn.close()
