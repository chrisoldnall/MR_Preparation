#$ -o INSERT OUTPUT LOG PATHWAY
#$ -e INSERT ERROR LOG PATHWAY
#!/bin/sh
# Set: Current Working Directory.
#$ -cwd
# Set: Runtime.
#$ -l h_rt=47:00:00
# Set: Cores Requested.
#$ -pe sharedmem 1
# Set: Memory Needed.
#$ -l h_vmem=10G
# Set: Value of return will be last non-zero exit status.
set -o pipefail
# Initialise: Environment Modules
. /etc/profile.d/modules.sh
# Load: Modules and Environments
module load igmm/apps/qctool/2.0.8

for SNP in $(cat INSERT PATHWAY OF SNPList FROM AS BY 3. SNPListCreator.py/SNPList.txt);
do
    for EXP in $(cat INSERT PATHWAY TO SNPListByValid/${SNP}/${SNP}List.txt);
    do
        BGEN_FILE="PATHWAY TO MERGED BGEN FILE FROM ChromMerger.sh/merged1_22.bgen"
        SAMPLE_FILE="SAMPLE FILE FROM COHORT (CAN BE ANY CHROMOSOME)"
        RSID_LIST="INSERT PATHWAY TO SNPListByValid/${SNP}/${EXP}.txt"
        qctool -g ${BGEN_FILE} -s ${SAMPLE_FILE} -og "INSERT PATHWAY TO iv_files/${SNP}/${EXP}.bed" -incl-positions ${RSID_LIST}
    done
done