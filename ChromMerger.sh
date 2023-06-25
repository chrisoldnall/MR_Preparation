#$ -o INSERT OUTCOME LOG PATHWAY
#$ -e INSERT ERROR LOG PATHWAY
#$ -N INSERT NAME OF THE JOB
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

INITIAL_CHR_BEGN="INSERT FIRST CHR BGEN FILE PATHWAY"
INITIAL_CHR_SAMPLE="INSERT FIRST CHR SAMPLE FILE PATHWAY"
SECOND_CHR_BGEN="INSERT SECOND CHR BGEN FILE PATHWAY"
SECOND_CHR_SAMPLE="INSERT SECOND CHR SAMPLE FILE PATHWAY"
qctool -g ${INITIAL_CHR_BEGN} -s ${INITIAL_CHR_SAMPLE} -merge-in ${SECOND_CHR_BGEN} ${SECOND_CHR_SAMPLE} -og "INSERT PATHWAY FOR MERGED FILES/merged1_2.bgen"

for chr in {2..21}
do
    chr1=${chr}
    chr2=$((chr + 1))
    BGEN_FILE1="INSERT PATHWAY FOR MERGED FILES/merged1_${chr1}.bgen"
    SAMPLE_FILE1="SAMPLE FILE PATHWAY, REPLACE CHROMOSOME NUMBER BY ${chr1}"
    BGEN_FILE2="INSERT FIRST CHR BGEN FILE PATHWAY REPLACE CHR NUMBER BY ${chr1}"
    SAMPLE_FILE2="SAMPLE FILE PATHWAY, REPLACE CHROMOSOME NUMBER BY ${chr2}"
    qctool -g ${BGEN_FILE1} -s ${SAMPLE_FILE1} -merge-in ${BGEN_FILE2} ${SAMPLE_FILE2} -og "INSERT PATHWAY FOR MERGED FILES/merged1_${chr2}.bgen"
done