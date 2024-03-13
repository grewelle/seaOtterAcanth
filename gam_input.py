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

def main():
    file = "C:/Users/Richard/Desktop/AcanthData/confirmedPerit.csv"  # import data file
    data = impData(file)


    for i in range(len(data)):
        b = [0,60,6,4,5,15,24,25,32,34,53,52,33,51,40,16]
        row = [data[i][x] for x in b]
        sonum = row[0]
        ap = row[1]
        year = row[2]
        day = row[3]
        month = row[4]
        atos = row[5]
        sex = row[6]
        age = row[7]
        weight = row[8]
        length = row[9]
        prey = row[10]
        food = row[11]
        tail = row[12]
        fat = row[13]
        teeth = row[14]
        bay = row[15]

        output = [sonum]
        if ap == '0':
            output.append(0)
        else:
            output.append(1)

        output.append(year)
        if month == '1':
            index = 0
        elif month == '2':
            index = 31
        elif month == '3':
            index = 59
        elif month == '4':
            index = 90
        elif month == '5':
            index = 120
        elif month == '6':
            index = 151
        elif month == '7':
            index = 181
        elif month == '8':
            index = 212
        elif month == '9':
            index = 243
        elif month == '10':
            index = 273
        elif month == '11':
            index = 304
        else:
            index = 334
        output.append(index + int(day))

        try:
            abs(int(atos))
        except:
            output.append('NA')
        else:
            output.append(abs(int(atos)))

        output.append(sex)

        if age in ['2', '12']:
            output.append(2)
        elif age in ['3', '13']:
            output.append(3)
        elif age in ['4','14']:
            output.append(4)
        elif age in ['5', '15']:
            output.append(5)
        elif age in ['6', '16']:
            output.append(6)
        elif age in ['7', '17']:
            output.append(7)
        elif age in ['8', '18']:
            output.append(8)
        else:
            output.append('NA')

        try:
            wl = abs(100*float(weight)/(float(length)-float(tail)))
        except:
            output.append('NA')
        else:
            if float(weight) > 0 and float(length) > 0 and float(tail) > 0:
                output.append(wl)
            else:
                output.append('NA')

        set = ['emer', 'sand cr']
        unset = ['not emer', 'not sand cr']
        nu = ['1', '2', '3']
        num = ['0', '1', '2', '3']
        num2 = ['0', '1', '2', '3', '4']
        num3 = ['0', '1', '2', '3', '4', '5', '6']



        if food in num:
            if 'EMER' in prey or 'SAND CR' in prey or 'BLEPH' in prey or 'MOLE' in prey:
                if 'NOT EMER' in prey or 'NOT SAND CR' in prey:
                    output.append(0)
                else:
                    output.append(1)
            else:
                output.append(0)
        else:
            output.append('NA')

        if fat in num2:
            output.append(fat)
        else:
            output.append('NA')

        if teeth in num3:
            output.append(teeth)
        else:
            output.append('NA')

        if bay == 'y' or bay == 'Y':
            output.append(1)
        elif bay == 'n' or bay == 'N':
            output.append(0)
        else:
            output.append('NA')

        if food in nu:
            output.append(1)
        elif food in num:
            output.append(0)
        else:
            output.append('NA')

        #print(output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8])
        if teeth != '5':
            print(output[0], output[-1])

    """n = 4852
    z = np.random.negative_binomial(2,0.8, size = n)
    W = np.random.binomial(1, 1 / (1 + np.exp(-z)), size = n)
    print(W)"""



main()