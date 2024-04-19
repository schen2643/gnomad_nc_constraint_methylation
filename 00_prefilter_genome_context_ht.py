#!/usr/bin/env python
# coding: utf-8

import hail as hl
hl.init()


import sys
sys.path.append('/home/siwei')

from generic import *
from constraint_basics import *



def remove_coverage_outliers(t: Union[hl.MatrixTable, hl.Table]) -> Union[hl.MatrixTable, hl.Table]:
    """
    Keep only loci where genome coverage was between 15 and 60
    """
    criteria = (t.coverage_mean >= 15) & (t.coverage_mean <= 60)
    return t.filter_rows(criteria) if isinstance(t, hl.MatrixTable) else t.filter(criteria)



context_ht = hl.read_table("gs://gnomad-nc-constraint-v31-paper/context_prepared.ht")
genome_ht = hl.read_table("gs://gnomad-nc-constraint-v31-paper/genome_prepared.ht")

filter_to_autosomes_par(remove_coverage_outliers(context_ht)).write("gs://gnomad-nc-constraint-v31-paper/context_prefiltered.ht")
filter_to_autosomes_par(remove_coverage_outliers(genome_ht)).write("gs://gnomad-nc-constraint-v31-paper/genome_prefiltered.ht")

# chrX
context_x_ht = hl.read_table("gs://gnomad-nc-constraint-v31-paper/context_prepared_chrX.ht")
genome_x_ht = hl.read_table("gs://gnomad-nc-constraint-v31-paper/genome_prepared_chrX.ht")

filter_to_autosomes_par(remove_coverage_outliers(conte_xxt_ht)).write("gs://gnomad-nc-constraint-v31-paper/context_prefiltered_chrX.ht")
filter_to_autosomes_par(remove_coverage_outliers(genome_x_ht)).write("gs://gnomad-nc-constraint-v31-paper/genome_prefiltered_chrX.ht")
