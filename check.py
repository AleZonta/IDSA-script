import filecmp
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import logging
import seaborn as sns
import numpy


def compute():
    listLength, numberPoi, top5, top10, top, perf = loadOtherFile("/Users/alessandrozonta/Documents/ResultsExp/latest/200idsa/", "PacmanNormal")
    number_one = 99  #75
    number_two = 262  #210
    number_three = 470  # 351

    only_one = []
    only_one_top = []
    only_one_length = []
    only_two = []
    only_two_top = []
    only_two_length = []
    only_three = []
    only_three_top = []
    only_three_length = []
    for i in range(len(numberPoi)):
        only_only_one = []
        only_only_one_top = []
        only_only_one_length = []
        only_only_two = []
        only_only_two_top = []
        only_only_two_length  = []
        only_only_three = []
        only_only_three_top = []
        only_only_three_length = []
        for j in range(len(numberPoi[i])):
            if numberPoi[i][j] == number_one:
                only_only_one.append(numberPoi[i][j])
                only_only_one_top.append(top[i][j])
                only_only_one_length.append(listLength[i][j])
            elif numberPoi[i][j] == number_two:
                only_only_two.append(numberPoi[i][j])
                only_only_two_top.append(top[i][j])
                only_only_two_length.append(listLength[i][j])
            elif numberPoi[i][j] == number_three:
                only_only_three.append(numberPoi[i][j])
                only_only_three_top.append(top[i][j])
                only_only_three_length.append(listLength[i][j])
        if len(only_only_one) > 0: only_one.append(only_only_one)
        if len(only_only_one_top) > 0: only_one_top.append(only_only_one_top)
        if len(only_only_one_length) > 0: only_one_length.append(only_only_one_length)
        if len(only_only_two) > 0: only_two.append(only_only_two)
        if len(only_only_two_top) > 0: only_two_top.append(only_only_two_top)
        if len(only_only_two_length) > 0: only_two_length.append(only_only_two_length)
        if len(only_only_three) > 0: only_three.append(only_only_three)
        if len(only_only_three_top) > 0: only_three_top.append(only_only_three_top)
        if len(only_only_three_length) > 0: only_three_length.append(only_only_three_length)

    median = []
    realTop = []
    for x in range(len(only_one_top)):
        appo = []
        try:
            for y in range(len(only_one_top[x])):
                appo.append((100 * only_one_top[x][y]) / only_one_length[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    median_two = []
    realTop = []
    for x in range(len(only_two_top)):
        appo = []
        try:
            for y in range(len(only_two_top[x])):
                appo.append((100 * only_two_top[x][y]) / only_two_length[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median_two.append(np.median(el))

    median_three = []
    realTop = []
    for x in range(len(only_two_top)):
        appo = []
        try:
            for y in range(len(only_three_top[x])):
                appo.append((100 * only_three_top[x][y]) / only_three_length[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median_three.append(np.median(el))


    # values = []
    # values.append(np.median(median))
    # values.append(np.median(median_two))
    # values.append(np.median(median_three))
    #
    # logging.debug(values)

    # plt.figure(1)
    # x = np.arange(len(median))
    # a = plt.scatter(x, median, c="r")
    # plt.ylabel("Different settings")
    #
    # plt.ylabel('Percentage before the end of the tracking path')
    # plt.ylim(0, 100)
    # plt.xlim(-1, len(x) + 1)
    # # plt.show()
    #
    #
    # plt.figure(2)
    # x = np.arange(len(median_two))
    # a = plt.scatter(x, median_two, c="r")
    # plt.ylabel("Different settings")
    #
    # plt.ylabel('Percentage before the end of the tracking path')
    # plt.ylim(0, 100)
    # plt.xlim(-1, len(x) + 1)
    #
    # plt.figure(3)
    # x = np.arange(len(median_three))
    # a = plt.scatter(x, median_three, c="r")
    # plt.ylabel("Different settings")
    #
    # plt.ylabel('Percentage before the end of the tracking path')
    # plt.ylim(0, 100)
    # plt.xlim(-1, len(x) + 1)
    # plt.show()
    #
    plt.figure(1)
    plt.boxplot(median, whis=50)
    x = np.arange(1, len(median) + 1)
    plt.ylabel("Percentage before the end of the tracking path")
    plt.show()

    s = "trwsa"


def loadOtherFile(path, nameExp):
    listLenght = []
    path += nameExp
    pathFastRead = path + "/listlength-" + nameExp + ".txt"
    try:
        with open(pathFastRead) as f:
            for content in f:
                value = content.split(" ")
                if "\n" in value:
                    value.remove("\n")
                valueReal = []
                for el in value:
                    valueReal.append(float(el))
                listLenght.append(valueReal)
    except:
        pass
    pathFastRead = path + "/numberPoi-" + nameExp + ".txt"
    numberPoi = []
    try:
        with open(pathFastRead) as f:
            for content in f:
                value = content.split(" ")
                if "\n" in value:
                    value.remove("\n")
                valueReal = []
                for el in value:
                    valueReal.append(float(el))
                numberPoi.append(valueReal)
    except:
        pass
    pathFastRead = path + "/listTop5-" + nameExp + ".txt"
    top5 = []
    with open(pathFastRead) as f:
        for content in f:
            value = content.split(" ")
            if "\n" in value:
                value.remove("\n")
            valueReal = []
            for el in value:
                valueReal.append(float(el))
            top5.append(valueReal)
    pathFastRead = path + "/listTop10-" + nameExp + ".txt"
    top10 = []
    with open(pathFastRead) as f:
        for content in f:
            value = content.split(" ")
            if "\n" in value:
                value.remove("\n")
            valueReal = []
            for el in value:
                valueReal.append(float(el))
            top10.append(valueReal)
    pathFastRead = path + "/listTop-" + nameExp + ".txt"
    top = []
    with open(pathFastRead) as f:
        for content in f:
            value = content.split(" ")
            if "\n" in value:
                value.remove("\n")
            valueReal = []
            for el in value:
                valueReal.append(float(el))
            top.append(valueReal)

    pathFastRead = path + "/Performance-" + nameExp + ".txt"
    perf = []
    with open(pathFastRead) as f:
        for content in f:
            value = content.split(" ")
            if "\n" in value:
                value.remove("\n")
            valueReal = []
            for el in value:
                valueReal.append(float(el))
            perf.append(valueReal)

    return listLenght, numberPoi, top5, top10, top, perf

# main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None
    compute()
    logging.debug("End Program")