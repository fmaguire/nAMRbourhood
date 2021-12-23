#!/usr/bin/env python
import argparse
from nAMRbourhood import __version__
from nAMRbourhood import nAMRbourhood

def main():

    parser = argpaser.ArgumentParser(description=\
                             f"nAMRbourhood (v{__version__}): "
                             "Identify and compare genomic contexts for focal "
                              "genes across genomes",
                              usage='nAMRbourhood <command> <options>')
    parser.add_argument('-v', '--version', action='version',
                        version=f"%(prog)s {__version__}")

    parser.add_argument("--input", "-i", required=True,
                        nargs="+",
                        help="List of gbk formatted genomes to use as input")

    parser.add_argument("--threshold", "-t", default=70,
                        help="Minimum detection threshold to include "
                             "focal genes (using threshold_metric)")
    parser.add_argument("--threshold_metric", "--tm", default='%ID',
                        choices=['%ID', 'bitscore', 'e-value', 'coverage'],
                        help="Metric to use for minimum focal gene detection "
                             "threshold")

    parser.add_argument("--window_size", "-w", default=5, type=int,
                        help="Size of the neighbourhood around focal gene to "
                             "use")
    parser.add_argument("--window_size_unit", "--wsu", default='genes',
                        choices=['genes', 'kbp'],
                        help='Unit to use to define window size')

    parser.add_argument("--cluster_threshold", "-c", default=95,
                        help="Clustering threshold comparing neighbourhoods")
    parser.add_argument("--number_of_clusters", "--nc", default=5,
                        help="Number of representative clusters per focal"
                             " neighbourhood")

    parser.add_argument("--output_dir", "-o", default=False,
                        help="Output folder")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing output folder")

    parser.add_argument('-j', '--num_threads', default=1, type=int,
                        help="Number of threads to use")
    parser.add_argument('--debug', action='store_true', default=False,
                        help="Run in debug mode")
    parser.add_argument('--verbose', action='store_true', default=False,
                        help="Run with verbose output")

    args = parser.parse_args()


    nAMRbourhood.run(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
