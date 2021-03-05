import itertools as it
import pandas
import os

colors = pandas.read_table("~/Desktop/colors.txt")

StringBuffer = it.repeat(colors)
SequenceRepeation = 0
SequenceStart = 0
SequenceEnd = 2

for output in StringBuffer: 
    if(SequenceStart == 0): 
        print("Sequence %d"%(SequenceRepeation + 1))
    print(output, end =" ")
    if(SequenceStart == SequenceEnd-1):   
        if(SequenceRepeation>= 2): 
            break
        else:
            SequenceRepeation+= 1
            SequenceStart = 0
            print("\n")
    else: 
        SequenceStart+= 1
