import scipy
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import csv


def impData(filename):
    abs_file_path = filename
    with open(abs_file_path, newline='') as csvfile:
        totalData = list(csv.reader(csvfile))
    return totalData



def main():
    file1 = "C:/Users/Richard/Desktop/AcanthData/fullStrandingData.csv"  # import data file
    file2 = "C:/Users/Richard/Desktop/AcanthData/fixedAcanthData.csv"
    dataBig = impData(file1)
    dataSmall = impData(file2)

    soNo1 = list(np.array(dataBig)[1:, 0])
    acanth1 = list(np.array(dataBig)[1:, 59])
    intes1 = list(np.array(dataBig)[1:, 60])
    abdom1 = list(np.array(dataBig)[1:, 61])

    soNo2 = list(np.array(dataSmall)[:, 0])
    acanth2 = list(np.array(dataSmall)[:, 1])
    intes2 = list(np.array(dataSmall)[:, 2])
    abdom2 = list(np.array(dataSmall)[:, 3])

    for i in range(len(soNo1)):
        if soNo1[i] in soNo2:

            spot = soNo2.index(soNo1[i])
            print(soNo1[i], intes1[i], intes2[spot])
            acanth1[i] = acanth2[spot]
            intes1[i] = intes2[spot]
            abdom1[i] = abdom2[spot]


    filteredData = [soNo1, acanth1, intes1, abdom1]


    myFile = open('/Users/Richard/Desktop/AcanthData/acanth_data_filtered.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(filteredData)


main()