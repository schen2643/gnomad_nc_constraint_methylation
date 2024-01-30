#!/usr/bin/env python
# coding: utf-8

import hail as hl
hl.init()


context_ht = hl.read_table('gs://gnomad-nc-constraint-v31/context_prepared.ht')
context_ht = context_ht.filter(context_ht.cpg)

ht = hl.read_table("gs://gnomad-nc-constraint-v31/methylation/methylation_dev_stages_liftover.ht")


# 1. annotate raw methyl
context_ht = context_ht.annotate(
    Sperm_raw = ht[context_ht.locus].methyl_level,
    Oocyte_raw = ht[context_ht.locus].methyl_level_1,
    PN_raw = ht[context_ht.locus].methyl_level_2,
    C2_raw = ht[context_ht.locus].methyl_level_3,
    C4_raw = ht[context_ht.locus].methyl_level_4,
    C8_raw = ht[context_ht.locus].methyl_level_5,
    Morula_raw = ht[context_ht.locus].methyl_level_6,
    ICM_raw = ht[context_ht.locus].methyl_level_7,
    PGC_7W_raw = ht[context_ht.locus].methyl_level_8,
    PGC_10W_raw = ht[context_ht.locus].methyl_level_9,
    PGC_11W_raw = ht[context_ht.locus].methyl_level_10,
    PGC_13W_raw = ht[context_ht.locus].methyl_level_11,
    PGC_17W_raw = ht[context_ht.locus].methyl_level_12,
    PGC_19W_raw = ht[context_ht.locus].methyl_level_13,)


# 2. fill na with mean
Sperm_mean = ht.aggregate(hl.agg.mean(ht.methyl_level))
Oocyte_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_1))
PN_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_2))
C2_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_3))
C4_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_4))
C8_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_5))
Morula_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_6))
ICM_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_7))
W7_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_8))
W10_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_9))
W11_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_10))
W13_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_11))
W17_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_12))
W19_mean = ht.aggregate(hl.agg.mean(ht.methyl_level_13))

annotation = {
    
    'Sperm': hl.if_else(hl.is_missing(context_ht.Sperm_raw), Sperm_mean, context_ht.Sperm_raw),
    'Oocyte': hl.if_else(hl.is_missing(context_ht.Oocyte_raw), Oocyte_mean, context_ht.Oocyte_raw),
    'PN': hl.if_else(hl.is_missing(context_ht.PN_raw), PN_mean, context_ht.PN_raw),
    'C2': hl.if_else(hl.is_missing(context_ht.C2_raw), C2_mean, context_ht.C2_raw),
    'C4': hl.if_else(hl.is_missing(context_ht.C4_raw), C4_mean, context_ht.C4_raw),
    'C8': hl.if_else(hl.is_missing(context_ht.C8_raw), C8_mean, context_ht.C8_raw),
    'Morula': hl.if_else(hl.is_missing(context_ht.Morula_raw), Morula_mean, context_ht.Morula_raw),
    'ICM': hl.if_else(hl.is_missing(context_ht.ICM_raw), ICM_mean, context_ht.ICM_raw),
    'PGC_7W': hl.if_else(hl.is_missing(context_ht.PGC_7W_raw), W7_mean, context_ht.PGC_7W_raw),
    'PGC_10W': hl.if_else(hl.is_missing(context_ht.PGC_10W_raw), W10_mean, context_ht.PGC_10W_raw),
    'PGC_11W': hl.if_else(hl.is_missing(context_ht.PGC_11W_raw), W11_mean, context_ht.PGC_11W_raw),
    'PGC_13W': hl.if_else(hl.is_missing(context_ht.PGC_13W_raw), W13_mean, context_ht.PGC_13W_raw),
    'PGC_17W': hl.if_else(hl.is_missing(context_ht.PGC_17W_raw), W17_mean, context_ht.PGC_17W_raw),
    'PGC_19W': hl.if_else(hl.is_missing(context_ht.PGC_19W_raw), W19_mean, context_ht.PGC_19W_raw),

}

context_ht = context_ht.annotate(**annotation)


