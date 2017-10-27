import logging
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
from pandas import scatter_matrix
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from sklearn.decomposition import PCA

from pandas.tools.plotting import parallel_coordinates
from sklearn.preprocessing import StandardScaler


def loadOtherFile(path, name):
    logging.debug("Reading files of {}".format(name))
    listLenght = []
    pathFastRead = path + "/listlength-" + name + ".txt"
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
    pathFastRead = path + "/numberPoi-" + name + ".txt"
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
    pathFastRead = path + "/listTop5-" + name + ".txt"
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
    pathFastRead = path + "/listTop10-" + name + ".txt"
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
    pathFastRead = path + "/listTop-" + name + ".txt"
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

    # pathFastRead = path + "/Performance-" + name + ".txt"
    perf = []
    # with open(pathFastRead) as f:
    #     for content in f:
    #         value = content.split(" ")
    #         if "\n" in value:
    #             value.remove("\n")
    #         valueReal = []
    #         for el in value:
    #             valueReal.append(float(el))
    #         perf.append(valueReal)

    # pathFastRead = path + "/lengthTracks-" + name + ".txt"
    track = []
    # with open(pathFastRead) as f:
    #     for content in f:
    #         value = content.split(" ")
    #         if "\n" in value:
    #             value.remove("\n")
    #         valueReal = []
    #         for el in value:
    #             valueReal.append(float(el))
    #         track.append(valueReal)

    return listLenght, numberPoi, top5, top10, top, perf, track


def readPar(path, files):
    listRules = []
    # files = ["param1", "param2", "param3", "param4", "param5", "param6", "param7", "param8"]
    for el in files:
        pathFastRead = path + "/" + el
        try:
            with open(pathFastRead) as f:
                for content in f:
                    value = content.split(" ")
                    if str(value[7]) == "1":
                        listRules.append(value[:5])
        except:
            logging.debug("No parameters file present")

    if len(listRules) == 0:
        return None
    # now I know all the rules
    # should find the parameters
    # inside listNumberRule I have all the index
    return listRules


def divideRules(listRules):
    degree30 = []
    degree60 = []
    degree120 = []
    degree180 = []
    degree240 = []
    s1025 = []
    s105 = []
    s11 = []
    w10005 = []
    w1001 = []
    w1002 = []
    s2025 = []
    s205 = []
    s201 = []
    w2025 = []
    w205 = []
    w201 = []
    for x in range(len(listRules)):
        # degree
        if listRules[x][0] == "30.0":
            degree30.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][0] == "60.0":
            degree60.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][0] == "120.0":
            degree120.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][0] == "180.0":
            degree180.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][0] == "240":
            degree240.append({"ID": x, "Rule": listRules[x]})
        # s1
        if listRules[x][1] == "0.25":
            s1025.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][1] == "0.5":
            s105.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][1] == "1.0":
            s11.append({"ID": x, "Rule": listRules[x]})
        # w1
        if listRules[x][2] == "0.005":
            w10005.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][2] == "0.01":
            w1001.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][2] == "0.02":
            w1002.append({"ID": x, "Rule": listRules[x]})
        # s2
        if listRules[x][3] == "0.25":
            s2025.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][3] == "0.5":
            s205.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][3] == "0.1":
            s201.append({"ID": x, "Rule": listRules[x]})
        # w2
        if listRules[x][4] == "0.25":
            w2025.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][4] == "0.5":
            w205.append({"ID": x, "Rule": listRules[x]})
        elif listRules[x][4] == "0.1":
            w201.append({"ID": x, "Rule": listRules[x]})

    return degree30, degree60, degree120, degree180, degree240, s1025, s105, s11, w10005, w1001, w1002, s2025, s205, s201, w2025, w205, w201


def compute(nameExperiemnt, path):
    list_length, numberPoi, top5, top10, top, perf, track = loadOtherFile(path, nameExperiemnt)
    listRules = readPar(path, ["p1"])
    degree30, degree60, degree120, degree180, degree240, s1025, s105, s11, w10005, w1001, w1002, s2025, s205, s201, w2025, w205, w201 = divideRules(
        listRules)

    x = [list_length, numberPoi, top5, top10, top, perf, track, degree120, degree180, degree240, s1025, s105, s11, w10005,
         w1001, w1002, s2025, s205, s201, w2025, w205, w201]
    first = [listRules, top, list_length]
    par(first)

    # par2(first)
    # showEveryParameter(tot)
    # showEveryParameter(degree30, degree60, degree120, s1025, s105, s11, w10005, w1001, w1002, s2025, s205, s201, w2025, w205, w201, top)

    # showRelation120withOther(tot)

    # showRelation120oneSettingAndOthers(tot)


