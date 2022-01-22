# Cordell Browne's Portfolio

Welcome, all of my projects are hyperlinked to the headers below. Supporting details for each project are listed below their respective header.

## [RNA-Seq Analysis.](https://c0rd3ll.github.io/RNAseq/)
The link contains an rmarkdown of bulk-RNA-Seq analysis on Oral squamous cell carinoma. It is seperated into Four distinct phases and answers questions like the following: 

* Preprocessing, I show the script that was used to develop the input data (count matrix) 
* Exploratory data anlysis, how does normaliztion and transformation affect the data? 
* Differential Expression (DE) , What genes are most regualted, what is statiscally important? 
* Co-expression Analysis (Subcategory of DE), what genes work together in hubs? Their expression levels? 


In case the first link doesn't work:  [Click Here](https://github.com/C0RD3LL/Portfolio/blob/main/RNA-seq.md)


## [Benchmarking](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.livescience.com%2F54258-donkeys.html&psig=AOvVaw0teG2GWPcdSjzDhlSpdLUQ&ust=1641435693727000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIin_s3GmfUCFQAAAAAdAAAAABAD)
An important analysis question is the quantification and statistical inference of systematic changes between conditions, as compared to within-condition variability. The package DESeq2 provides methods to test for differential expression by use of negative binomial generalized linear models; the estimates of dispersion and logarithmic fold changes incorporate data-driven prior distributions.[Benchmark scripts](https://github.com/C0RD3LL/Portfolio/tree/main/Benchmark%20scripts)
* initate The package DESeq2 provides methods to test for differential expression 
* protocal

```
python3 dance The package DESeq2 provides 
```

The package DESeq2 provides methods to test for differential expression by use of negative binomial generalized linear models; the estimates of dispersion and logarithmic fold changes incorporate data-driven prior distributions.

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
