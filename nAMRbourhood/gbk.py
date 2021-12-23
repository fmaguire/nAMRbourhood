#!/usr/bin/env python

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def get_proteins_from_gbk(gbk_fp, faa_fp):
    """
    Extract protein sequences from a GBK file and write to fasta
    """
    proteins = []
    with open(gbk_fp) as gbk_fh:
        for record in SeqIO.parse(gbk_fh, 'genbank'):
            for feature in record.features:
                if feature.type == 'CDS' and 'pseudo' not in feature.qualifiers:
                    proteins.append(\
                            SeqRecord(
                                Seq(record.qualifiers['translation'][0]),
                                id=record.qualifiers['locus_tag'][0],
                                name=record.name))
    with open(faa_fp) as out_fh:
        SeqIO.write(proteins, out_fh, "fasta-2line")