# print graph
def showGraph(axes, ax_x, ax_y, totalValueNeeded, color, title):
    for y in range(len(totalValueNeeded)):
        x = np.arange(len(totalValueNeeded[y]))
        axes[ax_x, ax_y].scatter(x, totalValueNeeded[y], c=color[y])
        axes[ax_x, ax_y].set_xlim([x[0] - 1, x[len(totalValueNeeded[y]) - 1] + 1])
    axes[ax_x, ax_y].set_ylim(0, 200)
    axes[ax_x, ax_y].set_title(title, fontsize=10)


# compute graph with two parameters
def computeValueWithTwoParam(degree, totalMedian, ind_var1, val1, ind_var2, val2):
    totalValueNeeded = []
    for x in range(len(degree)):
        valueMedianNeeded = []
        for y in range(len(degree[x])):
            try:
                if degree[x][y]["Rule"][ind_var1] == val1 and degree[x][y]["Rule"][ind_var2] == val2:
                    valueMedianNeeded.append(totalMedian[x][degree[x][y]["ID"]])
            except:
                pass
        totalValueNeeded.append(valueMedianNeeded)
    return totalValueNeeded


# compute graph with one parameters
def computeValueWithOneParam(degree, totalMedian, ind_var1, val1):
    totalValueNeeded = []
    for x in range(len(degree)):
        valueMedianNeeded = []
        for y in range(len(degree[x])):
            try:
                if degree[x][y]["Rule"][ind_var1] == val1:
                    valueMedianNeeded.append(totalMedian[x][degree[x][y]["ID"]])
            except:
                pass
        totalValueNeeded.append(valueMedianNeeded)
    return totalValueNeeded


# find relation between angle 120 , another settings and all the others
def showRelation120oneSettingAndOthers(tot):
    degree120 = [tot[0][9], tot[1][9]]
    top = [tot[0][4], tot[1][4]]
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 5))

    color = ["r", "b"]

    totalMedian = []
    for el in top:
        median = []
        for elem in el:
            median.append(np.median(elem))
        totalMedian.append(median)

    #
    #
    # 120 degree with w2 = 0.25 -> s2 = 0.25
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 3, "0.25")
    showGraph(axes, 0, 0, totalValueNeeded, color, "120 degrees with w2 = 0.25 and s2 = 0.25")

    #
    #
    # 120 degree with w2 = 0.25 -> s2 = 0.5
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 3, "0.5")
    showGraph(axes, 0, 1, totalValueNeeded, color, "120 degrees with w2 = 0.25 and s2 = 0.5")

    #
    #
    # 120 degree with w2 = 0.25 -> s2 = 0.1
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 3, "0.1")
    showGraph(axes, 0, 2, totalValueNeeded, color, "120 degrees with w2 = 0.25 and s2 = 0.1")

    #
    #
    # 120 degree with w2 = 0.25 -> w1 = 0.005
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 2, "0.005")
    showGraph(axes, 1, 0, totalValueNeeded, color, "120 degrees with w2 = 0.25 and w1 = 0.005")

    #
    #
    # 120 degree with w2 = 0.25 -> w1 = 0.01
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 2, "0.01")
    showGraph(axes, 1, 1, totalValueNeeded, color, "120 degrees with w2 = 0.25 and w1 = 0.01")

    #
    #
    # 120 degree with w2 = 0.25 -> w1 = 0.02
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 2, "0.02")
    showGraph(axes, 1, 2, totalValueNeeded, color, "120 degrees with w2 = 0.25 and s2 = 0.02")

    #
    #
    # 120 degree with w2 = 0.25 -> s1 = 0.25
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 1, "0.25")
    showGraph(axes, 2, 0, totalValueNeeded, color, "120 degrees with w2 = 0.25 and s1 = 0.25")

    #
    #
    # 120 degree with w2 = 0.25 -> s1 = 0.5
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 1, "0.5")
    showGraph(axes, 2, 1, totalValueNeeded, color, "120 degrees with w2 = 0.25 and s1 = 0.5")

    #
    #
    # 120 degree with w2 = 0.25 -> s1 = 1.0
    totalValueNeeded = computeValueWithTwoParam(degree120, totalMedian, 4, "0.25", 1, "1.0")
    showGraph(axes, 2, 2, totalValueNeeded, color, "120 degrees with w2 = 0.25 and s1 = 1.0")

    plt.show()


