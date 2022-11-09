import scipy
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns; sns.set(style="white", color_codes=True)
import csv

def impData(filename):
    abs_file_path = filename
    with open(abs_file_path, newline='') as csvfile:
        totalData = list(csv.reader(csvfile))
    return totalData


def findDupes(fullList):
    return set([x for x in fullList if fullList.count(x) > 1])

def findDupes2(fullList):
    for i in range(len(fullList)):
        fullList[i] = fullList[i].split('-')[0]
    return set([x for x in fullList if fullList.count(x) > 1])

def fixDates(soNo, date, month, year):
    soNoYear = []
    wrong = []
    for i in range(len(soNo)):
        flag = 0
        if '-' in soNo[i]:
            soNoYear.append(soNo[i].split('-')[1])
        else:
            soNoYear.append('NA')

        mn = date[i].split('-')[1]
        yr = date[i].split('-')[2]



        if soNoYear[i] != 'NA':
            if soNoYear[i] != yr:
                flag = 1
        if year[i][-2:] != yr:
            flag = 1
        if mn == 'Jan':
            mn = '1'
        elif mn == 'Feb':
            mn = '2'
        elif mn == 'Mar':
            mn = '3'
        elif mn == 'Apr':
            mn = '4'
        elif mn == 'May':
            mn = '5'
        elif mn == 'Jun':
            mn = '6'
        elif mn == 'Jul':
            mn = '7'
        elif mn == 'Aug':
            mn = '8'
        elif mn == 'Sep':
            mn = '9'
        elif mn == 'Oct':
            mn = '10'
        elif mn == 'Nov':
            mn = '11'
        else:
            mn = '12'

        if mn != month[i]:
            flag = 1

        if flag == 1:
            wrong.append(soNo[i])

        flag = 0



    return wrong

def fixArea(area, atos, soNo):
    wrong = []
    flag = 0
    for i in range(len(area)):
        try:
            int(atos[i])

        except ValueError:
            ar = area[i]
            flag = 1

        if flag == 0:

            if int(atos[i]) < 0:
                ar = 1
            elif 0 <= int(atos[i]) < 52:
                ar = 3
            elif 52 <= int(atos[i]) < 75:
                ar = 4
            elif 75 <= int(atos[i]) < 110:
                ar = 5
            elif 110 <= int(atos[i]) < 135:
                ar = 6
            elif 135 <= int(atos[i]) < 181:
                ar = 7
            elif 181 <= int(atos[i]) < 230:
                ar = 8
            elif 230 <= int(atos[i]) < 256:
                ar = 9
            elif 256 <= int(atos[i]) < 272:
                ar = 10
            elif 272 <= int(atos[i]) < 321:
                ar = 11
            elif 321 <= int(atos[i]) < 366:
                ar = 12
            elif 366 <= int(atos[i]) < 377:
                ar = 13
            elif 377 <= int(atos[i]) < 385:
                ar = 14
            elif 385 <= int(atos[i]) < 391:
                ar = 15
            elif 391 <= int(atos[i]) < 402:
                ar = 16
            elif 402 <= int(atos[i]) < 412:
                ar = 17
            elif 412 <= int(atos[i]) < 431:
                ar = 18
            elif 431 <= int(atos[i]) < 449:
                ar = 19
            elif 449 <= int(atos[i]) < 472:
                ar = 20
            elif 472 <= int(atos[i]) < 499:
                ar = 21
            elif 499 <= int(atos[i]) < 525:
                ar = 22
            elif 525 <= int(atos[i]) < 553:
                ar = 23
            elif 553 <= int(atos[i]) < 600:
                ar = 24
            elif 600 <= int(atos[i]) < 641:
                ar = 25
            elif 641 <= int(atos[i]) < 669:
                ar = 26
            elif 669 <= int(atos[i]) < 694:
                ar = 27
            elif 694 <= int(atos[i]) < 730:
                ar = 28
            elif 730 <= int(atos[i]) < 754:
                ar = 29
            elif 754 <= int(atos[i]) < 788:
                ar = 30
            elif 788 <= int(atos[i]) < 807:
                ar = 31
            elif 807 <= int(atos[i]) < 826:
                ar = 32
            elif 826 <= int(atos[i]) < 844:
                ar = 33
            elif 844 <= int(atos[i]) < 853:
                ar = 34
            elif 853 <= int(atos[i]) < 892:
                ar = 35
            elif 892 <= int(atos[i]) < 917:
                ar = 36
            elif 917 <= int(atos[i]) < 941:
                ar = 37
            elif 941 <= int(atos[i]) < 972:
                ar = 38
            elif 972 <= int(atos[i]) < 1013:
                ar = 39
            elif 1013 <= int(atos[i]) < 1060:
                ar = 40
            elif 1060 <= int(atos[i]) < 1112:
                ar = 41
            elif 1112 <= int(atos[i]) < 1162:
                ar = 42
            elif 1162 <= int(atos[i]) < 1234:
                ar = 43
            elif 1234 <= int(atos[i]) < 1271:
                ar = 44
            elif 1271 <= int(atos[i]) < 1319:
                ar = 45
            elif 1319 <= int(atos[i]) < 1367:
                ar = 46
            elif 1367 <= int(atos[i]) < 1400:
                ar = 47
            elif 1400 <= int(atos[i]) < 1435:
                ar = 48
            elif 1435 <= int(atos[i]) < 1461:
                ar = 49
            elif 1461 <= int(atos[i]):
                ar = 50
            else:
                ar = area[i]

        """if str(ar) != area[i]:
            if area[i] == '':
                print(soNo[i], ar)
            elif area[i] == '32/33':
                print('NA')
            else:
                wrong.append(soNo[i])
                print(ar-int(area[i]))"""
        flag = 0

    return wrong

