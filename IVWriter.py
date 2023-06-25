import pandas as pd
from pandas_plink import read_plink
from pandas_plink import get_data_folder
from os.path import join

SNPDF = pd.read_csv("INSERT PATHWAY FOR SNPList.txt", sep='\t', header=None, names=['SNPList'])
SNPList = SNPDF["SNPList"].tolist()
for i in SNPList:
    EXP = pd.read_csv("INSERT PATHWAY TO SNPListByValid/"+str(i)+"/"+str(i)+"List.txt", sep='\t', header=None, names=['EXPList'])
    EXPList = EXP["EXPList"].tolist()
    for j in EXPList:
        (bim, fam, bed) = read_plink(join(get_data_folder(), "INSERT PATHWAY TO iv_files/"+str(i)+"/"+str(j)+".bed"), verbose=False)
        matrix = bed.compute()
        ids = fam['iid']
        df = pd.DataFrame(matrix.T)
        df.insert(loc=0, column='id', value=ids)        
        df.to_csv("INSERT PATHWAY TO causalFramework/Z/"+str(i)+"/"+str(j)+".csv", index=False)