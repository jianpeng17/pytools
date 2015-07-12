#!/usr/bin/env python

"""
this tool can help compare the oprofile benchmark and result
"""
import re
import sys

if len(sys.argv) < 3:
    print "usage:  %s file1 file2" % sys.argv[0]
    sys.exit()

d = {}
with open(sys.argv[1]) as f1:
    for line in f1:
        cols = re.split('\s+', line, 3)
        d[cols[3]] = cols[1]


with open(sys.argv[2]) as f2:
    for line in f2:
        cols = re.split('\s+', line, 3)
        if cols[3] in d:
            print "%s %s %s" % ('{:<8s}'.format(cols[1]), '{:<8s}'.format(d[cols[3]]), cols[3])
        else:
            print "%s %s %s" % ('{:<8s}'.format(cols[1]), '{:<8s}'.format('{}'), cols[3])
