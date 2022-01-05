#Thanks for looking at my portfolio 
# ~Cordell Browne
###########Imports###########
import os
import gzip
import sys
from datetime import datetime
import pyfastx
import psutil
#############################

startTime = datetime.now()

fastq = sys.argv[1]

fq = pyfastx.Fastq(fastq)

#Get memory used in GBs 
pid = os.getpid()
python_process = psutil.Process(pid)
memoryUse = python_process.memory_info()[0]/2.**30  


print("Total Reads  :"len(fq))
print("Total Bases  :"fq.size)
print("Base per Read:"fq.avglen)
print("Runtime      :" datetime.now() - startTime)
print('memory use   :', memoryUse)
