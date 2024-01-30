#!/bin/sh


# https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63818

# 1. combine +/- strand
# 2. ave over samples
# 3. liftover


FILE_PREFIX="GSE63818_PGC_19W_embryo2_M_methylation_calling"
wget ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE63nnn/GSE63818/suppl/$FILE_PREFIX.bed.gz

zcat $FILE_PREFIX.bed.gz | awk 'BEGIN {FS= "\t"; OFS= "\t"}; ($10 == "CpG") {print $1,$2-1,$2,$4, $5,$6,$8}' > $FILE_PREFIX.CpG.1.bed

rm $FILE_PREFIX.bed.gz

bedSort $FILE_PREFIX.CpG.1.bed $FILE_PREFIX.CpG.2.bed

echo "chrom	start	end	strand	ttl	met	perc" > $FILE_PREFIX.CpG.bed

cat $FILE_PREFIX.CpG.2.bed >> $FILE_PREFIX.CpG.bed

rm $FILE_PREFIX.CpG.1.bed
rm $FILE_PREFIX.CpG.2.bed




FILE_PREFIX="GSE49828_WGBS_ICM_methylation_calling"

zcat $FILE_PREFIX.bed.txt.gz | awk 'BEGIN {FS= "\t"; OFS= "\t"}; ($10 == "CpG") {print $1,$2-1,$2,$4, $5,$6,$8}' > $FILE_PREFIX.CpG.1.bed

rm $FILE_PREFIX.bed.gz

bedSort $FILE_PREFIX.CpG.1.bed $FILE_PREFIX.CpG.2.bed

echo "chrom	start	end	strand	ttl	met	perc" > $FILE_PREFIX.CpG.bed

cat $FILE_PREFIX.CpG.2.bed >> $FILE_PREFIX.CpG.bed

rm $FILE_PREFIX.CpG.1.bed
rm $FILE_PREFIX.CpG.2.bed