#Thanks for looking at my portfolio 
# ~Cordell Browne
###########Imports###########
import gzip
import sys
from datetime import datetime
#############################
###########Help##############

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print(" \n ¯\_(ツ)_/¯ \n") 
    quit() 

#############################

startTime = datetime.now()

fastq = sys.argv[1]

reads = 0
bases = 0


if fastq.endswith('.gz') == True:
    with gzip.open(fastq, 'rb') as file:
        for id in file:
            seq = next(file)
            reads += 1
            bases += len(seq.strip())
            next(file)
            next(file)
else:
    with open(fastq, 'rb') as file:
        for id in file:
            seq = next(file)
            reads += 1
            bases += len(seq.strip())
            next(file)
            next(file)


print("Amount of Reads: ", reads)
print("Amount of Bases: ", bases)
print("Base per Read:   ",round(bases/reads))
print("Run time:        ", datetime.now() - startTime)
