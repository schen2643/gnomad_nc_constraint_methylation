#!/bin/sh


###
FILE_PREFIX="GSE63818_PGC_17W"
FILE_PREFIX_="GSE63818_PGC_17W_files"

{ xargs cat < $FILE_PREFIX_.txt ; } | sed /chrom/d | awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$2-1,$2,$3, $4,$5}' > $FILE_PREFIX.1.bed

bedSort $FILE_PREFIX.1.bed $FILE_PREFIX.2.bed

bedtools merge -i $FILE_PREFIX.2.bed -c 4,5,6 -o sum,sum,mean |  awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$2,$3,$4,$5,$6,$5/$4}' > $FILE_PREFIX.merged.mean2.bed

rm $FILE_PREFIX.1.bed
rm $FILE_PREFIX.2.bed


awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$3,$7}' $FILE_PREFIX.merged.mean2.bed > $FILE_PREFIX.merged.mean2.1.bed

awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$3+1,$7}' $FILE_PREFIX.merged.mean2.bed >> $FILE_PREFIX.merged.mean2.1.bed

bedSort $FILE_PREFIX.merged.mean2.1.bed $FILE_PREFIX.merged.mean2.2.bed

echo "locus methyl_level" > $FILE_PREFIX.merged.mean2.2hl.bed

awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1":"$2,$3}' $FILE_PREFIX.merged.mean2.2.bed | sed s/chr// >> $FILE_PREFIX.merged.mean2.2hl.bed

rm $FILE_PREFIX.merged.mean2.1.bed 
rm $FILE_PREFIX.merged.mean2.2.bed



###
FILE_PREFIX="GSE49828_WGBS_ICM"

sed /chrom/d GSE49828_WGBS_ICM_methylation_calling.CpG.combined_strand.txt | awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$2,$5}' > $FILE_PREFIX.merged.mean2.1.bed

sed /chrom/d GSE49828_WGBS_ICM_methylation_calling.CpG.combined_strand.txt | awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$2+1,$5}' >> $FILE_PREFIX.merged.mean2.1.bed

bedSort $FILE_PREFIX.merged.mean2.1.bed $FILE_PREFIX.merged.mean2.2.bed

echo "locus methyl_level" > $FILE_PREFIX.merged.mean2.2hl.bed

awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1":"$2,$3}' $FILE_PREFIX.merged.mean2.2.bed | sed s/chr// >> $FILE_PREFIX.merged.mean2.2hl.bed

rm $FILE_PREFIX.merged.mean2.1.bed 
rm $FILE_PREFIX.merged.mean2.2.bed



###
FILE_PREFIX="GSE81233_Oocyte"

cat Oocyte/* | sed /chrom/d | awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$2-1,$2,$3, $4,$5}' > $FILE_PREFIX.1.bed

bedSort $FILE_PREFIX.1.bed $FILE_PREFIX.2.bed

bedtools merge -i $FILE_PREFIX.2.bed -c 4,5,6 -o sum,sum,mean |  awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$2,$3,$4,$5,$6,$5/$4}' > $FILE_PREFIX.merged.mean2.bed

rm $FILE_PREFIX.1.bed
rm $FILE_PREFIX.2.bed


awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$3,$7}' $FILE_PREFIX.merged.mean2.bed > $FILE_PREFIX.merged.mean2.1.bed

awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1,$3+1,$7}' $FILE_PREFIX.merged.mean2.bed >> $FILE_PREFIX.merged.mean2.1.bed

bedSort $FILE_PREFIX.merged.mean2.1.bed $FILE_PREFIX.merged.mean2.2.bed

echo "locus methyl_level" > $FILE_PREFIX.merged.mean2.2hl.bed

awk 'BEGIN {FS= "\t"; OFS= "\t"}; {print $1":"$2,$3}' $FILE_PREFIX.merged.mean2.2.bed | sed s/chr// >> $FILE_PREFIX.merged.mean2.2hl.bed

rm $FILE_PREFIX.merged.mean2.1.bed 
rm $FILE_PREFIX.merged.mean2.2.bed



