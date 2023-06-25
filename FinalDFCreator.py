import pandas as pd
import re

SNPDF = pd.read_csv("INSERT PATHWAY TO SNPList.txt", sep='\t', header=None, names=['SNPList'])
SNPList = SNPDF["SNPList"].tolist()
for SNP in SNPList:
    EXP = pd.read_csv("INSERT PATHWAY TO SNPListByValid/"+str(SNP)+"/"+str(SNP)+"List.txt", sep='\t', header=None, names=['EXPList'])
    EXPList = EXP["EXPList"].tolist()
    for EXP in EXPList:
        df1 = pd.read_csv("INSERT PATHWAY TO causalFramework/A/"+EXP+".INSERTFILEEXTENSION")
        df2 = pd.read_csv("INSERT PATHWAY TO causalFramework/Y/INSERT OUTCOME NAME.INSERTFILEEXTENSION")
        df3 = pd.read_csv("INSERT PATHWAY TO causalFramework/Z/"+str(SNP)+"/"+str(EXP)+".csv")
        SNPNoList = list(range(0, len(df3.T)-1))
        SNPNoList = [str(x) for x in SNPNoList]
        SNPTitles = ["Z" + SNPNo for SNPNo in SNPNoList]
        df1_red = df1[[EXP, 'id']]
        df1_red.columns = [EXP, 'id']
        IDTag = ['id']
        Listfordf3Columns = IDTag + SNPTitles
        df3.columns = Listfordf3Columns
        df1_red["id"] = df1_red["id"].astype(str)
        df2["id"] = df2["id"].astype(str)
        df3["id"] = df3["id"].astype(str)
        df4 = pd.merge(df1_red, df2, on='id')
        df4 = pd.merge(df4, df3, on='id')
        df4 = df4.set_index('id')
        df4 = df4.reset_index()
        DF4Columns = [EXP, 'INSERT OUTCOME NAME']
        Listfordf4Columns = DF4Columns + SNPTitles
        df4 = df4[Listfordf4Columns]
        DF4ColumnsAgain = ['A', 'Y']
        Listfordf4ColumnsAgain = DF4ColumnsAgain + SNPTitles
        df4.columns = Listfordf4ColumnsAgain
        df5 = df4.dropna()
        df5.to_csv("INSERT PATHWAY TO causalFramework/INSERT NAME OF OUTCOME/"+str(SNP)+"/"+str(EXP)+".csv", index=False)