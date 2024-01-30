#!/usr/bin/env python
# coding: utf-8

import hail as hl
hl.init()


root = "gs://gnomad-nc-constraint-v31/methylation"

# for f in ["GSE63818_PGC_10W_embryo1_F_rep1_methylation_calling.CpG", 
#           "GSE63818_PGC_10W_embryo1_F_rep2_methylation_calling.CpG", 
#           "GSE63818_PGC_10W_embryo1_M_methylation_calling.CpG", 
#           "GSE63818_PGC_10W_embryo2_M_PBAT_methylation_calling.CpG", 
#           "GSE63818_PGC_10W_embryo2_M_TA-PBAT_methylation_calling.CpG", 
#           "GSE63818_PGC_11W_embryo1_F_methylation_calling.CpG", 
#           "GSE63818_PGC_11W_embryo1_M_rep1_methylation_calling.CpG", 
#           "GSE63818_PGC_11W_embryo1_M_rep2_methylation_calling.CpG", 
#           "GSE63818_PGC_13W_embryo1_M_methylation_calling.CpG", 
#           "GSE63818_PGC_17W_embryo1_F_methylation_calling.CpG", 
#           "GSE63818_PGC_19W_embryo1_M_methylation_calling.CpG", 
#           "GSE63818_PGC_19W_embryo2_M_methylation_calling.CpG"]:

# for f in [
#     "GSM2481579_scBS-hSp8.Cmet.CpG",
#     "GSM2481580_scBS-hSp9.Cmet.CpG",
#     "GSM2481652_scBS-ZHB-Sp10.Cmet.CpG",
#     "GSM2481653_scBS-ZHB-Sp11.Cmet.CpG",
#     "GSM2481654_scBS-ZHB-Sp12.Cmet.CpG",
#     "GSM2481655_scBS-ZHB-Sp13.Cmet.CpG",
#     "GSM2481656_scBS-ZHB-Sp14.Cmet.CpG",
#     "GSM2481657_scBS-ZHB-Sp15.Cmet.CpG",
#     "GSM2481658_scBS-ZHB-Sp16.Cmet.CpG",
#     "GSM2481659_scBS-ZHB-Sp1.Cmet.CpG",
#     "GSM2481660_scBS-ZHB-Sp2.Cmet.CpG",
#     "GSM2481661_scBS-ZHB-Sp3.Cmet.CpG",
#     "GSM2481662_scBS-ZHB-Sp4.Cmet.CpG",
#     "GSM2481663_scBS-ZHB-Sp5.Cmet.CpG",
#     "GSM2481664_scBS-ZHB-Sp6.Cmet.CpG",
#     "GSM2481665_scBS-ZHB-Sp7.Cmet.CpG",
#     "GSM2481666_scBS-ZHB-Sp8.Cmet.CpG",
#     "GSM2481667_scBS-ZHB-Sp9.Cmet.CpG",
#     "GSM2986301_scBS-hSp10.Cmet.CpG",
#     "GSM2986302_scBS-hSP3.Cmet.CpG",
#     "GSM2986303_scBS-hSP5.Cmet.CpG"]:
    
    
# for f in [
#     "GSM2986306_scBS-B-GV1.Cmet.CpG",
#     "GSM2481553_scBS-D-GV-2.Cmet.CpG",
#     "GSM2481568_scBS-F-GV1.Cmet.CpG",
#     "GSM2481569_scBS-F-GV2.Cmet.CpG",
#     "GSM2481583_scBS-K-GV-2.Cmet.CpG",
#     "GSM2481584_scBS-K-GV-3.Cmet.CpG",
#     "GSM2146951_scBS-A-MII-1.Cmet.CpG",
#     "GSM2146952_scBS-A-MII-2.Cmet.CpG",
#     "GSM2146953_scBS-A-MII-3.Cmet.CpG",
#     "GSM2146954_scBS-A-MII-4.Cmet.CpG",
#     "GSM2986308_scBS-D-MII-1.Cmet.CpG",
#     "GSM2986310_scBS-D-MII-3.Cmet.CpG",
#     "GSM2986311_scBS-D-MII-4.Cmet.CpG",
#     "GSM2986312_scBS-D-MII-5.Cmet.CpG",
#     "GSM2986313_scBS-D-MII-6.Cmet.CpG",
#     "GSM2986314_scBS-D-MII-7.Cmet.CpG",
#     "GSM2986316_scBS-D-MII-9.Cmet.CpG",
#     "GSM2986317_scBS-E-MII-10.Cmet.CpG",
#     "GSM2481556_scBS-E-MII-19.Cmet.CpG",
#     "GSM2481557_scBS-E-MII-20.Cmet.CpG",
#     "GSM2986319_scBS-E-MII-3.Cmet.CpG",
#     "GSM2986320_scBS-G-MII-10.Cmet.CpG",
#     "GSM2986321_scBS-G-MII-11.Cmet.CpG",
#     "GSM2986322_scBS-G-MII-12.Cmet.CpG",
#     "GSM2481570_scBS-G-MII-13.Cmet.CpG",
#     "GSM2481581_scBS-J-MII-5.Cmet.CpG",
#     "GSM2481586_scBS-K-MII-1.Cmet.CpG",
#     "GSM2481587_scBS-K-MII-2.Cmet.CpG",
#     "GSM2481588_scBS-K-MII-3.Cmet.CpG",
#     "GSM2986323_scBS-L-MII-1.Cmet.CpG",
#     "GSM2986324_scBS-L-MII-2.Cmet.CpG",
#     "GSM2986325_scBS-L-MII-3.Cmet.CpG",
#     "GSM2986326_scBS-L-MII-4.Cmet.CpG",
#     "GSM2481589_scBS-M-MII-1.Cmet.CpG",
#     "GSM2481591_scBS-M-MII-3.Cmet.CpG"]:
    
