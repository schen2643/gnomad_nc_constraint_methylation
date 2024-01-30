#!/usr/bin/env python
# coding: utf-8

import hail as hl
hl.init()

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression



df = pd.read_table(
    "context_methyl_CpG_14_obs01_passaf01_x.txt",
    header=0, index_col=0)

l = ['Sperm_raw','Oocyte_raw','PN_raw','C2_raw','C4_raw',
     'C8_raw','Morula_raw','ICM_raw','PGC_7W_raw','PGC_10W_raw',
     'PGC_11W_raw','PGC_13W_raw','PGC_17W_raw','PGC_19W_raw',]
df_x = df[l]
df_y = df["obs"]

clf = LogisticRegression(random_state=0).fit(df_x, df_y)
var = df_x.columns.to_list()
for i in var:
    print (i, clf.coef_[0][var.index(i)])

# Sperm_raw 1.2142327678822575
# Oocyte_raw -0.10153058557280095
# PN_raw 0.2096996493626876
# C2_raw 0.08246182249615806
# C4_raw 0.0803666551372927
# C8_raw 0.040510820716452144
# Morula_raw 0.2502153273086105
# ICM_raw 0.0682508020601786
# PGC_7W_raw 0.624121048631128
# PGC_10W_raw 1.015123980247576
# PGC_11W_raw 1.1535398138908222
# PGC_13W_raw 0.24685249760735126
# PGC_17W_raw 0.5309602092634527
# PGC_19W_raw 0.37232732130631524


met_ht = hl.read_table('gs://gnomad-nc-constraint-v31/methylation/context_prepared_methyl_CpG.ht')
met_ht = met_ht.filter(met_ht.locus.in_x_nonpar()) 

coeff = {
    "Sperm_raw" : 1.2142327678822575,
    "Oocyte_raw" : -0.10153058557280095,
    "PN_raw" : 0.2096996493626876,
    "C2_raw" : 0.08246182249615806,
    "C4_raw" : 0.0803666551372927,
    "C8_raw" : 0.040510820716452144,
    "Morula_raw" : 0.2502153273086105,
    "ICM_raw" : 0.0682508020601786,
    "PGC_7W_raw" : 0.624121048631128,
    "PGC_10W_raw" : 1.015123980247576,
    "PGC_11W_raw" : 1.1535398138908222,
    "PGC_13W_raw" : 0.24685249760735126,
    "PGC_17W_raw" : 0.5309602092634527,
    "PGC_19W_raw" : 0.37232732130631524,
}


weights = dict([k,np.exp(coeff[k])] for k in coeff)

met_ht = met_ht.annotate(methyl14_weighted_logit = 
                         sum([
                             met_ht.Sperm*weights["Sperm_raw"],
                             met_ht.Oocyte*weights["Oocyte_raw"],
                             met_ht.PN*weights["PN_raw"],
                             met_ht.C2*weights["C2_raw"],
                             met_ht.C4*weights["C4_raw"],
                             met_ht.C8*weights["C8_raw"],
                             met_ht.Morula*weights["Morula_raw"],
                             met_ht.ICM*weights["ICM_raw"],
                             met_ht.PGC_7W*weights["PGC_7W_raw"],
                             met_ht.PGC_10W*weights["PGC_10W_raw"],
                             met_ht.PGC_11W*weights["PGC_11W_raw"],
                             met_ht.PGC_13W*weights["PGC_13W_raw"],
                             met_ht.PGC_17W*weights["PGC_17W_raw"],
                             met_ht.PGC_19W*weights["PGC_19W_raw"]]
                         ) / sum(weights.values()) )



met_ht.select('context', 'ref', 'alt', 'methyl14_weighted_logit').write('gs://gnomad-nc-constraint-v31/methylation/context_prepared_methyl14_weighted_logit_x.ht')


met_ht = hl.read_table('gs://gnomad-nc-constraint-v31/methylation/context_prepared_methyl14_weighted_logit_x.ht')
met_ht = met_ht.annotate(chrom=met_ht.locus.contig, 
                         start=met_ht.locus.position-1,
                         end=met_ht.locus.position,
                        )
met_ht.select("chrom","start","end","methyl14_weighted_logit").export(
    "gs://gnomad-nc-constraint-v31/methylation/context_prepared_methyl14_weighted_logit_x.txt")






