import os

temp=0
path="PATHWAY OF .clumped FILES (no /)"
for r,d,f in os.walk(path):
    for files in f:
        i=0
        try:
            o=open( os.path.join(r,files) )        
        except Exception:pass            
        else:
            for lines in o: i=i+1 #count lines
            o.close()
            if i>=temp: temp=i; final = os.path.join(r,files)

max_SNPs = temp-3

causalFrameworkPathway = "PATHWAY FOR CAUSAL FRAMEWORK TO BE STORED"
SNPDenotion = "Z"
ExpsoureDenotion = "A"
OutcomeDenotion = "Y"
causalPathway = os.path.join(causalFrameworkPathway, SNPDenotion)
os.mkdir(causalPathway)
exposurePathway = os.path.join(causalFrameworkPathway, ExpsoureDenotion)
os.mkdir(exposurePathway)
outcomePathway = os.path.join(causalFrameworkPathway, OutcomeDenotion)
os.mkdir(outcomePathway)

iv_filesPathway = "PATHWAY FOR GENOTYPED BED/BIM/FAM FILES TO BE STORED"
SNPListByValidPathway = "PATHWAY FOR STORAGE OF SNP LISTS PER EXPOSIRE"

for i in range(1, max_SNPs+1):
    directory = str(i) + "SNP"
    path1 = os.path.join(causalPathway, directory)
    path2 = os.path.join(iv_filesPathway, directory)
    path3 = os.path.join(SNPListByValidPathway, directory)
    os.mkdir(path1)
    os.mkdir(path2)
    os.mkdir(path3)

SNPList = [
    str(i) + "SNP"
    for i in range(1, max_SNPs+1)
]

with open(r"PATHWAY FOR LIST OF SNP FOLDERS", 'w') as fp:
    for item in SNPList:
        fp.write("%s\n" % item)