# for f in [    
#     "GSM2986343_scBS-2C-10-1.Cmet.CpG",
#     "GSM2986344_scBS-2C-10-2.Cmet.CpG",
#     "GSM2986345_scBS-2C-1-1.Cmet.CpG",
#     "GSM2986347_scBS-2C-1-2.Cmet.CpG",
#     "GSM2986346_scBS-2C-11-1.Cmet.CpG",
#     "GSM2481532_scBS-2C-11-2.Cmet.CpG",
#     "GSM2481533_scBS-2C-6-1.Cmet.CpG",
#     "GSM2481534_scBS-2C-6-2.Cmet.CpG",
#     "GSM2986356_scBS-2C-7-1.Cmet.CpG",
#     "GSM2986357_scBS-2C-7-2.Cmet.CpG",
#     "GSM2481535_scBS-2C-8-1.Cmet.CpG",
#     "GSM2986358_scBS-2C-9-1.Cmet.CpG",
#     "GSM2986359_scBS-2C-9-2.Cmet.CpG",
#     "GSM2986360_scBS-4C-1-1.Cmet.CpG",
#     "GSM2986361_scBS-4C-1-2.Cmet.CpG",
#     "GSM2986362_scBS-4C-1-3.Cmet.CpG",
#     "GSM2986363_scBS-4C-1-4.Cmet.CpG",
#     "GSM2481536_scBS-4C-2-1.Cmet.CpG",
#     "GSM2481538_scBS-4C-2-4.Cmet.CpG",
#     "GSM2481539_scBS-4C-5-1.Cmet.CpG",
#     "GSM2481540_scBS-4C-5-3.Cmet.CpG",
#     "GSM2481541_scBS-4C-5-4.Cmet.CpG",
#     "GSM2481542_scBS-4C-6-1.Cmet.CpG",
#     "GSM2481543_scBS-4C-6-2.Cmet.CpG",
#     "GSM2481544_scBS-4C-6-4.Cmet.CpG",
#     "GSM2481546_scBS-4C-7-2.Cmet.CpG",
#     "GSM2481547_scBS-4C-7-3.Cmet.CpG",
#     "GSM2986364_scBS-E-4C-1.Cmet.CpG",
#     "GSM2986365_scBS-E-4C-2.Cmet.CpG",
#     "GSM2986366_scBS-E-4C-3.Cmet.CpG",
#     "GSM2986367_scBS-E-4C-4.Cmet.CpG",
#     "GSM2481628_scBS-8C-6-1.Cmet.CpG",
#     "GSM2481629_scBS-8C-6-2.Cmet.CpG",
#     "GSM2481630_scBS-8C-6-3.Cmet.CpG",
#     "GSM2481631_scBS-8C-6-4.Cmet.CpG",
#     "GSM2481632_scBS-8C-6-5.Cmet.CpG",
#     "GSM2481633_scBS-8C-6-6.Cmet.CpG",
#     "GSM2481634_scBS-8C-6-7.Cmet.CpG",
#     "GSM2481635_scBS-8C-6-8.Cmet.CpG",
#     "GSM2986382_scBS-8C-8-1.Cmet.CpG",
#     "GSM2986383_scBS-8C-8-2.Cmet.CpG"]:

    
    
    
# for f in [
#     "GSM2481571_scBS-H-PN1-1.Cmet.CpG",
#     "GSM2481572_scBS-H-PN1-2.Cmet.CpG",
#     "GSM2481573_scBS-H-PN2-1.Cmet.CpG",
#     "GSM2481574_scBS-H-PN2-2.Cmet.CpG",
#     "GSM2481576_scBS-H-PN3-2.Cmet.CpG",
#     "GSM2481577_scBS-H-PN4-1.Cmet.CpG",
#     "GSM2481578_scBS-H-PN4-2.Cmet.CpG",
#     "GSM2986337_scBS-MPN3-1.Cmet.CpG",
#     "GSM2986338_scBS-MPN3-2.Cmet.CpG",
#     "GSM2986339_scBS-MPN4-1.Cmet.CpG",
#     "GSM2986341_scBS-MPN7-1.Cmet.CpG",
#     "GSM2986342_scBS-MPN7-2.Cmet.CpG",
#     "GSM2986331_scBS-C-PN1-1.Cmet.CpG",
#     "GSM2986332_scBS-C-PN1-2.Cmet.CpG",
#     "GSM2986333_scBS-C-PN5-1.Cmet.CpG",
#     "GSM2986334_scBS-C-PN5-2.Cmet.CpG",
#     "GSM2986335_scBS-D-PN2-1.Cmet.CpG",
#     "GSM2986336_scBS-D-PN2-2.Cmet.CpG",
#     "GSM2481554_scBS-D-PN7-1.Cmet.CpG",
#     "GSM2481555_scBS-D-PN7-2.Cmet.CpG",
#     "GSM2481562_scBS-E-PN1-1.Cmet.CpG",
#     "GSM2481563_scBS-E-PN1-2.Cmet.CpG",
#     "GSM2481558_scBS-E-PN11-1.Cmet.CpG",
#     "GSM2481559_scBS-E-PN11-2.Cmet.CpG",
#     "GSM2481560_scBS-E-PN12-1.Cmet.CpG",
#     "GSM2481561_scBS-E-PN12-2.Cmet.CpG",
#     "GSM2481564_scBS-E-PN8-1.Cmet.CpG",
#     "GSM2481565_scBS-E-PN8-2.Cmet.CpG",
#     "GSM2481566_scBS-E-PN9-1.Cmet.CpG",
#     "GSM2481567_scBS-E-PN9-2.Cmet.CpG"]:
    