# find relation between angle 120 and all the others
def showRelation120withOther(tot):
    degree120 = [tot[0][9], tot[1][9]]
    top = [tot[0][4], tot[1][4]]
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12, 5))

    color = ["r", "b"]

    totalMedian = []
    for el in top:
        median = []
        for elem in el:
            median.append(np.median(elem))
        totalMedian.append(median)

    #
    # 120 degree with w2 = 0.25
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 4, "0.25")
    showGraph(axes, 0, 0, totalValueNeeded, color, "120 degrees with w2 = 0.25")

    #
    # 120 degree with w2 = 0.5
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 4, "0.5")
    showGraph(axes, 0, 1, totalValueNeeded, color, "120 degrees with w2 = 0.5")

    #
    # 120 degree with w2 = 0.1
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 4, "0.1")
    showGraph(axes, 0, 2, totalValueNeeded, color, "120 degrees with w2 = 0.1")

    #
    # 120 degree with s2 = 0.25
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 3, "0.25")
    showGraph(axes, 1, 0, totalValueNeeded, color, "120 degrees with s2 = 0.25")

    #
    # 120 degree with s2 = 0.5
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 3, "0.5")
    showGraph(axes, 1, 1, totalValueNeeded, color, "120 degrees with s2 = 0.5")

    #
    # 120 degree with s2 = 0.1
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 3, "0.1")
    showGraph(axes, 1, 2, totalValueNeeded, color, "120 degrees with s2 = 0.1")

    #
    # 120 degree with w1 = 0.005
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 2, "0.005")
    showGraph(axes, 2, 0, totalValueNeeded, color, "120 degrees with w1 = 0.005")

    #
    # 120 degree with w1 = 0.01
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 2, "0.01")
    showGraph(axes, 2, 1, totalValueNeeded, color, "120 degrees with w1 = 0.01")

    #
    # 120 degree with w1 = 0.02
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 2, "0.02")
    showGraph(axes, 2, 2, totalValueNeeded, color, "120 degrees with w1 = 0.02")

    #
    # 120 degree with s1 = 0.25
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 1, "0.25")
    showGraph(axes, 3, 0, totalValueNeeded, color, "120 degrees with s1 = 0.25")

    #
    # 120 degree with s1 = 0.5
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 1, "0.5")
    showGraph(axes, 3, 1, totalValueNeeded, color, "120 degrees with s1 = 0.5")

    #
    # 120 degree with s1 = 1.0
    totalValueNeeded = computeValueWithOneParam(degree120, totalMedian, 1, "1.0")
    showGraph(axes, 3, 2, totalValueNeeded, color, "120 degrees with s1 = 1.0")

    plt.show()


