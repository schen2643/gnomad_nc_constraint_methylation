#!/bin/sh

# ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE81nnn/GSE81233/matrix/


for FILE_PREFIX in  GSM2146951_scBS-A-MII-1.Cmet GSM2146952_scBS-A-MII-2.Cmet GSM2146953_scBS-A-MII-3.Cmet GSM2146954_scBS-A-MII-4.Cmet GSM2986308_scBS-D-MII-1.Cmet GSM2986310_scBS-D-MII-3.Cmet GSM2986311_scBS-D-MII-4.Cmet GSM2986312_scBS-D-MII-5.Cmet GSM2986313_scBS-D-MII-6.Cmet GSM2986314_scBS-D-MII-7.Cmet GSM2986316_scBS-D-MII-9.Cmet GSM2986317_scBS-E-MII-10.Cmet GSM2481556_scBS-E-MII-19.Cmet GSM2481557_scBS-E-MII-20.Cmet GSM2986319_scBS-E-MII-3.Cmet GSM2986320_scBS-G-MII-10.Cmet GSM2986321_scBS-G-MII-11.Cmet GSM2986322_scBS-G-MII-12.Cmet GSM2481570_scBS-G-MII-13.Cmet GSM2481581_scBS-J-MII-5.Cmet GSM2481586_scBS-K-MII-1.Cmet GSM2481587_scBS-K-MII-2.Cmet GSM2481588_scBS-K-MII-3.Cmet GSM2986323_scBS-L-MII-1.Cmet GSM2986324_scBS-L-MII-2.Cmet GSM2986325_scBS-L-MII-3.Cmet GSM2986326_scBS-L-MII-4.Cmet GSM2481589_scBS-M-MII-1.Cmet GSM2481591_scBS-M-MII-3.Cmet

do

    zcat $FILE_PREFIX.bed.gz | awk 'BEGIN {FS= "\t"; OFS= "\t"}; ($10 == "CpG") {print $1,$2-1,$2,$4, $5,$6,$8}' > $FILE_PREFIX.CpG.1.bed

    rm $FILE_PREFIX.bed.gz

    bedSort $FILE_PREFIX.CpG.1.bed $FILE_PREFIX.CpG.2.bed

    echo "chrom	start	end	strand	ttl	met	perc" > $FILE_PREFIX.CpG.bed

    cat $FILE_PREFIX.CpG.2.bed >> $FILE_PREFIX.CpG.bed

    rm $FILE_PREFIX.CpG.1.bed
    rm $FILE_PREFIX.CpG.2.bed

done



# re-do for .txt.gz

for FILE_PREFIX in  GSM2773514_Mor06-Q-s113.single5mC GSM2773515_Mor06-Q-s114.single5mC GSM2773516_Mor06-Q-s115.single5mC GSM2773517_Mor06-Q-s116.single5mC GSM2773518_Mor06-Q-s117.single5mC GSM2773519_Mor06-Q-s118.single5mC GSM2773520_Mor06-Q-s119.single5mC GSM2773521_Mor06-Q-s120.single5mC GSM2773522_Mor06-Q-s121.single5mC GSM2773523_Mor06-Q-s122.single5mC GSM2773524_Mor06-Q-s123.single5mC GSM2773525_Mor06-Q-s124.single5mC GSM2773526_Mor06-Q-s125.single5mC GSM2773527_Mor06-Q-s126.single5mC GSM2773528_Mor06-Q-s127.single5mC GSM2773529_Mor06-Q-s128.single5mC GSM2773530_Mor06-Q-s129.single5mC GSM2773531_Mor06-Q-s130.single5mC

do

    zcat $FILE_PREFIX.txt.gz | awk 'BEGIN {FS= "\t"; OFS= "\t"}; ($10 == "CpG") {print $1,$2-1,$2,$4, $5,$6,$8}' > $FILE_PREFIX.CpG.1.bed

    rm $FILE_PREFIX.txt.gz

    bedSort $FILE_PREFIX.CpG.1.bed $FILE_PREFIX.CpG.2.bed

    echo "chrom	start	end	strand	ttl	met	perc" > $FILE_PREFIX.CpG.bed

    cat $FILE_PREFIX.CpG.2.bed >> $FILE_PREFIX.CpG.bed

    rm $FILE_PREFIX.CpG.1.bed
    rm $FILE_PREFIX.CpG.2.bed

done


