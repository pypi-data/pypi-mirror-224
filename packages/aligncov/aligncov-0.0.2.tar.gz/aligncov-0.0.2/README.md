[![PyPI version](https://badge.fury.io/py/aligncov.svg)](https://badge.fury.io/py/aligncov)

# AlignCov

AlignCov is a bioinformatics tool which can be used to obtain a) alignment summary statistics and b) read depths from sorted BAM files in tidy tab-separated tables.

## Future plans

- [ ] Create a Bioconda recipe
- [ ] Create a Docker image

## Introduction

This script takes a sorted BAM file as input and uses [SAMtools](http://samtools.sourceforge.net/) and Python [Pandas](https://pandas.pydata.org/) to generate two tables:

- `_stats.tsv`: A table of alignment summary statistics, including fold-coverages (fold_cov) and proportions of target lengths covered by mapped reads (prop_cov).
  - target: Name of the target.
  - seqlen: Length of the target sequence (bp).
  - depth: Total number of base pairs mapped to the target.
  - len_cov: Total number of base pairs within the target that are covered by at least one mapped read.
  - prop_cov: Proportion of the target length covered by at least one mapped read (len_cov / seqlen).
  - fold_cov: Fold-coverage of mapped reads to the target (i.e. the number of times the target is completely covered by mapped reads) (depth / seqlen).
- `_depth.tsv`: A table of read depths for each bp position of each target.
  - target: Name of the target.
  - position: Base pair position within the target.
  - depth: Total number of reads aligned to the base pair position within the target.

## Dependencies

- `samtools>=1.15`

## Installation

AlignCov can be installed using Pip with the following command:

```bash
pip install aligncov
```

## Usage

### Quick start

For a sorted BAM file named 'bacillus.bam', compute alignment statistics and read depths, and save results to files named 'subtilis_stats.tsv' and 'subtilis_depth.tsv':

```bash
$ aligncov -i bacillus.bam -o subtilis
```

### More options

To show the program's help message:

```
$ aligncov -h
usage: aligncov [-h] -i INPUT [-o OUTPUT]

Parse a sorted BAM file to generate two tables: a table of alignment summary statistics ('_stats.tsv'), including fold-coverages (fold_cov) and proportions of target lengths covered by mapped reads (prop_cov), and a table of read
depths ('_depth.tsv') for each bp position of each target.

options:
  -h, --help            show this help message and exit

Required:
  -i INPUT, --input INPUT
                        Path to sorted BAM file to process.

Optional:
  -o OUTPUT, --output OUTPUT
                        Path and base name of files to save as tab-separated tables ('[output]_stats.tsv', '[output]_depth.tsv'). Default: 'sample'
```

## Credits

### Packages

- [Pandas](https://pandas.pydata.org/): McKinney W. 2011. Pandas: A foundation python library for data analysis and statistics. Python for High Performance and Scientific Computing 1–9.

### Dependencies

- [SAMtools](http://www.htslib.org/): Danecek P, Bonfield JK, Liddle J, Marshall J, Ohan V, Pollard MO, Whitwham A, Keane T, McCarthy SA, Davies RM, Li H. 2021. Twelve years of SAMtools and BCFtools. GigaScience 10(2) giab008. doi: [10.1093/gigascience/giab008](doi.org/10.1093/gigascience/giab008)

### Project structure

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage) project template.
