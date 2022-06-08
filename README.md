# [Cordell Browne's Portfolio](https://c0rd3ll.github.io/portfolio-0.01/index.html)

Welcome, all of my projects are hyperlinked to the headers below. Supporting details for each project are listed below their respective header.

# __Clinical Analytics__

## [Insurance Cost Prediction EDA + Regression]()


- In this project, my main aim is to show ways to go deep into the data story-telling even though the dataset is small. Also, I will work on a model that could give us an approximation as to what will be the charges of the patients. Nevertheless, we must go deeply into what factors influenced the charge of a specific patient. In order to do this we must look for patterns in our data analysis and gain extensive insight of what the data is telling us. Lastly, we will go step by step to understand the story behind the patients in this dataset only through this way we could have a better understanding of what features will help our model have a closer accuracy to the true patient charge


<br>

# __Bioinformatics__

## [Oral Squamous Cell Carcinoma (OSCC) RNA-Seq Analysis](https://c0rd3ll.github.io/portfolio-0.01/rnaseq.html)


- This RNA-Seq workflow aims to identify which genes and biological processes may be important for our condition of interest (Oral squamous cell carcinoma, metastasis vs no-metastasis). Starting with the generation of the reference genome, the workflow covers how the data was prepared for exploratory data analysis and Differential expression (DE) analysis (DE includes co-expression) and how it is used in those phases as well. The R package, DESeq2 and other supporting ones were an integral part for visualization of the results, helping better understand the characteristics of the data and also which significant differentially expressed genes could be identified. 
  - __Outline of RNA Seq Workflow:__ 
    - Preprocessing: Generating a count matrix from self-generated reference genome and sample reads (fastq) 
    - Exploratory data analysis: Answering question like, how does normalization and transformation affect the data? 
    - Differential Expression: What genes are most regulated, what is statically important? 
    - Co-expression Analysis: Assessing, what genes work together in hubs? What are their expression levels? 
    
<br>

## [Functional Analysis of OSCC Data](https://c0rd3ll.github.io/portfolio-0.01/functional.html)


- Functional Enrichment analysis methods helps gain insight about the biology underlying a list of genes. In this case genes that are considered signifcantly differentially expressed. The software package, Enrichr was used to analyzed the gene set. Enrichr currently contains a large collection of diverse gene set libraries available for analysis and download. Overall, Enrichr is a comprehensive resource for curated gene sets and a search engine that accumulates biological knowledge for further biological discoveries.

<br>

## [ChIP-Seq Analysis of TF ERa in Breast Cancer Cell Line Replicates](https://c0rd3ll.github.io/portfolio-0.01/ChIP.html)


- ChIP-seq was used to analyze five breast cancer cell lines against the transcription factor ERa. Three of these cell lines are responsive to tamoxifen treatment, while two others are resistant to tamoxifen; there are eleven total sequenced libraries. For each sample, there is an associated peakset derived using the MACS peak caller. Only data for chromosome 18 was included in the data. The goal of the analysis is compare binding across samples and cell types.

- Tamoxifen is a nonsteroidal antiestrogen that has found successful applications for each stage of breast cancer in the treatment of selected patients. Tamoxifen was originally introduced for the treatment of advanced disease in postmenopausal women. The proven efficacy of tamoxifen and the low incidence of side effects made the drug an ideal agent to test as an adjuvant therapy for women with node-positive breast cancer.

<br>

## [Benchmark experiment](https://c0rd3ll.github.io/portfolio-0.01/benchmark.html)

- Benchmarking different tools/method on their abilities to generate fastq indexes. This compares time in seconds and memory usage of the tools over amount of bases in file and file size in bytes.The benchmarking was done bewteen samtools, pyfastx, biopython, and bioperl's Index::Fastq module.
The results concluded that samtools performed faster then the rest, most likely becuase of its high memory usage. It was also noted that bioperl was signifcantly slower to generate an index than others and its memory usage was kept in a narrow range and consisently low (17,000 ~ 18,000) regardless of file size.

Thanks for stopping by!
