# Answers to Part 2
## Task 1
I consider my implementation to be complete.
However, it would be nice to be able to add SMTP configuration and a nicer e-mail template.
Therefore, the e-mail notification might not work actually as I was unable to test it.

## Task 2

a.  Depending on the data type (RNA seq or microarray), there might be the need for a different tools and resources. I am assuming RNA-seq for brevity.
First, I would obtain a data from healthy individuals to perfrom the DE analysis against. GTEx provides expression data from skin tissue from a large number of samples.
I would use DESeq2 to perfrom the DE analysis itself.
The genes are filtered by log fold change and adjusted p-value (FDR < 0.05) to obtain the differentially expressed.
For the gene-set enrichment analysis, I think clusterProfiler is a good choice as it integrates with the annotation available in Bioconductor and provides functions for evaluation and visualization.

b. GSEA can take quite a while to compute if there are many genes to be analysed.
In addition, it does not incorporate known pathway relationships such as activation and inhibition.

c. At first glance green and blue seem to share a common signature of up- and down-regulation, whereas the signature seems to be opposite in red.
The plot does suggest that there are some shared patterns between green and blue but this would definitely need some more testing as the figure does not show a clear-cut picture.

## Task3
As I had previously agreed to deliver results from three other projects during the coming week, I would kindly ask the fourth user if it was possible for them to get an extension for the revision.
If this is not possible, I would either see if there is a colleague who is also familiar with any of the projects to provide some back up.
If anything else fails, I'd have to ask any of the other users if they were able to wait another week.


## Task 4
I would be honest with them that I am not familiar with that analysis, yet.
I would either refer them to a colleague who might have better knowledge of the technique if this analysis is urgent.
If there is none or they are occupied, I would tell my partners that it might take a few more days as I have to get set up but I'd be happy to learn.

## Task 5
I would be honest with them that there was a mistake and fix it.
I'd also make sure not to make the same mistake again.
Depending on the user, I might ask how they figured it out so I can follow the same steps as sanity checks in the future.