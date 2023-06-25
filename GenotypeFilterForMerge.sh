#$ -o INSERT OUPUT LOG LOCATION
#$ -e INSERT ERROR LOG LOCATION
#$ -N INSERT NAME OF JOB
#!/bin/sh
# Set: Current Working Directory.
#$ -cwd
# Set: Runtime.
#$ -l h_rt=47:00:00
# Set: Cores Requested.
#$ -pe sharedmem 3
# Set: Memory Needed.
#$ -l h_vmem=10G
# Set: Value of return will be last non-zero exit status.
set -o pipefail
# Initialise: Environment Modules
. /etc/profile.d/modules.sh
# Load: Modules and Environments
module load igmm/apps/qctool/2.0.8

CHR=${SGE_TASK_ID}
BGEN_FILE="BGEN FILE PATHWAY"
SAMPLE_FILE="SAMPLE FILE PATHWAY, REPLACE CHROMOSOME NUMBER BY ${CHR}"
RSID_LIST="AllSigSNPList.txt CREATED BY SNP_Exposure_Lists.py"
qctool -g ${BGEN_FILE} -assume-chromosome ${CHR} -og "EXPORTPATHWAY/filtered${CHR}.bgen" -incl-positions ${RSID_LIST}