def fixCond(cond, cond2, soNo):
    flag = 0
    wrong = []
    for i in range(len(cond)):
        if cond[i] == '2':
            if cond2[i] != 'FRESH':
                flag = 1
        elif cond[i] == '3':
            if cond2[i] != 'MOD DECOMP':
                flag = 1
        elif cond[i] == '4':
            if cond2[i] != 'ADV DECOMP':
                flag = 1
        elif cond[i] == '5':
            if cond2[i] != 'MUMM/SKEL/FRAG':
                flag = 1
        elif cond[i] == '9':
            if cond2[i] != 'UNKNOWN':
                flag = 1
        else:
            if cond2[i] != 'ALIVE':
                flag =1

        if flag == 1:
            wrong.append(soNo[i])

        flag = 0

    return wrong

def fixAge(age, age2, soNo):
    flag = 0
    wrong = []
    for i in range(len(age)):
        if age[i] == '2' or age[i] == '12':
            if age2[i] != 'PUP':
                flag = 1
        elif age[i] == '3' or age[i] == '13':
            if age2[i] != 'IMM':
                flag = 1
        elif age[i] == '4' or age[i] == '14':
            if age2[i] != 'SUBADULT':
                flag = 1
        elif age[i] == '5' or age[i] == '15':
            if age2[i] != 'ADULT':
                flag = 1
        elif age[i] == '6' or age[i] == '16':
            if age2[i] != 'AGED ADULT':
                flag = 1
        else:
            if age2[i] != 'UNKNOWN':
                flag =1

        if flag == 1:
            wrong.append(soNo[i])
        flag = 0

    return wrong

