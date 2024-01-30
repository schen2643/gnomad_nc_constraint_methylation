#!/usr/bin/env python
# coding: utf-8

import hail as hl
hl.init()



root = "gs://gnomad-nc-constraint-v31/methylation"
methyl_ht_37 = hl.import_table("{0}/GSE81233_Sperm.merged.mean2.2hl.bed".format(root),
                               delimiter='\t', min_partitions=1000,
                               types = {'locus': hl.tlocus('GRCh37'),'methyl_level': hl.tfloat64,
                                       }).key_by('locus')

for f in [
    "GSE81233_Oocyte.merged.mean2.2hl.bed",
    "GSE81233_PN.merged.mean2.2hl.bed",
    "GSE81233_2-cell.merged.mean2.2hl.bed",
    "GSE81233_4-cell.merged.mean2.2hl.bed",
    "GSE81233_8-cell.merged.mean2.2hl.bed",
    "GSE81233_Morula.merged.mean2.2hl.bed",
    "GSE49828_WGBS_ICM.merged.mean2.2hl.bed",
    

    "GSE63818_PGC_7W.merged.mean2.2hl.bed",
    "GSE63818_PGC_10W.merged.mean2.2hl.bed",
    "GSE63818_PGC_11W.merged.mean2.2hl.bed",
    "GSE63818_PGC_13W.merged.mean2.2hl.bed",
    "GSE63818_PGC_17W.merged.mean2.2hl.bed",
    "GSE63818_PGC_19W.merged.mean2.2hl.bed"]:
    
    
    ht = hl.import_table(root+"/"+f,
                         delimiter='\t', min_partitions=1000,
                         types = {'locus': hl.tlocus('GRCh37'),
                                  'methyl_level': hl.tfloat64,
                                 }).key_by('locus')
    
    methyl_ht_37 = methyl_ht_37.join(ht,how="outer")
    

rg37 = hl.get_reference('GRCh37')  
rg38 = hl.get_reference('GRCh38')  
rg37.add_liftover('gs://hail-common/references/grch37_to_grch38.over.chain.gz', rg38) 



methyl_ht_38 = methyl_ht_37.annotate(new_locus=hl.liftover(methyl_ht_37.locus, 'GRCh38'),
                                     old_locus=methyl_ht_37.locus)  

methyl_ht_38 = methyl_ht_38.key_by(locus=methyl_ht_38.new_locus)  

methyl_ht_38.write("{0}/methylation_dev_stages_liftover.ht".format(root))



