#!/usr/bin/env python3

"""
Parse a sorted BAM file to generate two tables:
a table of alignment summary statistics ('_stats.tsv'), including fold-coverages
(fold_cov) and proportions of target lengths covered by mapped reads (prop_cov),
and a table of read depths ('_depth.tsv') for each bp position of each target.

Dependencies: python=3.10.8, pandas=1.5.2, samtools=1.16.1
Other package versions may work but are untested.
"""

__author__ = 'Liam Brown'
__email__ = 'liam.brown@inspection.gc.ca'

import argparse
import sys
from .aligncov import (
    compute_alignment_stats,
    compute_depth,
    compute_len_cov,
    join_dfs,
    write_dfs
)


def main():
    """
    Parse command-line arguments and execute script
    """
    parser = argparse.ArgumentParser(
        description = """
        Parse a sorted BAM file to generate two tables:
        a table of alignment summary statistics ('_stats.tsv'), including 
        fold-coverages (fold_cov) and proportions of target lengths covered by
        mapped reads (prop_cov), and a table of read depths ('_depth.tsv') for
        each bp position of each target.  
        """)

    # Required arguments
    required_args = parser.add_argument_group('Required')
    required_args.add_argument('-i', '--input', type = str, required = True,
        help = """
        Path to sorted BAM file to process.
        """)
        
    # Optional arguments
    optional_args = parser.add_argument_group('Optional')
    optional_args.add_argument('-o', '--output', type = str, required = False,
        default = 'sample',
        help = """
        Path and base name of files to save as tab-separated tables
        ('[output]_stats.tsv', '[output]_depth.tsv').
        Default: 'sample'
        """)

    args = parser.parse_args()
 
    idxstats_df = compute_alignment_stats(bamfile = args.input)
    depth_df, total_depth_df = compute_depth(bamfile = args.input)
    len_cov_df = compute_len_cov(depth_df)
    joined_df = join_dfs(idxstats_df, total_depth_df, len_cov_df)
    write_dfs(joined_df, depth_df, outbasename = args.output)


if __name__ == "__main__":
    sys.exit(main())