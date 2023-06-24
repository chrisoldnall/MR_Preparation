# MR Preparation
This is a repository that houses all the scripts within the pipeline to prepare data for Mendelian randomisation methods at an individual level. As such there are a mix of bash and python scripts included. These should be viewed and ran in the following order (note: where a number has an 'a' or 'b' this is because there are two parts of the pipeline which can be run simultaeneously.)

- 1 - SNP_Exposure_Lists.py
- 2a - GenotypeFilterForMerge.sh
- 2b - LDRemoval.sh
- 3a - ChromMerger.sh
- 3b - SNPIDReader.py
- 4 - Genotype.sh
- 5a - IVWriter.py
- 5b - OutcomeFilter.py
- 5c - ExposureFilter.py

As there is a fair few intracacies to these scripts, this user guide has been created. It is the intention that this will become a fully shelled pipeline soon.

## 1. SNP_Exposure_Lists.py [Run using Python]
Firstly run this script. It utilises whichever GWAS file you have to extract the exposures and SNPs in the system. This will create, within the same folder, a list of all of the SNPs which are relevant to the system into a file 'AllSigSNPList.txt' as well as a list of all the exposures in 'ExposureIDList.txt'. After these two files it will then create per exposure a list of the SNPs which are associated with it by the GWAS file in the folder in the format 'exposure1.tsv.'

## 2a. GenotypeFilterForMerge.sh [Run using Terminal]
Next we have a bash script which will take the BGEN and SAMPLE files from the cohort which we have (these contain the full genomic data for the individuals in our sample and their IDs) and reduce them per chromosome using the full list of SNPs that are relevant to the system in which we are working (determined by the 'AllSigSNPList.txt' file from 1.) - If you do not have the BGEN files per chromosome this will need some amending, otherwise the command below assumes all 22 chromosomes are being used. In this script you need to amend locations manually. 

Run in the terminal via: 'qsub GenotypeFilterForMerge.sh -t 1-22'
