# 0: Import relevant packages.
import pandas as pd

# 1: SIGNIFICANT SNP AND EXPOSURE LIST CREATION FUNCTION
# Inputs:
# 1. GWAS_Dataframe_Pathway - Pathway for file which has the list of prior associated hits at a pre-determined level, associated via some GWAS. Define with "" and assumed to be a tsv.
# 2. Exposure_Identifier - The label for the column which identifies the exposure in the hits file, define with "".
# 3. Export_Pathway - Pathway for where you want the list of SNPs to go, define with "".
def SNP_Exposure_Lists(GWAS_Dataframe_Pathway, Exposure_Identifier, Export_Pathway):
    subsets = [] 
    df_hits = pd.read_csv(GWAS_Dataframe_Pathway, sep='\t')
    exposureIDarray = df_hits[Exposure_Identifier].unique()
    exposureIDList = pd.DataFrame(data = exposureIDarray)
    exposureIDList.to_csv(Export_Pathway+"/ExposureIDList.txt", sep='\t', index=False)
    for i in exposureIDarray:
        subsets.append(df_hits[df_hits[Exposure_Identifier]==i])    
    bigFramechr = []
    bigFramepos = []
    counter = 0
    for frame in subsets:
        needColumns = frame[['chr', 'pos', 'Score.pval']]
        bigFramechr.extend(needColumns['chr'].tolist())
        bigFramepos.extend(needColumns['pos'].tolist())
        output = pd.DataFrame(data = needColumns)
        output = output.rename(columns={'chr':'chr', 'pos':'pos', 'Score.pval':'P'})
        chromosomes = needColumns['chr'].tolist()
        positions = needColumns['pos'].tolist()
        colonsperexposure = [':']*len(chromosomes)
        chrsperexposure = ['chr']*len(chromosomes)
        values = [a + str(b) + c + str(d) for a, b, c, d in zip(chrsperexposure, chromosomes, colonsperexposure, positions)]
        output['SNP'] = values
        output = output[['SNP', 'P']]
        output.to_csv(Export_Pathway+"/"+str(exposureIDarray[counter])+".tsv", sep='\t', index=False)
        counter += 1
    colons = [':']*len(bigFramechr)
    values = [str(a) + b + str(c) for a, b, c in zip(bigFramechr, colons, bigFramepos)]
    output = pd.DataFrame(data = values)
    outputnorepeats = output.drop_duplicates()
    outputnorepeats.to_csv(Export_Pathway+"/AllSigSNPList.txt", sep="\t", index=False, header=False)