import pandas as pd
import os
import re

def get_numbers_from_filename(filename):
    return re.search(r'\d+', filename).group(0)

directory = os.fsencode("INSERT PATHWAY OF .clumped FILES")
os.chdir("INSERT PATHWAY OF .clumped FILES")
LineCountHold = []

countingList = []
for file in os.listdir(directory):
    try:
        filename = os.fsdecode(file)
        filename = str(filename)
        ExposureNumber = get_numbers_from_filename(filename)
        df_Clumped = pd.read_csv(filename, sep='\s+', header=0)
        count = len(df_Clumped)
        df_Clumped_SNPs = df_Clumped['SNP']
        SNP_values = []
        for i in df_Clumped_SNPs:
            chr, pos = i.split(':')
            chr = get_numbers_from_filename(chr)
            pos = get_numbers_from_filename(pos)
            SNP_values.append(str(chr)+":"+str(pos))
        df_ChrPos = pd.DataFrame(SNP_values, columns=['pos']) 
        df_ChrPos.to_csv("SNPListByValid PATHWAY/"+str(count)+"SNP/Exposure"+str(ExposureNumber)+".txt", sep=' ', index=None, header=False)
        countingList.append([ExposureNumber, count])
    except:
        print("Error with exposure "+str(ExposureNumber))

countingFrame = pd.DataFrame(data=countingList, columns=['Exposure', 'SNPCount'])
SNPList = countingFrame.SNPCount.unique().tolist()
for SNPChoice in SNPList:
    df_Select = countingFrame[countingFrame['SNPCount']==SNPChoice]
    df_Exp_Txt = ['Exposure']*len(df_Select)
    df_Select_Red = df_Exp_Txt + df_Select['Exposure']
    df_Select_Red.to_csv("INSERT PATHWAY TO SNPListByValid/"+str(SNPChoice)+"SNP/"+str(SNPChoice)+"SNPList.txt", sep=' ', index=None, header=False)

