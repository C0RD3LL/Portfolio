# Cordell Browne's Portfolio

Welcome, all of my projects are hyperlinked to the headers below. Supporting details for each project are listed below their respective header.

## [RNA-Seq Analysis.](https://c0rd3ll.github.io/portfolio-0.01/functional.html)
This RNA-Seq workflow aims to identify which genes and biological processes may be important for our condition of interest (Oral squamous cell carcinoma, metastasis vs no-metastasis). Starting with the generation of the reference genome, the workflow covers how the data was prepared for exploratory data analysis and Differential expression (DE) analysis (DE includes co-expression) and how it is used in those phases as well. The R package, DESeq2 and other supporting ones were an integral part for visualization of the results, helping better understand the characteristics of the data and also which significant differentially expressed genes could be identified. 

* Outline of RNA Seq Workflow.
  * Preprocessing: Generating a count matrix from self-generated reference genome and sample reads (fastq)
  * Exploratory data analysis: Answering question like, how does normalization and transformation affect the data?
  * Differential Expression: What genes are most regulated, what is statically important?
  * Co-expression Analysis: Assessing, what genes work together in hubs? What are their expression levels? 



## [Benchmarking](https://c0rd3ll.github.io/benchmark_page)
Benchmarking different tools/method on their abilities to generate fastq indexes. This compares time in seconds and memory usage of the tools over amount of bases in file and file size in bytes.

* The benchmarking was done bewteen samtools, pyfastx, biopython, and bioperl's Index::Fastq module.

The results concluded that samtools performed faster then the rest, most likely becuase of its high memory usage. It was also noted that bioperl was signifcantly slower to generate an index than others and its memory usage was kept in a narrow range and consisently low (17,000 ~ 18,000) regardless of file size.

## [Benchmark Scripts](https://github.com/C0RD3LL/Portfolio/tree/main/Benchmark%20scripts)
Collection of scripts that were made to execute the benchmarking project.


The benchmarking was inspired by a python script, that when a fastq file is inputted the script will output Number of reads, total bases, and an average of bases per read. (It was a simple way to gauge the size of fastq files.)


![alt text](https://github.com/C0RD3LL/Portfolio/blob/main/extra/Screen%20Shot%202022-01-07%20at%205.19.41%20PM.png)
### Example Argument
```
python3 fqcount.py <../example/directory.fastq>
```
**Improvements**

I improved the code with pyfastx’s ability to index fastqs for quick access. This inspired me to look at other software’s that can index fastq files and how the index could be used. The image below is to display the progression/improvement of the idea that was initiated with fqcount.py. 
![alt text](https://github.com/C0RD3LL/Portfolio/blob/main/extra/Screen%20Shot%202022-01-07%20at%205.19.54%20PM.png)

## Other 

[EDA w/ Python](https://c0rd3ll.github.io/feburary_21_2022_12-24/)

[Machine learning(SVM & NN) predict Market Volatility](https://colab.research.google.com/drive/1tIQA-mWIla0jw8bFNOxVSscBukmpVufx?usp=sharing)


Thanks for stopping by!
