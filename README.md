# Cordell Browne's Portfolio

Welcome, all of my projects are hyperlinked to the headers below. Supporting details for each project are listed below their respective header.

## [RNA-Seq Analysis.](https://c0rd3ll.github.io/RNAseq/)
The link contains an rmarkdown of bulk-RNA-Seq analysis on Oral squamous cell carinoma. It is seperated into Four distinct phases and answers questions like the following: 

* Preprocessing, I show the script that was used to develop the input data (count matrix) 
* Exploratory data anlysis, how does normaliztion and transformation affect the data? 
* Differential Expression (DE) , What genes are most regualted, what is statiscally important? 
* Co-expression Analysis (Subcategory of DE), what genes work together in hubs? Their expression levels? 


In case the first link doesn't work:  [Click Here](https://github.com/C0RD3LL/Portfolio/blob/main/RNA-seq.md)


## [Benchmarking](https://c0rd3ll.github.io/benchmark_page)
Benchmarking different tools/method on their abilities to generate fastq indexes. It compares time in seconds and memory of each method over total bases in file and actual file size.

* The benchmarking was done bewteen samtools, pyfastx, biopython, and bioperl's Index::Fastq module.

The results concluded that samtools performed faster then the rest, most likely becuase of its high memory usage. It was also noted that bioperl was signifcantly slower to generate and index than others and that memory was consisently between 17,000 ~ 18,000 regardless of file size.

## [Benchmark Scripts](https://github.com/C0RD3LL/Portfolio/tree/main/Benchmark%20scripts)
Python script, that when a fastq file is inputed the script will output: Amount of reads, total bases, and an average of bases per read.

(I created it becuase it was a simple way to gauge the size of fastq files.)


![alt text](https://github.com/C0RD3LL/Portfolio/blob/main/extra/Screen%20Shot%202022-01-07%20at%205.19.41%20PM.png)
### Example Argument
```
python3 fqcount.py <../example/directory.fastq>
```
**Improvements**

I looked for ways to imporove the code and did it with a simple command provided by the pyfastx package. This inspired the benchmarking portion of the portfolio. The image below is to display the progression/improvment of the idea that was initiated with fqcount.py. 
![alt text](https://github.com/C0RD3LL/Portfolio/blob/main/extra/Screen%20Shot%202022-01-07%20at%205.19.54%20PM.png)


Thanks for stopping by!
