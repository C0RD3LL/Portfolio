# Cordell Browne's Portfolio

Welcome, all of my projects are hyperlinked to the headers below. Supporting details for each project are listed below their respective header.

## [RNA-Seq Analysis.](https://c0rd3ll.github.io/RNAseq/)
This is a RNA-Seq workflow that aims to identify which genes and biological processes may be important for our condition of interest (Oral squamous cell carinoma. metastisis vs no-metastisis).Starting with the counts for each gene, the course will cover how to prepare data for DE analysis, assess the quality of the count data, and identify outliers and detect major sources of variation in the data. The DESeq2 R package will be used to model the count data using a negative binomial model and test for differentially expressed genes. Visualization of the results with heatmaps and volcano plots will be performed and the significant differentially expressed genes will be identified and saved.

* Outline of RNA Seq Workflow.
  * Preprocessing: Generating a countmatrix from self-generated reference genome and sample reads (fastq)
  * Exploratory data anlysis: Answering question like, how does normaliztion and transformation affect the data? 
  * Differential Expression: What genes are most regualted, what is statiscally important? 
  * Co-expression Analysis: Assessing, what genes work together in hubs? Their expression levels? 

In case the first link doesn't work:  [Click Here](https://github.com/C0RD3LL/Portfolio/blob/main/RNA-seq.md)


## [Benchmarking](https://c0rd3ll.github.io/benchmark_page)
Benchmarking different tools/method on their abilities to generate fastq indexes. It compares time in seconds and memory of each method over total bases in file and actual file size.

* The benchmarking was done bewteen samtools, pyfastx, biopython, and bioperl's Index::Fastq module.

The results concluded that samtools performed faster then the rest, most likely becuase of its high memory usage. It was also noted that bioperl was signifcantly slower to generate an index than others and its memory usage was kept in a narrow range and consisently low (17,000 ~ 18,000) regardless of file size.

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
