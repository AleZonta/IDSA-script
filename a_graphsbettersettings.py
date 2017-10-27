# import logging
import matplotlib.pyplot as plt
import numpy as np


import numpy
from pandas import DataFrame
from pandas import scatter_matrix
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from sklearn.decomposition import PCA

from pandas.tools.plotting import parallel_coordinates
from sklearn.preprocessing import StandardScaler


def loadOtherFile(path, name):
    # logging.debug("Reading files of {}".format(name))
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

    return first

def par(china, idsa):
    # substract average and divide by sd -> normalized median
    dataset = []
    medianchina = []
    realTopchina = []
    for x in range(len(china[1])):
        appo = []
        try:
            for y in range(len(china[1][x])):
                appo.append((100 * china[1][x][y]) / china[2][x][y])
        except:
            pass
        realTopchina.append(appo)
    for el in realTopchina:
        medianchina.append(np.median(el))
        dataset.append("Geolife")

    realmedia = []
    average = np.average(medianchina)
    std = np.std(medianchina)
    for el in medianchina:
        realmedia.append((el - average) / std)


    medianidsa = []
    realTopidsa = []
    for x in range(len(idsa[1])):
        appo = []
        try:
            for y in range(len(idsa[1][x])):
                appo.append((100 * idsa[1][x][y]) / idsa[2][x][y])
        except:
            pass
        realTopidsa.append(appo)
    for el in realTopidsa:
        medianidsa.append(np.median(el))
        dataset.append("IDSA")

    average = np.average(medianidsa)
    std = np.std(medianidsa)
    for el in medianidsa:
        realmedia.append((el - average) / std)

    angle = []
    s1 = []
    w1 = []
    s2 = []
    w2 = []
    for el in china[0]:
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

    for el in china[0]:
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

    zz = {"angle": angle, "s1": s1, "s2": s2, "w1": w1, "w2": w2, "median": realmedia, "dataset": dataset}


    #w1=0.005
    ind0005 = []
    for x in range(len(w1)):
        if w1[x] == 0.005:
            ind0005.append(x)
    subangle = np.take(angle, ind0005)
    subs1 = np.take(s1, ind0005)
    subs2 = np.take(s2, ind0005)
    subw1 = np.take(w1, ind0005)
    subw2 = np.take(w2, ind0005)
    submedia = np.take(realmedia, ind0005)
    subdataset = np.take(dataset, ind0005)
    # w2=0.1
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.1:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(1)
    # plt.subplot(331)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias, "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.005 | w2 = 0.1')
    # ax.xaxis.set_visible(False)
    plt.ylim(-2.5, 2.5)
    plt.ylabel("Normalised percentage before the end")
    sns.despine(offset=10, trim=True)

    # w2=0.25
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.25:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(2)
    # plt.subplot(332)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias,
           "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.005 | w2 = 0.25')
    plt.ylabel("Normalised percentage before the end")
    # ax.xaxis.set_visible(False)
    # ax.yaxis.set_visible(False)

    plt.ylim(-2.5, 2.5)
    sns.despine(offset=10, trim=True)

    # w2=0.5
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.5:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(3)
    # plt.subplot(333)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias,
           "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.005 | w2 = 0.5')
    # ax.xaxis.set_visible(False)
    # ax.yaxis.set_visible(False)
    plt.ylabel("Normalised Performance")
    plt.ylim(-2.5,2.5)
    sns.despine(offset=10, trim=True)

    # -------------------------------------------------------------------------------
    # w1=0.01
    ind0005 = []
    for x in range(len(w1)):
        if w1[x] == 0.01:
            ind0005.append(x)
    subangle = np.take(angle, ind0005)
    subs1 = np.take(s1, ind0005)
    subs2 = np.take(s2, ind0005)
    subw1 = np.take(w1, ind0005)
    subw2 = np.take(w2, ind0005)
    submedia = np.take(realmedia, ind0005)
    subdataset = np.take(dataset, ind0005)
    # w2=0.1
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.1:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(4)
    # plt.subplot(334)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias,
           "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.01 | w2 = 0.1')
    # ax.xaxis.set_visible(False)
    plt.ylim(-2.5, 2.5)
    plt.ylabel("Normalised percentage before the end")
    sns.despine(offset=10, trim=True)

    # w2=0.25
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.25:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(5)
    # plt.subplot(335)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias,
           "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.01 | w2 = 0.25')
    # ax.xaxis.set_visible(False)
    # ax.yaxis.set_visible(False)
    plt.ylabel("Normalised percentage before the end")
    plt.ylim(-2.5, 2.5)
    sns.despine(offset=10, trim=True)

    # w2=0.5
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.5:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(6)
    # plt.subplot(336)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias,
           "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.01 | w2 = 0.5')
    # ax.xaxis.set_visible(False)
    # ax.yaxis.set_visible(False)
    plt.ylabel("Normalised percentage before the end")
    plt.ylim(-2.5, 2.5)
    sns.despine(offset=10, trim=True)

    # -------------------------------------------------------------------------------
    # w1=0.02
    ind0005 = []
    for x in range(len(w1)):
        if w1[x] == 0.02:
            ind0005.append(x)
    subangle = np.take(angle, ind0005)
    subs1 = np.take(s1, ind0005)
    subs2 = np.take(s2, ind0005)
    subw1 = np.take(w1, ind0005)
    subw2 = np.take(w2, ind0005)
    submedia = np.take(realmedia, ind0005)
    subdataset = np.take(dataset, ind0005)
    # w2=0.1
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.1:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(7)
    # plt.subplot(337)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias,
           "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.02 | w2 = 0.1')
    plt.ylabel("Normalised percentage before the end")
    plt.ylim(-2.5, 2.5)
    sns.despine(offset=10, trim=True)

    # w2=0.25
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.25:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(8)
    # plt.subplot(338)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias,
           "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.02 | w2 = 0.25')
    # ax.yaxis.set_visible(False)
    plt.ylabel("Normalised percentage before the end")

    plt.ylim(-2.5, 2.5)
    sns.despine(offset=10, trim=True)

    # w2=0.5
    ind01 = []
    for x in range(len(subw2)):
        if subw2[x] == 0.5:
            ind01.append(x)
    subangles = np.take(subangle, ind01)
    subs1s = np.take(subs1, ind01)
    subs2s = np.take(subs2, ind01)
    subw1s = np.take(subw1, ind01)
    subw2s = np.take(subw2, ind01)
    submedias = np.take(submedia, ind01)
    subdatasets = np.take(subdataset, ind01)

    plt.figure(9)
    # plt.subplot(339)
    zzz = {"angle": subangles, "s1": subs1s, "s2": subs2s, "w1": subw1s, "w2": subw2s, "median": submedias,
           "dataset": subdatasets}
    df = DataFrame(data=zzz)
    sns.set(font_scale=1.5)
    ax = sns.boxplot(x="angle", y="median", hue="dataset", data=df, palette="PRGn")
    # ax.yaxis.set_visible(False)
    plt.ylabel("Normalised percentage before the end")
    # remove legend from axis 'ax'
    sns.plt.title('w1 = 0.02 | w2 = 0.5')
    plt.ylim(-2.5, 2.5)
    sns.despine(offset=10, trim=True)

    # plt.figure(1)
    # # # df = DataFrame(data=yy)
    # dfs = DataFrame(data=zz)
    # # dfs.to_csv('test4.csv')
    # g = sns.FacetGrid(dfs, row="w1", col="w2", hue="dataset")
    # g.map(sns.boxplot, "angle", "median")
    # # g = sns.PairGrid(dfs, vars=["angle", "s1", "s2", "w1", "w2"])
    # # # g.map(plt.scatter, s=sizes)
    # # # g.map_diag(plt.hist)
    # # g.map(sns.stripplot, jitter=0.45, hue=medianchina)
    # # # plt.show()

    plt.show()


# main
if __name__ == "__main__":
    # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # logging.debug("Starting Program")
    # result = None

    nameExperiemnt = "PacmanDistance"
    path = "/Users/alessandrozonta/Documents/ResultsExp/latest/china/" + nameExperiemnt
    china = compute(nameExperiemnt, path)

    nameExperiemnt = "PacmanDistance"
    path = "/Users/alessandrozonta/Documents/ResultsExp/latest/idsa/" + nameExperiemnt
    idsa = compute(nameExperiemnt, path)

    par(china, idsa)


    # logging.debug("End Program")