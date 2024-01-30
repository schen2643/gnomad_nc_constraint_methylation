import hail as hl
hl.init()


context_ht = hl.read_table('gs://gnomad-nc-constraint-v31/methylation/context_prepared_methyl_CpG.ht')

grouping_variables = ('Sperm_raw','Oocyte_raw','PN_raw','C2_raw','C4_raw','C8_raw','Morula_raw','ICM_raw',
                      'PGC_7W_raw','PGC_10W_raw','PGC_11W_raw','PGC_13W_raw','PGC_17W_raw','PGC_19W_raw')
grouping_variables2 = list(grouping_variables) + ['Sperm_methyl_level','Oocyte_methyl_level','PN_methyl_level',
                                                 'C2_methyl_level','C4_methyl_level','C8_methyl_level',
                                                 'Morula_methyl_level','ICM_methyl_level','PGC_7W_methyl_level',
                                                 'PGC_10W_methyl_level','PGC_11W_methyl_level','PGC_13W_methyl_level',
                                                 'PGC_17W_methyl_level','PGC_19W_methyl_level','context']
grouping_variables2 = tuple(grouping_variables2)

context_ht = context_ht.filter( hl.all(lambda x: x, [hl.is_defined(context_ht[x]) for x in grouping_variables])).select(*grouping_variables2)

genome_ht = hl.read_table('gs://gnomad-nc-constraint-v31/genome_prefiltered.ht')
genome_join = genome_ht[context_ht.key]

af_cutoff = 0.001
context_ht = context_ht.filter(
    hl.is_missing(genome_join) | (
        (genome_join.freq[0].AF <= af_cutoff) & genome_join.pass_filters
    )
)

genome_ht = genome_ht.filter(
    (genome_ht.freq[0].AF <= af_cutoff) & genome_ht.pass_filters
)

context_ht = context_ht.annotate(obs = hl.is_defined(genome_ht[context_ht.key]))

context_ht.export('gs://gnomad-nc-constraint-v31/methylation/context_methyl_CpG_14_obs01_passaf01.txt')