# for f in [
#     "GSM2481644_scBS-Morula-1-1.Cmet.CpG",
#     "GSM2481645_scBS-Morula-1-2.Cmet.CpG",
#     "GSM2481646_scBS-Morula-1-9.Cmet.CpG",
#     "GSM2481647_scBS-Morula-3-3.Cmet.CpG",
#     "GSM2481648_scBS-Morula-3-4.Cmet.CpG",
#     "GSM2481649_scBS-Morula-3-5.Cmet.CpG",
#     "GSM2773514_Mor06-Q-s113.single5mC.CpG",
#     "GSM2773515_Mor06-Q-s114.single5mC.CpG",
#     "GSM2773516_Mor06-Q-s115.single5mC.CpG",
#     "GSM2773517_Mor06-Q-s116.single5mC.CpG",
#     "GSM2773518_Mor06-Q-s117.single5mC.CpG",
#     "GSM2773519_Mor06-Q-s118.single5mC.CpG",
#     "GSM2773520_Mor06-Q-s119.single5mC.CpG",
#     "GSM2773521_Mor06-Q-s120.single5mC.CpG",
#     "GSM2773522_Mor06-Q-s121.single5mC.CpG",
#     "GSM2773523_Mor06-Q-s122.single5mC.CpG",
#     "GSM2773524_Mor06-Q-s123.single5mC.CpG",
#     "GSM2773525_Mor06-Q-s124.single5mC.CpG",
#     "GSM2773526_Mor06-Q-s125.single5mC.CpG",
#     "GSM2773527_Mor06-Q-s126.single5mC.CpG",
#     "GSM2773528_Mor06-Q-s127.single5mC.CpG",
#     "GSM2773529_Mor06-Q-s128.single5mC.CpG",
#     "GSM2773530_Mor06-Q-s129.single5mC.CpG",
#     "GSM2773531_Mor06-Q-s130.single5mC.CpG"]:
    
