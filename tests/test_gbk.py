import tempfile
import os
from Bio import SeqIO
from nAMRbourhood import gbk

# This just tests that pytest can find the tests.
def test_tests():
    assert True

def test_gbk_reader():
    temp_f = tempfile.NamedTemporaryFile('w')
    gbk.get_proteins_from_gbk(os.getcwd()+'/tests/test_data/one_locus.gbk', temp_f.name)
    fa = list(SeqIO.parse(temp_f.name, 'fasta-2line'))
    #117 valid proteins in "one_locus.gbk"
    assert len(fa) == 117
