# read folder
import filecmp
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import logging
import seaborn as sns
import numpy
from pandas import DataFrame

dict = {'PacmanDistance': 'DE', 'PacmanDistancePF': 'DEA', 'PacmanNormal': 'NE', 'PacmanNormalPF': 'NEA',
        'PacmanDistancePath': 'DP', 'PacmanDistancePathPF': 'DPA', 'PacmanNormalPath': 'NP',
        'PacmanNormalPathPF': 'NPA', 'PacmanNormalPath2': 'Normal_Path_Correct',
        'PacmanNormalPFOld': 'Normal_Path_Wrong'
    , 'PacmanNormalChina': 'Normal_China', 'PacmanNormalPFChina': 'Normal_APF_China'}

dict2 = {'PacmanDistance': 'Distance', 'PacmanDistancePF': 'Distance_APF', 'PacmanNormal': 'Normal',
         'PacmanNormalPF': ' Normal_APF',
         'PacmanDistancePath': 'Path_Distance', 'PacmanDistancePathPF': 'Path_Distance_APF',
         'PacmanNormalPath': 'Normal_Path',
         'PacmanNormalPathPF': 'Normal_Path_APF'}

accepted = ['PacmanDistance']


def loadOtherFile(path, nameExp):
    listLenght = []
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


def computeGeneral(subpath, secondsubpath, total_number_parameter_file):
    directories = os.listdir(subpath)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    for x in range(total_number_parameter_file + 1):
        pp = "p" + str(x)
        if pp in directories:
            directories.remove(pp)
    totalTop = []
    # totalTop5 = []
    # totalTop10 = []
    # totalPerf = []
    totalLength = []
    version = []
    for el in directories:
        if el in accepted:
            nameExp = el.replace("Output", "")
            path = subpath + nameExp
            listLength, numberPoi, top5, top10, top, perf = loadOtherFile(path, nameExp)
            totalTop.append(top)
            # totalTop5.append(top5)
            # totalTop10.append(top10)
            # totalPerf.append(perf)
            totalLength.append(listLength)
            version.append("old")

    nameGraph = []
    for x in range(0, len(directories)):
        if directories[x] in accepted:
            nameGraph.append(dict[directories[x].replace("Output", "")])

    # second experiment
    directories = os.listdir(secondsubpath)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    for x in range(total_number_parameter_file + 1):
        pp = "p" + str(x)
        if pp in directories:
            directories.remove(pp)
    for el in directories:
        nameExp = el.replace("Output", "")
        if nameExp in accepted:
            path = secondsubpath + "Output" + nameExp
            listLength, numberPoi, top5, top10, top, perf = loadOtherFile(path, nameExp)
            totalTop.append(top)
            # totalTop5.append(top5)
            # totalTop10.append(top10)
            # totalPerf.append(perf)
            totalLength.append(listLength)
            version.append("new")

    for x in range(0, len(directories)):
        nameGraph.append(dict[directories[x].replace("Output", "")])

    totalNewMeasure = []
    for x in range(len(totalLength)):
        newMeasure = []
        for y in range(len(totalLength[x])):
            newNewMeasure = []
            for z in range(len(totalLength[x][y])):
                newNewMeasure.append((100 * totalTop[x][y][z]) / totalLength[x][y][z])
            newMeasure.append(np.median(newNewMeasure))
        totalNewMeasure.append(newMeasure)

    xx = np.arange(1, len(totalNewMeasure) + 1)
    dataVector = []
    dataNameVector = []
    dataTipologyVector = []
    for x in range(len(totalNewMeasure)):
        name = nameGraph[x]
        tipo = version[x]
        for y in range(len(totalNewMeasure[x])):
            dataVector.append(totalNewMeasure[x][y])
            dataNameVector.append(name)
            dataTipologyVector.append(tipo)

    zz = {"Percentage before the end": dataVector, "Rules": dataNameVector, "Dataset": dataTipologyVector}
    dfs = DataFrame(data=zz)
    dfs.to_csv("geos.csv")


    sns.set(font_scale=1.5)
    sns.boxplot(x="Percentage before the end", y="Rules", hue="Dataset", data=dfs, palette="PRGn")
    sns.stripplot(x="Percentage before the end", y="Rules", data=dfs,
                  jitter=True, size=3, color=".3", linewidth=0, hue="Dataset", palette=sns.diverging_palette(10, 220, sep=80, n=7))

    # sns.despine(offset=10, trim=True)
    # sns.stripplot(x="data", y="name", data=dfs,
    #               jitter=True, size=3, color=".3", linewidth=0)

    sns.despine(trim=True)
    # plt.figure(1)
    # plt.boxplot(totalNewMeasure, whis=50)
    # x = np.arange(1, len(nameGraph) + 1)
    # plt.xticks(x, nameGraph, rotation=90)
    # plt.ylabel("Percentage before the end of the tracking path")
    # plt.xlim(-1, 25)
    # plt.figure(2)
    # for el in totalPerf:
    #     x = np.arange(len(el))
    #     plt.scatter(x, el)

    plt.show()


# main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None

    computeGeneral("/Users/alessandrozonta/Documents/ResultsExp/latest/china/",
                   "/Volumes/TheMaze/Results/ratio_results/geoset/", 23)
    # computeGeneral("/Users/alessandrozonta/Documents/ResultsExp/latest/idsa/",
    #                "/Volumes/TheMaze/Results/ratio_results/idsa/", 23)

    logging.debug("End Program")
