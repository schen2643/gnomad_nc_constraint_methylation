#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np

# awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $3,$4,$5,$6}' context_prepared_methyl14_weighted_logit.txt | sed /chrX/d | sed /chrY/d | sed /chrM/d > context_prepared_methyl14_weighted_logit.bed &


df_met = pd.read_csv("context_prepared_methyl14_weighted_logit.bed",sep="\t")

conditions = [
    (df_met['methyl14_weighted_logit'] > 0.9),
    (df_met['methyl14_weighted_logit'] > 0.85) & (df_met['methyl14_weighted_logit'] <= 0.9),
    (df_met['methyl14_weighted_logit'] > 0.8) & (df_met['methyl14_weighted_logit'] <= 0.85),
    (df_met['methyl14_weighted_logit'] > 0.75) & (df_met['methyl14_weighted_logit'] <= 0.8),
    (df_met['methyl14_weighted_logit'] > 0.7) & (df_met['methyl14_weighted_logit'] <= 0.75),
    (df_met['methyl14_weighted_logit'] > 0.65) & (df_met['methyl14_weighted_logit'] <= 0.7),
    (df_met['methyl14_weighted_logit'] > 0.6) & (df_met['methyl14_weighted_logit'] <= 0.65),
    (df_met['methyl14_weighted_logit'] > 0.55) & (df_met['methyl14_weighted_logit'] <= 0.6),
    (df_met['methyl14_weighted_logit'] > 0.5) & (df_met['methyl14_weighted_logit'] <= 0.55),
    (df_met['methyl14_weighted_logit'] > 0.3) & (df_met['methyl14_weighted_logit'] <= 0.5),
    (df_met['methyl14_weighted_logit'] > 0.25) & (df_met['methyl14_weighted_logit'] <= 0.3),
    (df_met['methyl14_weighted_logit'] > 0.2) & (df_met['methyl14_weighted_logit'] <= 0.25),
    (df_met['methyl14_weighted_logit'] > 0.15) & (df_met['methyl14_weighted_logit'] <= 0.2),
    (df_met['methyl14_weighted_logit'] > 0.1) & (df_met['methyl14_weighted_logit'] <= 0.15),
    (df_met['methyl14_weighted_logit'] > 0.05) & (df_met['methyl14_weighted_logit'] <= 0.1),
    (df_met['methyl14_weighted_logit'] <= 0.05)
    ]

# create a list of the values we want to assign for each condition
values = list(range(0,len(conditions)))[::-1]
# create a new column and use np.select to assign values to it using our lists as arguments
df_met['methy_level'] = np.select(conditions, values)

df_met[["chrom","start","end","methy_level"]].to_csv(
    'context_prepared_methyl14_weighted_logit.methyl_level.bed', 
    index=False,
    header=False,
    sep="\t", quoting=csv.QUOTE_NONE)


