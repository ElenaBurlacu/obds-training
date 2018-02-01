#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:21:48 2018

@author: eburlacu
"""

import pysam



samfile = pysam.Alignmentfile('bam_testfile.bam', "rb")

iter = samfile.fetch("chr1", 10, 20)
for x in iter :
    print (x)