# show rules ordered per every parameter
def showEveryParameter(tot):
    degree30 = [tot[0][7], tot[1][7]]
    degree60 = [tot[0][8], tot[1][8]]
    degree120 = [tot[0][9], tot[1][9]]
    s1025 = [tot[0][10], tot[1][10]]
    s105 = [tot[0][11], tot[1][11]]
    s11 = [tot[0][12], tot[1][12]]
    w10005 = [tot[0][13], tot[1][13]]
    w1001 = [tot[0][14], tot[1][14]]
    w1002 = [tot[0][15], tot[1][15]]
    s2025 = [tot[0][16], tot[1][16]]
    s205 = [tot[0][17], tot[1][17]]
    s201 = [tot[0][18], tot[1][18]]
    w2025 = [tot[0][19], tot[1][19]]
    w205 = [tot[0][20], tot[1][20]]
    w201 = [tot[0][21], tot[1][21]]
    top = [tot[0][4], tot[1][4]]
    listLenght = [tot[0][0], tot[1][0]]

    median = []
    realTop = []
    for x in range(len(top[0])):
        appo = []
        for y in range(len(top[0][x])):
            appo.append((100 * top[0][x][y]) / listLenght[0][x][y])
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    medianTwo = []
    realTopTwo = []
    for x in range(len(top[1])):
        appo = []
        for y in range(len(top[1][x])):
            appo.append((100 * top[1][x][y]) / listLenght[1][x][y])
        realTopTwo.append(appo)
    for el in realTopTwo:
        medianTwo.append(np.median(el))

    fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(12, 5))

    # value for 30 degree
    valueMedianNeeded = []
    for el in degree30[0]:
        valueMedianNeeded.append(median[el["ID"]])
    valueMedianNeededTwo = []
    for el in degree30[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[0, 0].scatter(x, valueMedianNeeded, c="r")
    axes[0, 0].scatter(x, valueMedianNeededTwo, c="b")
    axes[0, 0].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[0, 0].set_ylim(0, 35)
    axes[0, 0].set_title("30 degrees", fontsize=10)

    # value for 60 degree
    valueMedianNeeded = []
    rules = []
    for el in degree60[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    for el in degree60[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[0, 1].scatter(x, valueMedianNeeded, c="r")
    axes[0, 1].scatter(x, valueMedianNeededTwo, c="b")
    axes[0, 1].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[0, 1].set_ylim(0, 35)
    axes[0, 1].set_title("60 degrees", fontsize=10)

    # value for 120 degree
    valueMedianNeeded = []
    rules = []
    for el in degree120[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    try:
        for el in degree120[1]:
            valueMedianNeededTwo.append(medianTwo[el["ID"]])
    except:
        pass

    x = np.arange(len(valueMedianNeeded))
    axes[0, 2].scatter(x, valueMedianNeeded, c="r")
    x = np.arange(len(valueMedianNeededTwo))
    axes[0, 2].scatter(x, valueMedianNeededTwo, c="b")
    axes[0, 2].set_xlim([x[0] - 1, x[len(valueMedianNeededTwo) - 1] + 1])
    axes[0, 2].set_ylim(0, 35)
    axes[0, 2].set_title("120 degrees", fontsize=10)

    # value for s1025 degree
    valueMedianNeeded = []
    rules = []
    for el in s1025[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    try:
        for el in s1025[1]:
            valueMedianNeededTwo.append(medianTwo[el["ID"]])
    except:
        pass

    x = np.arange(len(valueMedianNeeded))
    axes[1, 0].scatter(x, valueMedianNeeded, c="r")
    x = np.arange(len(valueMedianNeededTwo))
    axes[1, 0].scatter(x, valueMedianNeededTwo, c="b")
    axes[1, 0].set_xlim([x[0] - 1, x[len(valueMedianNeededTwo) - 1] + 1])
    axes[1, 0].set_ylim(0, 35)
    axes[1, 0].set_title("s1 = 0.25", fontsize=10)

    # value for s105 degree
    valueMedianNeeded = []
    rules = []
    for el in s105[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    for el in s1025[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[1, 1].scatter(x, valueMedianNeeded, c="r")
    axes[1, 1].scatter(x, valueMedianNeededTwo, c="b")
    axes[1, 1].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[1, 1].set_ylim(0, 35)
    axes[1, 1].set_title("s1 = 0.5", fontsize=10)

    # value for s11 degree
    valueMedianNeeded = []
    rules = []
    for el in s11[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    try:
        for el in s11[1]:
            valueMedianNeededTwo.append(medianTwo[el["ID"]])
    except:
        pass

    x = np.arange(len(valueMedianNeeded))
    axes[1, 2].scatter(x, valueMedianNeeded, c="r")
    x = np.arange(len(valueMedianNeededTwo))
    axes[1, 2].scatter(x, valueMedianNeededTwo, c="b")
    axes[1, 2].set_xlim([x[0] - 1, x[len(valueMedianNeededTwo) - 1] + 1])
    axes[1, 2].set_ylim(0, 35)
    axes[1, 2].set_title("s1 = 1.0", fontsize=10)

    # value for w10005 degree
    valueMedianNeeded = []
    rules = []
    for el in w10005[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    for el in w10005[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[2, 0].scatter(x, valueMedianNeeded, c="r")
    axes[2, 0].scatter(x, valueMedianNeededTwo, c="b")
    axes[2, 0].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[2, 0].set_ylim(0, 35)
    axes[2, 0].set_title("w1 = 0.0005", fontsize=10)

    # value for w1001 degree
    valueMedianNeeded = []
    rules = []
    for el in w1001[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    for el in w1001[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[2, 1].scatter(x, valueMedianNeeded, c="r")
    axes[2, 1].scatter(x, valueMedianNeededTwo, c="b")
    axes[2, 1].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[2, 1].set_ylim(0, 35)
    axes[2, 1].set_title("w1 = 0.001", fontsize=10)

    # value for w1002 degree
    valueMedianNeeded = []
    rules = []
    for el in w1002[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    try:
        for el in w1002[1]:
            valueMedianNeededTwo.append(medianTwo[el["ID"]])
    except:
        pass

    x = np.arange(len(valueMedianNeeded))
    axes[2, 2].scatter(x, valueMedianNeeded, c="r")
    x = np.arange(len(valueMedianNeededTwo))
    axes[2, 2].scatter(x, valueMedianNeededTwo, c="b")
    axes[2, 2].set_xlim([x[0] - 1, x[len(valueMedianNeededTwo) - 1] + 1])
    axes[2, 2].set_ylim(0, 35)
    axes[2, 2].set_title("w1 = 0.002", fontsize=10)

    # value for s2025 degree
    valueMedianNeeded = []
    rules = []
    for el in s2025[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    for el in s2025[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[3, 0].scatter(x, valueMedianNeeded, c="r")
    axes[3, 0].scatter(x, valueMedianNeededTwo, c="b")
    axes[3, 0].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[3, 0].set_ylim(0, 35)
    axes[3, 0].set_title("s2 = 0.25", fontsize=10)

    # value for s205 degree
    valueMedianNeeded = []
    rules = []
    for el in s205[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    try:
        for el in s205[1]:
            valueMedianNeededTwo.append(medianTwo[el["ID"]])
    except:
        pass

    x = np.arange(len(valueMedianNeeded))
    axes[3, 1].scatter(x, valueMedianNeeded, c="r")
    x = np.arange(len(valueMedianNeededTwo))
    axes[3, 1].scatter(x, valueMedianNeededTwo, c="b")
    axes[3, 1].set_xlim([x[0] - 1, x[len(valueMedianNeededTwo) - 1] + 1])
    axes[3, 1].set_ylim(0, 35)
    axes[3, 1].set_title("s2 = 0.5", fontsize=10)

    # value for s201 degree
    valueMedianNeeded = []
    rules = []
    for el in s201[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    for el in s201[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[3, 2].scatter(x, valueMedianNeeded, c="r")
    axes[3, 2].scatter(x, valueMedianNeededTwo, c="b")
    axes[3, 2].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[3, 2].set_ylim(0, 35)
    axes[3, 2].set_title("s2 = 0.1", fontsize=10)

    # value for w2025 degree
    valueMedianNeeded = []
    rules = []
    for el in w2025[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    for el in w2025[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[4, 0].scatter(x, valueMedianNeeded, c="r")
    axes[4, 0].scatter(x, valueMedianNeededTwo, c="b")
    axes[4, 0].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[4, 0].set_ylim(0, 35)
    axes[4, 0].set_title("w2 = 0.25", fontsize=10)

    # value for w205 degree
    valueMedianNeeded = []
    rules = []
    for el in w205[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    try:
        for el in w205[1]:
            valueMedianNeededTwo.append(medianTwo[el["ID"]])
    except:
        pass

    x = np.arange(len(valueMedianNeeded))
    axes[4, 1].scatter(x, valueMedianNeeded, c="r")
    x = np.arange(len(valueMedianNeededTwo))
    axes[4, 1].scatter(x, valueMedianNeededTwo, c="b")
    axes[4, 1].set_xlim([x[0] - 1, x[len(valueMedianNeededTwo) - 1] + 1])
    axes[4, 1].set_ylim(0, 35)
    axes[4, 1].set_title("w2 = 0.5", fontsize=10)

    # value for w201 degree
    valueMedianNeeded = []
    rules = []
    for el in w201[0]:
        valueMedianNeeded.append(median[el["ID"]])
        rules.append(el["Rule"])
    valueMedianNeededTwo = []
    for el in w201[1]:
        valueMedianNeededTwo.append(medianTwo[el["ID"]])

    x = np.arange(len(valueMedianNeeded))
    axes[4, 2].scatter(x, valueMedianNeeded, c="r")
    axes[4, 2].scatter(x, valueMedianNeededTwo, c="b")
    axes[4, 2].set_xlim([x[0] - 1, x[len(valueMedianNeeded) - 1] + 1])
    axes[4, 2].set_ylim(0, 35)
    axes[4, 2].set_title("w2 = 0.1", fontsize=10)

    fig.subplots_adjust(hspace=0.6)
    plt.show()


def findValues(list, sublist):
    valueMedianNeeded = []
    for el in sublist:
        valueMedianNeeded.append(list[int(el["ID"]) - 1])
    return valueMedianNeeded


def findValuesFour(list, sublist, inx, val):
    valueMedianNeeded = []
    for el in sublist:
        if el["Rule"][inx] == val:
            valueMedianNeeded.append(list[int(el["ID"]) - 1])
    return valueMedianNeeded


# try new view
def par(second):
    # first = [listRules, top, list_length]
    # degree30 = [tot[0][7], tot[1][7]]
    # degree60 = [tot[0][8], tot[1][8]]
    # degree120 = [tot[0][9], tot[1][9]]
    # s1025 = [tot[0][10], tot[1][10]]
    # s105 = [tot[0][11], tot[1][11]]
    # s11 = [tot[0][12], tot[1][12]]
    # w10005 = [tot[0][13], tot[1][13]]
    # w1001 = [tot[0][14], tot[1][14]]
    # w1002 = [tot[0][15], tot[1][15]]
    # s2025 = [tot[0][16], tot[1][16]]
    # s205 = [tot[0][17], tot[1][17]]
    # s201 = [tot[0][18], tot[1][18]]
    # w2025 = [tot[0][19], tot[1][19]]
    # w205 = [tot[0][20], tot[1][20]]
    # w201 = [tot[0][21], tot[1][21]]
    # top = [tot[0][4], tot[1][4]]
    # listLength = [tot[0][0], tot[1][0]]
    #
    # median = []
    # realTop = []
    # for x in range(len(top[1])):
    #     appo = []
    #     for y in range(len(top[1][x])):
    #         appo.append((100 * top[1][x][y]) / listLength[1][x][y])
    #     realTop.append(appo)
    # for el in realTop:
    #     median.append(np.median(el))
    #
    # # value for 30 degree
    # d30 = findValues(median, degree30[1])
    # d60 = findValues(median, degree60[1])
    # d120 = findValues(median, degree120[1])
    # s1v1 = findValues(median, s1025[1])
    # s1v2 = findValues(median, s105[1])
    # s1v3 = findValues(median, s11[1])
    # w1v1 = findValues(median, w10005[1])
    # w1v2 = findValues(median, w1001[1])
    # w1v3 = findValues(median, w1002[1])
    # s2v1 = findValues(median, s2025[1])
    # s2v2 = findValues(median, s205[1])
    # s2v3 = findValues(median, s201[1])
    # w2v1 = findValues(median, w2025[1])
    # w2v2 = findValues(median, w205[1])
    # w2v3 = findValues(median, w201[1])
    #
    # xx = {"d30": d30, "d60": d60, "d120": d120, "s1.025": s1v1, "s1.05": s1v2, "s1.1": s1v3, "w1.0005": w1v1,
    #       "w1.001": w1v2,
    #       "w1.002": w1v3, "s2.025": s2v1, "s2.05": s2v2, "s2.01": s2v3, "w2.025": w2v1, "w2.05": w2v2, "w2.01": w2v3}
    # df = DataFrame(data=xx)
    # sns.pairplot(df)
    # # scatter_matrix(df, alpha=0.2, figsize=(6, 6))
    # plt.show()
    median = []
    realTop = []
    for x in range(len(second[1])):
        appo = []
        try:
            for y in range(len(second[1][x])):
                appo.append((100 * second[1][x][y]) / second[2][x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    if len(median) == 242:
        median.append(np.median(median))

    angle = []
    s1 = []
    w1 = []
    s2 = []
    w2 = []
    for el in second[0]:
        if el[0] == "240":
            angle.append(240.0)
        if el[0] == "180.0":
            angle.append(180.0)
        if el[0] == "120.0":
            angle.append(120.0)
        if el[0] == "60.0":
            angle.append(60.0)
        if el[0] == "30.0":
            angle.append(30.0)
        if el[1] == "0.25":
            s1.append(0.25)
        if el[1] == "0.5":
            s1.append(0.5)
        if el[1] == "1.0":
            s1.append(1.0)
        if el[2] == "0.005":
            w1.append(0.005)
        if el[2] == "0.01":
            w1.append(0.01)
        if el[2] == "0.02":
            w1.append(0.02)
        if el[3] == "0.25":
            s2.append(0.25)
        if el[3] == "0.5":
            s2.append(0.5)
        if el[3] == "0.1":
            s2.append(0.1)
        if el[4] == "0.25":
            w2.append(0.25)
        if el[4] == "0.5":
            w2.append(0.5)
        if el[4] == "0.1":
            w2.append(0.1)

    x = np.arange(len(angle))

    # yy = {"angle": angle, "s1 * 100": s1, "s2 * 100": s2, "w1 * 10000": w1, "w2 * 100": w2, "median * 10": median, "x": x}
    zz = {"angle": angle, "s1": s1, "s2": s2, "w1": w1, "w2": w2, "median": median}



    # sizes = []
    # for el in median:
    #     OldRange = (np.array(median).max() - np.array(median).min())
    #     NewRange = (500 - 1)
    #     sizes.append((((el - np.array(median).min()) * NewRange) / OldRange) + 1)


    # df = DataFrame(data=yy)
    # dfs = DataFrame(data=zz)
    # g = sns.PairGrid(dfs,  vars=["angle", "s1", "s2", "w1", "w2"])
    # # g.map(plt.scatter, s=sizes, facecolors='none', edgecolors='b')
    # g.map(plt.scatter)
    # g.map_diag(plt.hist)

    # dfs = DataFrame(data=zz)
    # g = sns.PairGrid(dfs, hue="median")
    # g.map(plt.scatter)
    # g.map_diag(plt.hist)
    sizes = []
    for el in median:
        OldRange = (np.array(median).max() - np.array(median).min())
        NewRange = (400 - 1)
        sizes.append((((el - np.array(median).min()) * NewRange) / OldRange) + 1)

    plt.figure(1)
    # df = DataFrame(data=yy)
    dfs = DataFrame(data=zz)
    g = sns.PairGrid(dfs, vars=["angle", "s1", "s2", "w1", "w2"])
    # g.map(plt.scatter, s=sizes)
    # g.map_diag(plt.hist)
    g.map(sns.stripplot, jitter=0.25, hue=median)

    plt.figure(2)
    g = sns.PairGrid(dfs, vars=["angle", "s1", "s2", "w1", "w2"])
    g.map(plt.scatter, s=sizes, facecolors='none', edgecolors='b')
    # plt.show()

    plt.show()


def par2(second):
    # first = [listRules, top, list_length]
    median = []
    realTop = []
    for x in range(len(second[1])):
        appo = []
        try:
            for y in range(len(second[1][x])):
                appo.append((100 * second[1][x][y]) / second[2][x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    if len(median) == 242:
        median.append(np.median(median))

    angle = []
    s1 = []
    w1 = []
    s2 = []
    w2 = []
    for el in second[0]:
        if el[0] == "240":
            angle.append(240.0)
        if el[0] == "180.0":
            angle.append(180.0)
        if el[0] == "120.0":
            angle.append(120.0)
        if el[0] == "60.0":
            angle.append(60.0)
        if el[0] == "30.0":
            angle.append(30.0)
        if el[1] == "0.25":
            s1.append(0.25)
        if el[1] == "0.5":
            s1.append(0.5)
        if el[1] == "1.0":
            s1.append(1.0)
        if el[2] == "0.005":
            w1.append(0.005)
        if el[2] == "0.01":
            w1.append(0.01)
        if el[2] == "0.02":
            w1.append(0.02)
        if el[3] == "0.25":
            s2.append(0.25)
        if el[3] == "0.5":
            s2.append(0.5)
        if el[3] == "0.1":
            s2.append(0.1)
        if el[4] == "0.25":
            w2.append(0.25)
        if el[4] == "0.5":
            w2.append(0.5)
        if el[4] == "0.1":
            w2.append(0.1)

    x = np.arange(len(angle))
    # yy = {"angle": angle, "s1 * 100": s1, "s2 * 100": s2, "w1 * 10000": w1, "w2 * 100": w2, "median * 10": median, "x": x}
    zz = {"angle": angle, "s1": s1, "s2": s2, "w1": w1, "w2": w2}

    # df = DataFrame(data=yy)
    dfs = DataFrame(data=zz)

    X_std = StandardScaler().fit_transform(dfs)

    pca = PCA(n_components=5)
    pca.fit(X_std)

    plt.figure(1)
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance')
    # plt.show()

    dfs = pca.fit_transform(X_std)

    x = []
    y = []
    for el in dfs:
        x.append(el[0])
        y.append(el[1])

    # plt.figure(2)
    # plt.scatter(x[:80], y[:80], alpha=0.5, c='y')
    # plt.scatter(x[81:161], y[81:161], alpha=0.5, c='r')
    # plt.scatter(x[162:242], y[162:242], alpha=0.5, c='g')
    # plt.scatter(x[243:], y[243:], alpha=0.5, c='b')
    # # g = sns.PairGrid(dfs)
    # g.map(plt.scatter)
    # g.map_diag(plt.hist)
    # plt.figure(3)
    # plt.scatter(x, y, alpha=0.5, c=median, edgecolor='none',
    #         cmap=plt.cm.get_cmap('nipy_spectral', 100))
    # plt.colorbar()

    plt.show()

    # parallel_coordinates(df, 'x', colormap='gist_rainbow')

    # scatter_matrix(dfs, alpha=0.5, figsize=(6, 6), color=cc)
    #
    # plt.show()
    # plt.figure(1)
    # plt.subplot(1, 4, 1)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='angle', y='s1', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # plt.subplot(1, 4, 2)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='angle', y='w1', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # plt.subplot(1, 4, 3)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='angle', y='s2', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # plt.subplot(1, 4, 4)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='angle', y='w2', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # # Drawing the side color bar
    # normalize = mcolors.Normalize(vmin=dfs['median'].min(), vmax=dfs['median'].max())
    # colormap = cm.ocean
    #
    # for n in dfs['median']:
    #     plt.plot(color=colormap(normalize(n)))
    #
    # scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
    # scalarmappaple.set_array(dfs['median'])
    # plt.colorbar(scalarmappaple)
    #
    # # grouped = dfs[['angle', 's1', 'median']].groupby('angle')
    # # grouped.aggregate(np.mean)
    # plt.figure(2)
    # plt.subplot(1, 3, 1)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='s1', y='w2', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # plt.subplot(1, 3, 2)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='s1', y='w1', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # plt.subplot(1, 3, 3)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='s1', y='s2', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    #
    # # Drawing the side color bar
    # normalize = mcolors.Normalize(vmin=dfs['median'].min(), vmax=dfs['median'].max())
    # colormap = cm.ocean
    #
    # for n in dfs['median']:
    #     plt.plot(color=colormap(normalize(n)))
    #
    # scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
    # scalarmappaple.set_array(dfs['median'])
    # plt.colorbar(scalarmappaple)
    #
    # plt.figure(3)
    # plt.subplot(1, 2, 1)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='s2', y='w2', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # plt.subplot(1, 2, 2)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='s2', y='w1', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # # Drawing the side color bar
    # normalize = mcolors.Normalize(vmin=dfs['median'].min(), vmax=dfs['median'].max())
    # colormap = cm.ocean
    #
    # for n in dfs['median']:
    #     plt.plot(color=colormap(normalize(n)))
    #
    # scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
    # scalarmappaple.set_array(dfs['median'])
    # plt.colorbar(scalarmappaple)
    #
    # plt.figure(4)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='w1', y='w2', data=dfs, jitter=True, edgecolor='none', hue="median", alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # # Drawing the side color bar
    # normalize = mcolors.Normalize(vmin=dfs['median'].min(), vmax=dfs['median'].max())
    # colormap = cm.ocean
    #
    # for n in dfs['median']:
    #     plt.plot(color=colormap(normalize(n)))
    #
    # scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
    # scalarmappaple.set_array(dfs['median'])
    # plt.colorbar(scalarmappaple)
    #
    #
    # plt.figure(5)
    # plt.subplot(5, 1, 1)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='median', y='s1', data=dfs, jitter=True, edgecolor='none', alpha=.40)
    # sns.despine()
    #
    # plt.subplot(5, 1, 2)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='median', y='w1', data=dfs, jitter=True, edgecolor='none', alpha=.40)
    # sns.despine()
    #
    # plt.subplot(5, 1, 3)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='median', y='s2', data=dfs, jitter=True, edgecolor='none', alpha=.40)
    # sns.despine()
    #
    # plt.subplot(5, 1, 4)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='median', y='w2', data=dfs, jitter=True, edgecolor='none', alpha=.40)
    # sns.despine()
    #
    # plt.subplot(5, 1, 5)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='median', y='angle', data=dfs, jitter=True, edgecolor='none', alpha=.40)
    # sns.despine()

    # plt.show()


# main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    logging.debug("Starting Program")
    # result = None

    nameExperiemnt = "PacmanDistance"
    path = "/Users/alessandrozonta/Documents/ResultsExp/latest/china/" + nameExperiemnt
    compute(nameExperiemnt, path)

    # nameExperiemnt = "PacmanDistance"
    # path = "/Users/alessandrozonta/Documents/Results Exp/250/" + nameExperiemnt
    # compute(nameExperiemnt, path)

    logging.debug("End Program")
