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
    # tempList2 = []
    week = 1
    for i in range(1, len(allData)):
        if week == int(allData[i][10]):
            tempList.append(float(allData[i][9]))
            # tempList2.append(float(allData[i][1]))
        else:
            # print(week, np.average(tempList), np.average(tempList2))
            print(week, round(np.average(tempList), 3), round(np.sqrt(np.var(tempList) / len(tempList)), 3))
            tempList = [float(allData[i][9])]
            # tempList2 = [float(allData[i][1])]
        week = int(allData[i][10])
    return


def pupMonths(file):
    file = impData(file)
    pups = [0,0,0,0,0,0,0,0,0,0,0,0]
    other = [0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(1,len(file)):
        if file[i][15] > '600':
            if file[i][25] == '3' or file[i][25] == '13':
                pups[int(file[i][5])-1] += 1
            else:
                other[int(file[i][5])-1] += 1

    print(np.array(pups)/(np.array(pups)+np.array(other)))
    return

def pupSpring(file):
    data = impData(file)

    lastperiod = 1968
    pup = 0
    other = 0
    for i in range(1, len(data)):
        if 5.1 < float(data[i][5]) < 9.1:
            if int(data[i][6]) == lastperiod:
                if data[i][25] == '3' or data[i][25] == '13':
                    pup += 1
                else:
                    other += 1

            else:
                print(lastperiod, pup/(pup+other))
                pup = 0
                other = 0
                if data[i][25] == '3' or data[i][25] == '13':
                    pup += 1
                else:
                    other += 1

            lastperiod = int(data[i][6])

    return


def main():
    file = "C:/Users/Richard/Desktop/AcanthData/fullStrandingData.csv"  # import data file


    pupMonths(file)
    #pupSpring(file)


main()