# 3. define level
annotation = {
    'Sperm_methyl_level': hl.case().when(
        context_ht.Sperm > 0.6, 2
    ).when(
        context_ht.Sperm > 0.2, 1
    ).default(0),
    
    'Oocyte_methyl_level': hl.case().when(
        context_ht.Oocyte > 0.6, 2
    ).when(
        context_ht.Oocyte > 0.2, 1
    ).default(0),
    
    'PN_methyl_level': hl.case().when(
        context_ht.PN > 0.6, 2
    ).when(
        context_ht.PN > 0.2, 1
    ).default(0),
    
    'C2_methyl_level': hl.case().when(
        context_ht.C2 > 0.6, 2
    ).when(
        context_ht.C2 > 0.2, 1
    ).default(0),
    
    'C4_methyl_level': hl.case().when(
        context_ht.C4 > 0.6, 2
    ).when(
        context_ht.C4 > 0.2, 1
    ).default(0),
    
    'C8_methyl_level': hl.case().when(
        context_ht.C8 > 0.6, 2
    ).when(
        context_ht.C8 > 0.2, 1
    ).default(0),
    
    'Morula_methyl_level': hl.case().when(
        context_ht.Morula > 0.6, 2
    ).when(
        context_ht.Morula > 0.2, 1
    ).default(0),
    
    'ICM_methyl_level': hl.case().when(
        context_ht.ICM > 0.6, 2
    ).when(
        context_ht.ICM > 0.2, 1
    ).default(0),
    
    'PGC_7W_methyl_level': hl.case().when(
        context_ht.PGC_7W > 0.6, 2
    ).when(
        context_ht.PGC_7W > 0.2, 1
    ).default(0),
    
    'PGC_10W_methyl_level': hl.case().when(
        context_ht.PGC_10W > 0.6, 2
    ).when(
        context_ht.PGC_10W > 0.2, 1
    ).default(0),
    
    'PGC_11W_methyl_level': hl.case().when(
        context_ht.PGC_11W > 0.6, 2
    ).when(
        context_ht.PGC_11W > 0.2, 1
    ).default(0),
    
    'PGC_13W_methyl_level': hl.case().when(
        context_ht.PGC_13W > 0.6, 2
    ).when(
        context_ht.PGC_13W > 0.2, 1
    ).default(0),
    
    'PGC_17W_methyl_level': hl.case().when(
        context_ht.PGC_17W > 0.6, 2
    ).when(
        context_ht.PGC_17W > 0.2, 1
    ).default(0),
    
    'PGC_19W_methyl_level': hl.case().when(
        context_ht.PGC_19W > 0.6, 2
    ).when(
        context_ht.PGC_19W > 0.2, 1
    ).default(0),
}

context_ht = context_ht.annotate(**annotation)


# 4. summarize level, max, sum
context_ht = context_ht.annotate(
    methyl_level_max = hl.max([
        context_ht.Sperm_methyl_level,
        context_ht.Oocyte_methyl_level,
        context_ht.PN_methyl_level,
        context_ht.C2_methyl_level,
        context_ht.C4_methyl_level,
        context_ht.C8_methyl_level,
        context_ht.Morula_methyl_level,
        context_ht.ICM_methyl_level,
        context_ht.PGC_7W_methyl_level,
        context_ht.PGC_10W_methyl_level,
        context_ht.PGC_11W_methyl_level,
        context_ht.PGC_13W_methyl_level,
        context_ht.PGC_17W_methyl_level,
        context_ht.PGC_19W_methyl_level
        ]),
    
    methyl_level_sum = hl.sum([
        context_ht.Sperm_methyl_level,
        context_ht.Oocyte_methyl_level,
        context_ht.PN_methyl_level,
        context_ht.C2_methyl_level,
        context_ht.C4_methyl_level,
        context_ht.C8_methyl_level,
        context_ht.Morula_methyl_level,
        context_ht.ICM_methyl_level,
        context_ht.PGC_7W_methyl_level,
        context_ht.PGC_10W_methyl_level,
        context_ht.PGC_11W_methyl_level,
        context_ht.PGC_13W_methyl_level,
        context_ht.PGC_17W_methyl_level,
        context_ht.PGC_19W_methyl_level
        ]),
)



context_ht.write('gs://gnomad-nc-constraint-v31/methylation/context_prepared_methyl_CpG.ht')











