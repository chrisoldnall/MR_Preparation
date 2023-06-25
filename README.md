# MR Preparation
This is a repository that houses all the scripts within the pipeline to prepare data for Mendelian randomisation methods at an individual level. As such there are a mix of bash and python scripts included. These should be viewed and ran in the following order (note: where a number has an 'a' or 'b' this is because there are two parts of the pipeline which can be run simultaeneously.)

- 1 - SNP_Exposure_Lists.py
- 2a - GenotypeFilterForMerge.sh
- 2b - LDClumping.sh

- Interlude (i)

  Before proceeding there is some manual work which is required to move only the .clumped files in to their own folder. We additionally need to create a folder set up based on how many SNPs we have per exposure as to save the genotyping information next.

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

Run in the terminal via: ``` qsub GenotypeFilterForMerge.sh -t 1-22 ```

## 2b. LDClumping.sh [Run using Terminal]
In parallel with 2a, we may also run the LD clumping procedure for each of the exposures. This script takes in the individual SNP per exposure files that were created in 1. and forms LD clump blocks in order to ensure what SNPs we retain for the MR process are not in LD with each other. There will be a range of files returned, most importantly the '.clumped' files.
- WARNING: This script requires the cohort files to be in BED/BIM/FAM format. If you only have BGEN files then you will need to convert to BED/BIM/FAM. There is a variety of scripts/advices to do so online. It is hope to add in a script here in future.

Run in the terminal via: ``` qsub LDClumping.sh ```

## Interlude (i)
Following running script 2b, it is necessary to move the .clumped files in to their own folder for later usage. This can be done with the following commands.
```
find "OUTPUT_LOCATION_OF_2B" -name "*.clumped" -exec cp -vuni '{}' "OUTPUT_LOCATION_FOR_CLUMPED_FILED" ";"
```
After this we need to create the folders to save the genotyping information in, in a couple of steps. Therefore we search through all the '.clumped' files and work out the maximum number of candidate SNPs we have. 
```
find /exports/igmm/eddie/GenScot-PBMC-proteomics-GWAS/coldnall/testFolder -type f -print0 | xargs -0 wc -l | sort -n
```

## 3a. ChromMerger.sh [Run using Terminal]
Next we merge the BGEN files that came from the script in 2a. This is because we have filtered each individual chromosome to only now contain the genotyping information for the SNPs that we know are associated with the system that we are working in. For this we have to merge each of the chromosomes. It starts with doing chr 1 and 2 individually, then loops around the rest of the chromosomes. Eventually in the folder you will have a file 'merged1_22.bgen.'

Run in the terminal via: ``` qsub ChromMerger.sh ```