def fixLength(age, totalLength, soNo, sex, grizz, toothCond):
    flag = 0
    flag2 = 0
    wrong = []
    diff = []
    fAge = []
    fTotalLength = []
    fSex = []
    fGrizz = []
    fToothCond = []
    for i in range(len(age)):

        try:
            float(totalLength[i])

        except ValueError:
            flag2 = 1

        if flag2 == 0:

            if age[i] == '2' or age[i] == '12':
                if 40 <= float(totalLength[i]) <= 90 or '-' in totalLength[i]:
                    flag = 0
                else:
                    flag = 1
                    diff.append(min(abs(float(totalLength[i])-40), abs(float(totalLength[i])-90)))
            elif age[i] == '3' or age[i] == '13':
                if 80 <= float(totalLength[i]) <= 105 or '-' in totalLength[i]:
                    flag = 0
                else:
                    flag = 1
                    diff.append(min(abs(float(totalLength[i]) - 80), abs(float(totalLength[i]) - 105)))
            elif age[i] == '4' or age[i] == '14':
                if sex[i] == 'M':
                    if 100 <= float(totalLength[i]) <= 125 or '-' in totalLength[i]:
                        flag = 0
                    else:
                        flag = 1
                        diff.append(min(abs(float(totalLength[i]) - 100), abs(float(totalLength[i]) - 125)))
                elif sex[i] == 'F':
                    if 95 <= float(totalLength[i]) <= 115 or '-' in totalLength[i]:
                        flag = 0
                    else:
                        flag = 1
                        diff.append(min(abs(float(totalLength[i]) - 95), abs(float(totalLength[i]) - 115)))
                else:
                    if 95 <= float(totalLength[i]) <= 125 or '-' in totalLength[i]:
                        flag = 0
                    else:
                        flag = 1
                        diff.append(min(abs(float(totalLength[i]) - 95), abs(float(totalLength[i]) - 125)))
            elif age[i] == '5' or age[i] == '15' or age[i] == '6' or age[i] == '16':
                if sex[i] == 'M':
                    if 115 < float(totalLength[i]) or '-' in totalLength[i]:
                        flag = 0
                    else:
                        flag = 1
                        diff.append(abs(float(totalLength[i]) - 115))
                elif sex[i] == 'F':
                    if 105 < float(totalLength[i]) or '-' in totalLength[i]:
                        flag = 0
                    else:
                        flag = 1
                        diff.append(abs(float(totalLength[i]) - 105))
                else:
                    if 105 < float(totalLength[i]) or '-' in totalLength[i]:
                        flag = 0
                    else:
                        flag = 1
                        diff.append(abs(float(totalLength[i]) - 105))
            elif age[i] == '7' or age[i] == '17':
                if float(totalLength[i]) < 105 or '-' in totalLength[i]:
                    flag = 0
                else:
                    flag = 1
                    diff.append(abs(float(totalLength[i]) - 105))
            elif age[i] == '8' or age[i] == '18':
                if float(totalLength[i]) > 95 or '-' in totalLength[i]:
                    flag = 0
                else:
                    flag = 1
                    diff.append(abs(float(totalLength[i]) - 95))
            else:
                flag = 0

        if flag == 1:
            wrong.append(soNo[i])
            fAge.append(age[i])
            fTotalLength.append(totalLength[i])
            fSex.append(sex[i])
            fGrizz.append(grizz[i])
            fToothCond.append(toothCond[i])
        flag = 0
        flag2 = 0

    return wrong, diff, fAge, fTotalLength, fSex, fGrizz, fToothCond

def fixAcanth(acanth, intes, abdom):
    p_intest = []
    p_abdom = []
    coryn = []
    for i in range(len(acanth)):
        if acanth[i] == 'Y' or acanth[i] == 'y':
            if abdom[i] == '1' or abdom[i] == '2' or abdom[i] == '3':
                p_intest.append('3')
                p_abdom.append(abdom[i])
            else:
                p_intest.append('9')
                p_abdom.append('0')

            coryn.append('9')

        elif acanth[i] == 'N' or acanth[i] == 'n':
            p_intest.append('0')
            p_abdom.append('0')
            coryn.append('0')

        elif 'Y(CORY' in acanth[i]:
            p_intest.append('0')
            p_abdom.append('0')
            coryn.append(intes[i])

        elif 'Y(PROF' in acanth[i]:
            p_intest.append(intes[i])
            p_abdom.append(abdom[i])
            coryn.append('0')

        elif 'Y(CORY & PROF' in acanth[i] or 'Y(C & P)' in acanth[i]:
            p_intest.append(intes[i])
            p_abdom.append(abdom[i])
            coryn.append(intes[i])

        elif acanth[i] == 'P' or acanth[i] == 'p':
            p_intest.append(intes[i])
            p_abdom.append(abdom[i])
            coryn.append('0')

        elif acanth[i] == 'C' or acanth[i] == 'c':
            p_intest.append('0')
            p_abdom.append('0')
            coryn.append(intes[i])

        elif acanth[i] == 'PC' or acanth[i] == 'pc':
            p_intest.append(intes[i])
            p_abdom.append(abdom[i])
            coryn.append('1')

        elif acanth[i] == 'CP' or acanth[i] == 'cp':
            p_intest.append('1')
            p_abdom.append(abdom[i])
            coryn.append(intes[i])

        elif acanth[i] == '' or acanth[i] == '-':
            p_intest.append('-')
            p_abdom.append('-')
            coryn.append('-')

        else:
            p_intest.append('9')
            p_abdom.append('9')
            coryn.append('9')


    return p_intest, p_abdom, coryn


