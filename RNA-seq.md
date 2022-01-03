Differential Expression
================
Cordell Browne
<cordell@knights.ucf.edu>

-   [Abstract](#abstract)
-   [Introduction](#introduction)
    -   [Normaliztion ???](#normaliztion-)
-   [Citation](#citation)

# Abstract

# Introduction

The purpose of the project is to show competency with RNA-seq
Differential expression workflow methods. The data was preprocessed in a
Google Cloud Platform VM instance w/ specs high enough run necessary
programs like STAR.

A basic task in the analysis of count data from RNA-seq is the detection
of differentially expressed genes. The count data are presented as a
table which reports, for each sample, the number of sequence fragments
that have been assigned to each gene. Analogous data also arise for
other assay types, including comparative ChIP-Seq, HiC, shRNA screening,
and mass spectrometry. An important analysis question is the
quantification and statistical inference of systematic changes between
conditions, as compared to within-condition variability. The package
DESeq2 provides methods to test for differential expression by use of
negative binomial generalized linear models; the estimates of dispersion
and logarithmic fold changes incorporate data-driven prior
distributions. This vignette explains the use of the package and
demonstrates typical workflows. An RNA-seq workflow on the Bioconductor
website covers similar material to this vignette but at a slower pace,
including the generation of count matrices from FASTQ files. DESeq2
package version: 1.34.0

**Experimetnal Data:**

Mucus and blood were removed, flash frozen on dry ice, and RNA was
harvested using Trizol reagent. Illumina TruSeq RNA Sample Prep Kit
(Cat#FC-122-1001) was used with 5 ug of total RNA for the construction
of sequencing libraries. RNA libraries were prepared for sequencing
using standard Illumina protocols.

Comparing the differentially expressed genes between OSCC tumors with
lymph-node metastasis (LNM) and those without LNM, which were obtained
though NGS, we found that immune response plays an important role in the
process of OSCC LNM and the candidate genes involved in the anti-tumor
immunity were validated with qRT-PCR. Overall design: mRNA profiles of
OSCC patients with LNM (n=5) and those without LNM (n=4).

The data for this workflow was randomly selected from geo browser. There
is no asscoiated paper with it, so there was not much insight to how the
data is intended to be used outside of the basic description.

**Preparing Count Matrix**

The computational analysis of an RNA-seq experiment begins with a set of
FASTQ files that contain the nucleotide sequence of each read and a
quality score at each position. These reads must either be aligned to a
reference genome or transcriptome, or the abundances and estimated
counts per transcript can be estimated without alignment, as described
above. In either case, it is important to know if the sequencing
experiment was single-end or paired-end, as the alignment software will
require the user to specify both FASTQ files for a paired-end
experiment. The output of this alignment step is commonly stored in a
file format called SAM/BAM.

The reads for this experiment were aligned to the Ensembl release 7515
human reference genome using the STAR read aligner16. In this example,
we have a file in the current directory called files with each line
containing an identifier for each experiment, and we have all the FASTQ
files in a subdirectory fastq. If you have downloaded the FASTQ files
from the Sequence Read Archive, the identifiers would be SRA run IDs,
e.g. SRR1039520. You should have two files for a paired-end experiment
for each ID, fastq/SRR1039520_1.fastq1 and fastq/SRR1039520_2.fastq,
which give the first and second read for the paired-end fragments. If
you have performed a single-end experiment, you would only have one file
per ID. The FASTQ files that were aligned for this article were
downloaded from the European Nucleotide Archive, and can be found by
searching the project ID: SRP033351. We have also created a
subdirectory, aligned, where STAR will output its alignment files.

#### Get Fastq files `SRAtools`

In order to retrieve from SRA sratools command, `fasterqdump` was used
to loop through and download all study samples.

``` bash
#for ((i = 26; i <= 34; i++))
#  do
#  fasterq-dump SRR147406$i
#done
```

FastQC MulitQC

**Generate reference genome** My macbook only has 16 gbs of RAM so in
order to use STAR I had to run most of pipeline on Google Cloud Platform
VM instance. The perticular instance was 16 vcpu 64 GB of RAM

``` bash
#STAR --runThreadN 16 \
#--runMode genomeGenerate \
#--genomeDir ref \
#--genomeFastaFiles ref/GRCh38.primary_assembly.genome.fa \
#--sjdbGTFile ref/gencode.v39.annotation.gtf 
```

**Align Samples to references** The reads are paired-end so when
`fasterq-dump` brings them in they are split e.g. (
SRR1847400123_1.fastq & SRR1847400123_2.fastq) In order to align each
sample to the reference in a effiecent manner I write a for loop to
iterate there each sample and perform the desired task.

``` bash
#for file in *1.fastq; do name=$(basename ${file} 1.fastq); do

#  STAR --runMode alignReads --genomeDir ../index/ \
#  --outSAMtype BAM SortedByCoordinate \ 
#  --readFilesIn ${name}1.fastq ${name}2.fastq \
#  --runThreadN 12 \
#  --outFileNamePrefix ../mapped/${name}
#;done
```

#### BAMs to count matrix

Generating a count table with featureCounts. output `count.out`

``` bash
#featureCounts -a ref/gencode.v39.annotation.gtf -o count.out -T 8 -p bams/*.bam
```

Once countmatirx was made there were downloaded locally and the rest of
the workflow was done on my personal machine.

``` r
library(readr)
library(tibble)
count <- read_table("../../Downloads/count.out", col_names= FALSE,skip = 1)
head(count)
```

    ## # A tibble: 6 × 15
    ##   X1     X2    X3    X4    X5    X6    X7    X8    X9    X10   X11   X12   X13  
    ##   <chr>  <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr> <chr>
    ## 1 Geneid Chr   Start End   Stra… Leng… bams… bams… bams… bams… bams… bams… bams…
    ## 2 ENSG0… chr1… 1186… 1222… +;+;… 1735  4     0     6     0     0     1     3    
    ## 3 ENSG0… chr1… 1440… 1450… -;-;… 1351  92    33    92    117   137   44    47   
    ## 4 ENSG0… chr1  17369 17436 -     68    10    3     14    20    28    6     18   
    ## 5 ENSG0… chr1… 2955… 3003… +;+;… 1021  0     2     0     0     0     0     0    
    ## 6 ENSG0… chr1  30366 30503 +     138   0     0     0     0     0     0     0    
    ## # … with 2 more variables: X14 <chr>, X15 <chr>

``` r
count <- count[,-c(2:6)] # Get rid of columns (2-6)
names(count) <- count[1,]; count <- count[-1,] #Row to columnnames
count[,2:10] <- sapply(count[, 2:10], as.numeric) #Change column type from char to numeric.
count <- column_to_rownames(count, var="Geneid")#

colnames(count) <-  c(
  "tumor1pos","tumor2pos","tumor3pos",
  "tumor4neg","tumor5neg","tumor6neg",
  "tumor7pos","tumor8neg","tumor9neg"
)
```

``` r
head(count)
```

    ##                   tumor1pos tumor2pos tumor3pos tumor4neg tumor5neg tumor6neg
    ## ENSG00000223972.5         4         0         6         0         0         1
    ## ENSG00000227232.5        92        33        92       117       137        44
    ## ENSG00000278267.1        10         3        14        20        28         6
    ## ENSG00000243485.5         0         2         0         0         0         0
    ## ENSG00000284332.1         0         0         0         0         0         0
    ## ENSG00000237613.2         0         1         0         0         0         0
    ##                   tumor7pos tumor8neg tumor9neg
    ## ENSG00000223972.5         3         1         0
    ## ENSG00000227232.5        47        97        67
    ## ENSG00000278267.1        18         9         9
    ## ENSG00000243485.5         0         0         0
    ## ENSG00000284332.1         0         0         0
    ## ENSG00000237613.2         0         0         0

## Normaliztion ???

Total number of counted reads per sample is not a good estimate of
library size. It is un-necessarily influenced by regions with large
counts, and can introduce bias and correlation across genes. Instead,
use a robust measure of library size that takes account of skew in the
distribution of counts (simplest: trimmed geometric mean; more advanced
/ appropriate encountered in the lab). Library size (total number of
counted reads) differs between samples, and should be included as a
statistical offset in analysis of differential expression, rather than
‘dividing by’ the library size early in an analysis.

While it is not necessary to pre-filter low count genes before running
the DESeq2 functions, there are two reasons which make pre-filtering
useful: by removing rows in which there are very few reads, we reduce
the memory size of the dds data object, and we increase the speed of the
transformation and testing functions within DESeq2. Here we perform a
minimal pre-filtering to keep only rows that have at least 10 reads
total. Note that more strict filtering to increase power is
automatically applied via independent filtering on the mean of
normalized counts within the results function.

In this count matrix, each row represents an Ensembl gene, each column a
sequenced RNA library, and the values give the raw numbers of fragments
that were uniquely assigned to the respective gene in each library. We
also have information on each of the samples (the columns of the count
matrix). If you’ve counted reads with some other software, it is very
important to check that the columns of the count matrix correspond to
the rows of the sample information table.

Our count matrix with our DESeqDataSet contains many rows with only
zeros, and additionally many rows with only a few fragments total. In
order to reduce the size of the object, and to increase the speed of our
functions, we can remove the rows that have no or nearly no information
about the amount of gene expression. Here we remove rows of the
DESeqDataSet that have no counts, or only a single count across all
samples:

``` r
count <- count[which(rowSums(count) > 25),]
condition <- factor(c("pos","pos","pos",
                      "neg","neg","neg",
                      "pos","pos","neg"))
coldata <- data.frame(row.names=  colnames(count), condition)
```

``` r
suppressMessages(library(DESeq2))
dds <- DESeqDataSetFromMatrix(countData = count, colData = coldata, design = ~condition)
dds <- DESeq(dds)
res <- results(dds)
res <- res[order(res$padj),]
```

``` r
library("EnhancedVolcano")

par(mfrow=c(6,1))
 
EnhancedVolcano(res,
    lab = rownames(res),
    x = "log2FoldChange",
    y = "pvalue",
    pCutoff = 10e-4,
    FCcutoff = 2,
    ylim = c(0, -log10(10e-7)),
    xlim = c(-5,5),
    pointSize = c(ifelse(res$log2FoldChange>2, 8, 1)),
    labSize = 6.0,
    shape = c(6, 6, 19, 16),
    title = "DESeq2 results",
    subtitle = "Differential expression",
    caption = bquote(~Log[2]~ "fold change cutoff, 2; p-value cutoff, 10e-4"),
    legendPosition = "right",
    legendLabSize = 14,
    colAlpha = 0.9,
    colGradient = c('red3', 'royalblue'),
    drawConnectors = TRUE,
    hline = c(10e-8),
    widthConnectors = 0.5)
```

![](RNA-seq_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

Many common statistical methods for exploratory analysis of
multidimensional data, for example clustering and principal components
analysis (PCA), work best for data that generally has the same range of
variance at different ranges of the mean values. When the expected
amount of variance is approximately the same across different mean
values, the data is said to be homoskedastic. For RNA-seq raw counts,
however, the variance grows with the mean. For example, if one performs
PCA directly on a matrix of size-factor-normalized read counts, the
result typically depends only on the few most strongly expressed genes
because they show the largest absolute differences between samples. A
simple and often used strategy to avoid this is to take the logarithm of
the normalized count values plus a small pseudocount; however, now the
genes with the very lowest counts will tend to dominate the results
because, due to the strong Poisson noise inherent to small count values,
and the fact that the logarithm amplifies differences for the smallest
values, these low count genes will show the strongest relative
differences between samples.

As a solution, DESeq2 offers transformations for count data that
stabilize the variance across the mean. One such transformation is the
regularized-logarithm transformation or rlog2. For genes with high
counts, the rlog transformation will give similar result to the ordinary
log2 transformation of normalized counts. For genes with lower counts,
however, the values are shrunken towards the genes’ averages across all
samples. Using an empirical Bayesian prior on inter-sample differences
in the form of a ridge penalty, the rlog-transformed data then becomes
approximately homoskedastic, and can be used directly for computing
distances between samples and making PCA plots. Another transformation
that similarly improves distance calculation across samples, the
variance stabilizing transformation24 implemented in the vst function,
is discussed alongside the rlog in the DESeq2 vignette.

``` r
vsdata <- vst(dds, blind=FALSE)
plotPCA(vsdata, intgroup="condition")
```

![](RNA-seq_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->

``` r
list <- c("ENSG00000188856.6","ENSG00000156076.10", "ENSG00000185069.2",
          "ENSG00000091128.13", "ENSG00000259781.1" ,  "ENSG00000134240.12")

par(mfrow=c(2,3))
for(i in list){
  plotCounts(dds, gene= i, intgroup="condition")
  }
```

![](RNA-seq_files/figure-gfm/unnamed-chunk-14-1.png)<!-- -->

In DESeq2, the function plotMA shows the log2 fold changes attributable
to a given variable over the mean of normalized counts for all the
samples in the DESeqDataSet. Points will be colored red if the adjusted
p value is less than 0.1. Points which fall out of the window are
plotted as open triangles pointing either up or down. It is more useful
visualize the MA-plot for the shrunken log2 fold changes, which remove
the noise associated with log2 fold changes from low count genes without
requiring arbitrary filtering thresholds. After calling plotMA, one can
use the function identify to interactively detect the row number of
individual genes by clicking on the plot. One can then recover the gene
identifiers by saving the resulting indices: The moderated log fold
changes proposed by Love, Huber, and Anders (2014) use a normal prior
distribution, centered on zero and with a scale that is fit to the data.
The shrunken log fold changes are useful for ranking and visualization,
without the need for arbitrary filters on low count genes. The normal
prior can sometimes produce too strong of shrinkage for certain
datasets. In DESeq2 version 1.18, we include two additional adaptive
shrinkage estimators, available via the type argument of lfcShrink. For
more details, see ?lfcShrink

The options for type are:

`apeglm` is the adaptive t prior shrinkage estimator from the apeglm
package (Zhu, Ibrahim, and Love 2018). As of version 1.28.0, it is the
default estimator.

`ashr` is the adaptive shrinkage estimator from the ashr package
(Stephens 2016). Here DESeq2 uses the ashr option to fit a mixture of
Normal distributions to form the prior, with method=“shrinkage”.

`normal` is the the original DESeq2 shrinkage estimator, an adaptive
Normal distribution as prior.

``` r
plotMA(res, ylim=c(-5,5))
```

![](RNA-seq_files/figure-gfm/unnamed-chunk-15-1.png)<!-- -->

``` r
resLFC <- lfcShrink(dds, coef="condition_pos_vs_neg", type="apeglm")
resNorm <- lfcShrink(dds, coef=2, type="normal")
resAsh <- lfcShrink(dds, coef=2, type="ashr")

par(mfrow=c(1,3), mar=c(4,4,2,1))

plotMA(resLFC,ylim= c(.005,.005), main="apeglm")
plotMA(resNorm,ylim= c(-3,3), main="normal")
plotMA(resAsh,ylim= c(-5,5),main="ashr")
```

![](RNA-seq_files/figure-gfm/unnamed-chunk-16-1.png)<!-- -->

``` r
#reset par
```

Beginning with the first row, all shrinkage methods provided by DESeq2
are good for ranking genes by “effect size”, that is the log2 fold
change (LFC) across groups, or associated with an interaction term. It
is useful to contrast ranking by effect size with ranking by a p-value
or adjusted p-value associated with a null hypothesis: while increasing
the number of samples will tend to decrease the associated p-value for a
gene that is differentially expressed, the estimated effect size or LFC
becomes more precise. Also, a gene can have a small p-value although the
change in expression is not great, as long as the standard error
associated with the estimated LFC is small.

The next two rows point out that apeglm and ashr shrinkage methods help
to preserve the size of large LFC, and can be used to compute s-values.
These properties are related. As noted in the previous section, the
original DESeq2 shrinkage estimator used a Normal distribution, with a
scale that adapts to the spread of the observed LFCs. Because the tails
of the Normal distribution become thin relatively quickly, it was
important when we designed the method that the prior scaling is
sensitive to the very largest observed LFCs. As you can read in the
DESeq2 paper, under the section, “Empirical prior estimate”, we used the
top 5% of the LFCs by absolute value to set the scale of the Normal
prior (we later added weighting the quantile by precision). ashr,
published in 2016, and apeglm use wide-tailed priors to avoid shrinking
large LFCs. While a typical RNA-seq experiment may have many LFCs
between -1 and 1, we might consider a LFC of \>4 to be very large, as
they represent 16-fold increases or decreases in expression. ashr and
apeglm can adapt to the scale of the entirety of LFCs, while not
over-shrinking the few largest LFCs. The potential for over-shrinking
LFC is also why DESeq2’s shrinkage estimator is not recommended for
designs with interaction terms.

What are s-values? This quantity proposed by Stephens (2016) gives the
estimated rate of false sign among genes with equal or smaller s-value.
Stephens (2016) points out they are analogous to the q-value of Storey
(2003). The s-value has a desirable property relative to the adjusted
p-value or q-value, in that it does not require supposing there to be a
set of null genes with LFC = 0 (the most commonly used null hypothesis).
Therefore, it can be benchmarked by comparing estimated LFC and s-value
to the “true LFC” in a setting where this can be reasonably defined. For
these estimated probabilities to be accurate, the scale of the prior
needs to match the scale of the distribution of effect sizes, and so the
original DESeq2 shrinkage method is not really compatible with computing
s-values.

The last four rows explain differences in whether coefficients or
contrasts can have shrinkage applied by the various methods. All three
methods can use coef with either the name or numeric index from
resultsNames(dds) to specify which coefficient to shrink. normal and
apeglm also allow for a positive lfcThreshold to be specified, in which
case, they will return p-values and adjusted p-values or s-values for
the LFC being greater in absolute value than the threshold (see this
section for normal). For apeglm, setting a threshold means that the
s-values will give the “false sign or small” rate (FSOS) among genes
with equal or small s-value. We found FSOS to be a useful description
for when the LFC is either the wrong sign or less than the threshold
distance from 0.

# Citation

-   M. I. Love, W. Huber, S. Anders: Moderated estimation of fold change
    and dispersion for RNA-Seq data with DESeq2. bioRxiv (2014).
    <doi:10.1101/002832> \[1\]

-   Zhu, A., Ibrahim, J.G., Love, M.I. (2018) Heavy-tailed prior
    distributions for sequence count data: removing the noise and
    preserving large differences. Bioinformatics.
    10.1093/bioinformatics/bty895

-   Stephens, M. (2016) False discovery rates: a new deal.
    Biostatistics, 18:2. 10.1093/biostatistics/kxw041

-   Lauren Ashlock, Computational Biology Spring 2017, DESeq2 tutorial:
    <https://lashlock.github.io/compbio/R_presentation.html>

\-<https://www.bioconductor.org/packages/release/bioc/vignettes/EnhancedVolcano/inst/doc/EnhancedVolcano.html>
