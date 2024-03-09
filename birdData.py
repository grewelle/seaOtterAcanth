import scipy
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import csv

def impData(filename):
    abs_file_path = filename
    with open(abs_file_path, newline='', encoding='utf-8') as csvfile:
        totalData = list(csv.reader(csvfile))
    return totalData



def avgSeason(file5):
    allData = impData(file5)
    tempList = []
    #tempList2 = []
    week = 1
    for i in range(1,len(allData)):
        if week == int(allData[i][8]):
            try:
                tempList.append(float(allData[i][9]))
                #tempList2.append(float(allData[i][1]))
            except:
                week = week
        else:
            #print(week, np.average(tempList), np.average(tempList2))
            print(week, round(np.average(tempList),3), round(np.sqrt(np.var(tempList)/len(tempList)),3))
            tempList = [float(allData[i][9])]
            #tempList2 = [float(allData[i][1])]
        week = int(allData[i][8])
    return

def filterData(file2,file3):
    data = impData(file2)
    newFile = []
    for i in range(1,len(data)):
        if data[i][10] != 'X' and 34 < float(data[i][28]) < 38 and data[i][37] != '' and data[i][40] != '':
            newFile.append([data[i][0], data[i][10], data[i][28], data[i][29], data[i][30], data[i][37], data[i][40]])

    with open(file3, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for row in newFile:
            writer.writerow(row)
    return

def main():
    file = "C:/Users/Richard/Desktop/AcanthData/greaterScaup_full.csv"  # import data file
    file2 = "C:/Users/Richard/Desktop/AcanthData/greaterScaup_raw.csv"





    #filterData(file2,file)
    avgSeason(file)




main()