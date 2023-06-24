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

