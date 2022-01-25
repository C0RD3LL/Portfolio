#Thanks for looking at my portfolio 
# ~Cordell Browne
###########Imports###########
import os
import sys
import pyfastx

#############################


fastq = sys.argv[1]

fq = pyfastx.Fastq(fastq)




print("Total Reads:",len(fq))
print("Total Bases:",fq.size)
print("Base per Read:",round(fq.avglen))

