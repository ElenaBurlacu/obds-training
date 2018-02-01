#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:21:48 2018

@author: eburlacu
"""

import pysam
import sys
import logging as L

L.basicConfig(filename = "MyLog.log", level = L.DEBUG)
fragment_end = 0
pairs_count = 0
average_fragmentssize = 0
sum_intervals = 0

bamfile = pysam.AlignmentFile("BEL033_1000.bam", 'rb')
iter = bamfile.fetch() # read over the entire file - each line will be an AlignmentSegment class
initial_count = bamfile.count()
for aln in iter :
    if aln.is_paired and aln.is_read1:
        pairs_count += 1
        fragment_end = aln.reference_start + aln.template_length
        sum_intervals += aln.template_length
        sys.stdout.write(aln.reference_name + "\t"+ str(aln.reference_start) + "\t"+ str(fragment_end) +"\t"+aln.query_name + "." +"\t"+"," + "\n")
        
average_fragmentssize = sum_intervals / pairs_count
L.info("Initial count is {}".format(initial_count))
L.info("Number of paired reads is {}".format(pairs_count))
L.info("Average fragment size is {:4.2f}".format(average_fragmentssize))


bamfile.close()