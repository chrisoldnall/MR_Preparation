#$ -o INSERT OUTCOME LOG PATHWAY
#$ -e INSERT ERROR LOG PATHWAY
#!/bin/sh
# Set: Current Working Directory.
#$ -cwd
# Set: Runtime.
#$ -l h_rt=49:00:00
# Set: Cores Requested.
#$ -pe sharedmem 4
# Set: Memory Needed.
#$ -l h_vmem=10G
# Set: Value of return will be last non-zero exit status.
set -o pipefail
# Initialise: Environment Modules
. /etc/profile.d/modules.sh
# Load: Modules and Environments
module load igmm/apps/plink/1.90b4

for EXP in $(cat INSERTPATHWAYOF/ExposureIDList.txt);
do
    BED_FILE="INSERT COHORT BED/BIM/FAM LOCATION - DO NOT SPECIFY THE FILE EXTENSION IT WILL AUTO PICKUP ALL 3"
    RSID_LIST="INSERT PATHWAY OF SNPS PER EXPOSURE FILE/$EXP.tsv"
    plink --bfile ${BED_FILE} --clump ${RSID_LIST} --clump-r2 0.05 --clump-kb 2000 --out "INSERT OUTCOME PATHWAY/Uncorrelated$PRO"
done