for f in [
    "GSM2986306_scBS-B-GV1.Cmet.CpG",
    "GSM2481553_scBS-D-GV-2.Cmet.CpG",
    "GSM2481568_scBS-F-GV1.Cmet.CpG",
    "GSM2481569_scBS-F-GV2.Cmet.CpG",
    "GSM2481583_scBS-K-GV-2.Cmet.CpG",
    "GSM2481584_scBS-K-GV-3.Cmet.CpG",
    "GSM2146951_scBS-A-MII-1.Cmet.CpG",
    "GSM2146952_scBS-A-MII-2.Cmet.CpG",
    "GSM2146953_scBS-A-MII-3.Cmet.CpG",
    "GSM2146954_scBS-A-MII-4.Cmet.CpG",
    "GSM2986308_scBS-D-MII-1.Cmet.CpG",
    "GSM2986310_scBS-D-MII-3.Cmet.CpG",
    "GSM2986311_scBS-D-MII-4.Cmet.CpG",
    "GSM2986312_scBS-D-MII-5.Cmet.CpG",
    "GSM2986313_scBS-D-MII-6.Cmet.CpG",
    "GSM2986314_scBS-D-MII-7.Cmet.CpG",
    "GSM2986316_scBS-D-MII-9.Cmet.CpG",
    "GSM2986317_scBS-E-MII-10.Cmet.CpG",
    "GSM2481556_scBS-E-MII-19.Cmet.CpG",
    "GSM2481557_scBS-E-MII-20.Cmet.CpG",
    "GSM2986319_scBS-E-MII-3.Cmet.CpG",
    "GSM2986320_scBS-G-MII-10.Cmet.CpG",
    "GSM2986321_scBS-G-MII-11.Cmet.CpG",
    "GSM2986322_scBS-G-MII-12.Cmet.CpG",
    "GSM2481570_scBS-G-MII-13.Cmet.CpG",
    "GSM2481581_scBS-J-MII-5.Cmet.CpG",
    "GSM2481586_scBS-K-MII-1.Cmet.CpG",
    "GSM2481587_scBS-K-MII-2.Cmet.CpG",
    "GSM2481588_scBS-K-MII-3.Cmet.CpG",
    "GSM2986323_scBS-L-MII-1.Cmet.CpG",
    "GSM2986324_scBS-L-MII-2.Cmet.CpG",
    "GSM2986325_scBS-L-MII-3.Cmet.CpG",
    "GSM2986326_scBS-L-MII-4.Cmet.CpG",
    "GSM2481589_scBS-M-MII-1.Cmet.CpG",
    "GSM2481591_scBS-M-MII-3.Cmet.CpG"]:


    ht = hl.import_table("{0}/{1}.bed".format(root,f),
                         delimiter='\t', min_partitions=1000,
                         types = {'chrom': hl.tstr,
                                  'start': hl.tint32,
                                  'end': hl.tint32,
                                  'strand': hl.tstr,
                                  'ttl': hl.tint32,
                                  'met': hl.tint32,
                                  'perc': hl.tfloat64,
                                 })




    ht = ht.annotate(pos = hl.cond(ht.strand=="+", ht.end, ht.start))

    grouping = hl.struct(chrom=ht.chrom, pos=ht.pos)

    ht_comb = ht.group_by(**grouping).aggregate(
        ttl=hl.agg.sum(ht.ttl), 
        met=hl.agg.sum(ht.met))

    ht_comb = ht_comb.annotate(methy_level = ht_comb.met/ht_comb.ttl)

    ht_comb.export("{0}/{1}.combined_strand.txt".format(root,f))


    