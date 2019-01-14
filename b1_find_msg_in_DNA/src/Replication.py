#! usr/bin/env python

def PatternCount(Text:str, Pattern:str):
"count the number of times Pattern is found in the string Text"
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 



