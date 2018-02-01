#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:21:48 2018

@author: eburlacu
"""

import pysam

fragment_end = 0

bamfile = pysam.AlignmentFile('../BEL033_1000.bam', 'rb')
output = open('BEL033_bam2bed.bed', 'w')
iter = bamfile.fetch() # read over the entire file - each line will be an AlignmentSegment class
for aln in iter :
    if aln.is_paired and aln.is_read1:
        fragment_end = aln.reference_start + aln.template_length
        output.write(aln.reference_name + "\t"+ str(aln.reference_start) + "\t"+ str(fragment_end) +"\t"+aln.query_name + "." +"\t"+"," + "\n")
bamfile.close()
output.close()