def errorAcanth(soNo, acanth, intes, abdom):
    wrongAcanth = []
    positiveSet = ['1', '2', '3', 'Y', 'y', 'Y(CORY', 'Y(PROF', 'Y(CORY & PROF', 'Y(C & P)', 'P', 'p', 'C', 'c', 'PC', 'pc', 'cp', 'CP']
    for i in range(len(soNo)):
        if acanth[i] in positiveSet:
            if intes[i] != '1' and intes[i] != '2' and intes[i] != '3':
                wrongAcanth.append(soNo[i])

        if abdom[i] == '1' or abdom[i] == '2' or abdom[i] == '3':
            if acanth[i] not in positiveSet:
                wrongAcanth.append(soNo[i])

        if acanth[i] == 'N' or acanth[i] == 'n':
            if intes[i] != '0':
                wrongAcanth.append(soNo[i])

    return wrongAcanth


def main():
    file = "C:/Users/Richard/Desktop/AcanthData/acanth_data_all.csv"  # import data file
    data = impData(file)
    soNo = list(np.array(data)[1:, 0])
    date = list(np.array(data)[1:, 1])
    month = list(np.array(data)[1:, 2])
    year = list(np.array(data)[1:, 3])
    area = list(np.array(data)[1:, 6])
    atos = list(np.array(data)[1:, 7])
    cond = list(np.array(data)[1:, 11])
    cond2 = list(np.array(data)[1:, 12])
    age = list(np.array(data)[1:, 14])
    age2 = list(np.array(data)[1:, 15])
    totalLength = list(np.array(data)[1:, 16])
    toothCond = list(np.array(data)[1:, 20])
    grizz = list(np.array(data)[1:, 19])
    sex = list(np.array(data)[1:, 13])

    acanth = list(np.array(data)[1:, 28])
    intes = list(np.array(data)[1:, 29])
    abdom = list(np.array(data)[1:, 30])

    print(acanth)

    duplicates = findDupes(soNo)
    duplicates2 = findDupes2(soNo)
    wrongSONO = fixDates(soNo, date, month, year)
    wrongArea = fixArea(area, atos, soNo)
    wrongCond = fixCond(cond, cond2, soNo)
    wrongAge = fixAge(age, age2, soNo)
    wrongLength, lengthDiff, fAge, fTL, fSex, fGrizz, fToothCond = fixLength(age, totalLength, soNo, sex, grizz, toothCond)
    wrongAcanth = errorAcanth(soNo, acanth, intes, abdom)
    p_intest, p_abdom, coryn = fixAcanth(acanth, intes, abdom)

    """for x in range(len(wrongLength)):
        print(wrongLength[x], lengthDiff[x], fAge[x], fTL[x], fSex[x], fGrizz[x], fToothCond[x])
    print('done with length')
    for x in range(len(wrongAge)):
        print(wrongAge[x])
    print('done with age')
    for x in range(len(wrongCond)):
        print(wrongCond[x])
    print('done with condition')
    for x in range(len(wrongArea)):
        print(wrongArea[x])
    print('done with area')
    for x in range(len(wrongSONO)):
        print(wrongSONO[x])
    print('done with SoNo')"""

    for x in range(len(p_intest)):
        print(p_intest[x], p_abdom[x], coryn[x])

    #print(duplicates)
    #print(duplicates2)

    """myFile = open('/Users/Richard/Desktop/acanth_data_filtered.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(filteredData)"""

main()