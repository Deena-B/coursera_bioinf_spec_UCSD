#! usr/bin/env python

# create a list of 2-mers with ATGC

# Text = GATCCAGATCCCCATAC
# Pattern = [AA, AT, AG, AC, TT, TA, TG, TC, GG, GA, GT, GC, CC, CA, CT, CG]
# PatFreqListofDicts = [{Pattern: Frequency},...] = [{AA, 0}, {AT, 3}, {AG,1}, { AC, 1}, {TT, 0}, {TA, 1}, {TG, 0}, {TC, 2}, {GG, 0}, {GA, 2}, {GT, 0}, {GC, 0}, {CC, 4}, {CA, 2}, {CT, 0}, {CG, 0}]
# 4 CC's is the max

# Generate Pattern list
# we have position 1 & position 2 and every nt can be in each

# A in position 1, ATGC in position 2
# T in position 1, ATGC...
# G...
# ...
    

# make a dictionary to hold the Pattern and frequency with which it occurs in Text
freq_dict = {}


def pattern_count(text:str, pattern:str):
"count the number of times `pattern` is found in the string `text`"
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count 


def MostFreqPattern(freq_dict:dict)
    "find the pattern(s) with max occurances in text"
