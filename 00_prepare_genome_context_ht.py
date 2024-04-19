#!/usr/bin/env python
# coding: utf-8

import hail as hl
hl.init()


import sys
sys.path.append('/home/siwei')

from generic import *
from constraint_basics import *



context_ht = hl.read_table("gs://gcp-public-data--gnomad/resources/context/grch38_context_vep_annotated.ht")
coverage_ht = hl.read_table("gs://gcp-public-data--gnomad/release/3.0.1/coverage/genomes/gnomad.genomes.r3.0.1.coverage.ht")

trimer = False
context_ht = context_ht.annotate(ref=context_ht.alleles[0], alt=context_ht.alleles[1])
context_ht = context_ht.filter((hl.len(context_ht.ref) == 1) & (hl.len(context_ht.alt) == 1) & context_ht.context.matches(f'[ATCG]{{{str_len}}}'))
context_ht = annotate_variant_types(collapse_strand(context_ht), not trimer)

context_ht = context_ht.annotate(
	coverage_mean=coverage_ht[context_ht.locus].mean,
	coverage_median=coverage_ht[context_ht.locus].median_approx)

################
# these were later dropped and replaced by new methylation data 
# root = "gs://gnomad-nc-constraint-v31/methylation"
# methyl_ht_1 = hl.import_table('{0}/ENCFF918PML.sorted.perc_combined.short.pos2.sorted.rf2ht.txt'.format(root),
#     delimiter='\t', min_partitions=1000,
#     types={'locus': hl.tlocus('GRCh38'), 'methyl_level': hl.tfloat64}).key_by('locus')
# methyl_ht_2 = hl.read_table('{0}/methyl_h1_GSM429321_liftover.ht'.format(root))

# context_ht = context_ht.annotate(
# 	methylation_ENCFF918PML = methyl_ht_1[context_ht.locus].methyl_level, 
# 	methylation_GSM429321 = methyl_ht_2[context_ht.locus].methyl_level)

# annotation = {
#     'methylation_level_ENCFF918PML': hl.case().when(
#         context_ht.cpg & (hl.is_defined(context_ht.methylation_ENCFF918PML) == hl.literal(False)), -1
#     ).when(
#         context_ht.cpg & (context_ht.methylation_ENCFF918PML>0.6), 2
#     ).when(
#         context_ht.cpg & (context_ht.methylation_ENCFF918PML>=0.2), 1
#     ).default(0),

#     'methylation_level_GSM429321': hl.case().when(
#         context_ht.cpg & (hl.is_defined(context_ht.methylation_GSM429321) == hl.literal(False)), -1
#     ).when(
#         context_ht.cpg & (context_ht.methylation_GSM429321>0.6), 2
#     ).when(
#         context_ht.cpg & (context_ht.methylation_GSM429321>=0.2), 1
#     ).default(0)

# }
# context_ht = context_ht.annotate(**annotation)
################

context_ht.write("gs://gnomad-nc-constraint-v31/context_prepared.ht")



# Annotate new methylation data for public bucket
context_ht = hl.read_table('gs://gnomad-nc-constraint-v31/context_prepared.ht')

fields_to_drop = ['coverage_10','coverage_20','methyl_mean','coverage_median','methylation_ENCFF918PML','methylation_GSM429321','methylation_level_ENCFF918PML','methylation_level_GSM429321']
context_ht = context_ht.drop(*fields_to_drop)

met_ht = hl.read_table('gs://gnomad-nc-constraint-v31/methylation/context_prepared_methyl14_weighted_logit.ht')
annotation = {
    'methyl14_weighted_logit_level': hl.case().when(
        met_ht.methyl14_weighted_logit > 0.9, 15
    ).when(
        met_ht.methyl14_weighted_logit > 0.85, 14
    ).when(
        met_ht.methyl14_weighted_logit > 0.8, 13
    ).when(
        met_ht.methyl14_weighted_logit > 0.75, 12
    ).when(
        met_ht.methyl14_weighted_logit > 0.7, 11
    ).when(
        met_ht.methyl14_weighted_logit > 0.65, 10
    ).when(
        met_ht.methyl14_weighted_logit > 0.6, 9
    ).when(
        met_ht.methyl14_weighted_logit > 0.55, 8
    ).when(
        met_ht.methyl14_weighted_logit > 0.5, 7
    ).when(
        met_ht.methyl14_weighted_logit > 0.3, 6
    ).when(
        met_ht.methyl14_weighted_logit > 0.25, 5
    ).when(
        met_ht.methyl14_weighted_logit > 0.2, 4
    ).when(
        met_ht.methyl14_weighted_logit > 0.15, 3
    ).when(
        met_ht.methyl14_weighted_logit > 0.1, 2
    ).when(
        met_ht.methyl14_weighted_logit > 0.05, 1
    ).default(0)
    }
met_ht = met_ht.annotate(**annotation)
context_ht = context_ht.annotate(methyl_level=hl.if_else(hl.is_missing(met_ht[context_ht.key]), 0, met_ht[context_ht.key].methyl14_weighted_logit_level))
context_ht.write("gs://gnomad-nc-constraint-v31-paper/context_prepared.ht")

genome_ht = hl.read_table("gs://gcp-public-data--gnomad/release/3.1/ht/genomes/gnomad.genomes.v3.1.sites.ht")
genome_ht = genome_ht.annotate(**context_ht[genome_ht.key], pass_filters=hl.len(genome_ht.filters) == 0)
genome_ht.write("gs://gnomad-nc-constraint-v31-paper/genome_prepared.ht")


# chrX
context_ht = hl.read_table("gs://gnomad-nc-constraint-v31/context_prepared.ht")
genome_ht = hl.read_table("gs://gnomad-nc-constraint-v31/genome_prepared.ht")

context_x_ht = context_ht.filter(context_ht.locus.in_x_nonpar())
genome_x_ht = genome_ht.filter(genome_ht.locus.in_x_nonpar())

context_x_ht.write("gs://gnomad-nc-constraint-v31/context_prepared_chrX.ht")
genome_x_ht.write("gs://gnomad-nc-constraint-v31/genome_prepared_chrX.ht")

