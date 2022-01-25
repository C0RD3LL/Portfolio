#! bin/bash

for file in ../Downloads/fastq/*.fastq; do
    
    #get fastq basename 
    name=$(basename ${file} .fastq)

    printf "$name\n"
	#pyfastx; gtime records "e" : time & "M" : memory 
	gtime -f "pyfast\n(time: '%e' | memory: '%M')" python3 pyfast_index.py $file

    #samtools
    gtime -f "samtools\n(time: '%e' | memory: '%M')" samtools fqidx $file

    #biopython
    gtime -f "biopython\n(time: '%e' | memory: '%M')" python3 biopy_index.py  $file

    #bioperl
    gtime -f "perl\n(time: '%e'| memory: '%M')" perl bioperl_index.pl $file

done