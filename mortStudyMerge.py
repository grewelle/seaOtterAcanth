import scipy
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import csv


def impData(filename):
    abs_file_path = filename
    with open(abs_file_path, newline='', encoding="utf8") as csvfile:
        totalData = list(csv.reader(csvfile))
    return totalData



def main():
    file1 = "C:/Users/Richard/Desktop/AcanthData/fullStrandingData.csv"  # import data file
    file2 = "C:/Users/Richard/Desktop/AcanthData/mortStudy.csv"
    dataBig = impData(file1)
    dataSmall = impData(file2)

    soNo1 = list(np.array(dataBig)[1:, 0])


    soNo2 = list(np.array(dataSmall)[1:, 0])
    mort = list(np.array(dataSmall)[1:, 1:])

    #filteredData = []
    count = 0

    for i in range(len(soNo1)):
        if soNo1[i] in soNo2:
            spot = soNo2.index(soNo1[i])
            print(*mort[spot], sep='\t')
            count +=1

        else:
            print('')


    #filteredData = [soNo1, acanth1, intes1, abdom1]






main()