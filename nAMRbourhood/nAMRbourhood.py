#!/usr/bin/env python

from nAMRbourhood import utils
from nAMRbourhood import gbk

from pathlib import Path
import tqdm


def run(args):

    output_dir = utils.initialise(args)
    utils.check_dependencies()

    logging.info("Identifying focal genes (AMR) in gbk")
    ## get neighbourhood
    for input_gbk in tqdm.tqdm(args.input):
        gbk.get_proteins_from_gbk(input_gbk, faa_fp)
        # run RGI with threshold for loose
        # for each hit in RGI output extract neighbourhood with windowsize
        # store neighbourhoods across all genomes in AMR keyed datastructurs

    ## cluster neighbourhoods
    #for each amr neighbourhood set:
        # get all proteins from gbks in set
        # cluster proteins at 100% ID to dereplicate (to reduce work)
        # cluster proteins at user defined threshold
        # get normalised bitscores for all pairs of sequences in each cluster
        # calculate dissimilarity between all neighbourhood pairs (max theoretical sum of norm bitscores - sum of norm bitscores)
        # UPGMA clustering of matrix (modularised)
        # representative subset using user cluster information (generating diagnostic plot)

    ## visualise neighbourhoods
    # for each representative subset:
        # feed subset into clinker viz (maintaining consistent colourscheme)




