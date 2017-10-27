import logging
import os
import numpy as np
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt


dict = {0: "P_Distance", 1: "P_Distance_APF", 2: "P_Normal", 3: "P_Normal_APF"}
dict2 = {0: "P_Distance", 1: "P_Normal", 2: "P_Normal", 3: "P_Normal_APF"}
dict3 = {0: "P_Distance", 1: "P_Normal"}

def loadOtherFile(path, nameExp):
    nameExp = nameExp.replace("Output","")
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


def readParameters(path, nameExp, total_number_parameter_file):
    nameExp = nameExp.replace("Output", "")
    listRules = []
    for x in range(total_number_parameter_file):
        pathFastRead = path + "p" + str(x)
        with open(pathFastRead) as f:
            for content in f:
                value = content.split(" ")
                if value[5] == nameExp:
                    listRules.append(value)
    return listRules


def computeGeneral(subpath):
    directories = os.listdir(subpath)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    if "p0" in directories:
        directories.remove("p0")
    totalTop = []
    totalLength = []
    rules = []
    for el in directories:
        path = subpath + el
        nameExp = el
        listLength, numberPoi, top5, top10, top, perf = loadOtherFile(path, nameExp)
        totalTop.append(top)
        totalLength.append(listLength)
        rules.append(readParameters(subpath, nameExp))

    total_percentage = []
    for x in range(len(totalTop)):
        percentage = []
        for y in range(len(totalTop[x])):
            newNewMeasure = []
            for z in range(len(totalTop[x][y])):
                newNewMeasure.append((100 * totalTop[x][y][z]) / totalLength[x][y][z])
            percentage.append(np.median(newNewMeasure))
        total_percentage.append(percentage)

    h = []
    z1 = []
    z2 = []
    result_value = []
    rules_value = []
    for x in range(len(total_percentage)):
        for y in range(len(total_percentage[x])):
            h.append(float(rules[x][y][0]))
            z1.append(float(rules[x][y][1]))
            z2.append(float(rules[x][y][2]))
            result_value.append(total_percentage[x][y])
            rules_value.append(x)

    h_1 = []
    z1_1 = []
    z2_1 = []
    result_value_1 = []
    rules_value_1 = []
    for x in range(len(z2)):
        if z2[x] == 0.01:
            h_1.append(h[x])
            z1_1.append(z1[x])
            z2_1.append(z2[x])
            result_value_1.append(result_value[x])
            rules_value_1.append(rules_value[x])

    h_2 = []
    z1_2 = []
    z2_2 = []
    result_value_2 = []
    rules_value_2 = []
    for x in range(len(z2)):
        if z2[x] == 0.1:
            h_2.append(h[x])
            z1_2.append(z1[x])
            z2_2.append(z2[x])
            result_value_2.append(result_value[x])
            rules_value_2.append(rules_value[x])

    h_3 = []
    z1_3 = []
    z2_3 = []
    result_value_3 = []
    rules_value_3 = []
    for x in range(len(z2)):
        if z2[x] == 0.2:
            h_3.append(h[x])
            z1_3.append(z1[x])
            z2_3.append(z2[x])
            result_value_3.append(result_value[x])
            rules_value_3.append(rules_value[x])

    h_4 = []
    z1_4 = []
    z2_4 = []
    result_value_4 = []
    rules_value_4 = []
    for x in range(len(z2)):
        if z2[x] == 0.5:
            h_4.append(h[x])
            z1_4.append(z1[x])
            z2_4.append(z2[x])
            result_value_4.append(result_value[x])
            rules_value_4.append(rules_value[x])

    # zz = {"h": h_1, "z1": z1_1, "z2": z2_1, "Performance": result_value_1, "Rules": rules_value_1}
    # dfs = DataFrame(data=zz)
    # sns.lmplot("z1", "Performance", hue="Rules", data=dfs)
    # sns.despine(trim=True)
    # plt.ylim(-2,10)
    #
    # zz = {"h": h_2, "z1": z1_2, "z2": z2_2, "Performance": result_value_2, "Rules": rules_value_2}
    # dfs = DataFrame(data=zz)
    # sns.lmplot("z1", "Performance", hue="Rules", data=dfs)
    # sns.despine(trim=True)
    # plt.ylim(-2, 10)
    #
    # zz = {"h": h_3, "z1": z1_3, "z2": z2_3, "Performance": result_value_3, "Rules": rules_value_3}
    # dfs = DataFrame(data=zz)
    # sns.lmplot("z1", "Performance", hue="Rules", data=dfs)
    # sns.despine(trim=True)
    # plt.ylim(-2, 10)
    #
    # zz = {"h": h_4, "z1": z1_4, "z2": z2_4, "Performance": result_value_4, "Rules": rules_value_4}
    # dfs = DataFrame(data=zz)
    # sns.lmplot("z1", "Performance", hue="Rules", data=dfs)
    # sns.despine(trim=True)
    # plt.ylim(-2, 10)
    #
    zz = {"h": h, "z1": z1, "z2": z2, "Performance": result_value, "Rules": rules_value}
    dfs = DataFrame(data=zz)
    # dfs.to_csv("idsa_rule.csv")

    sns.lmplot("z1", "Performance", hue="h", data=dfs)
    sns.despine(trim=True)

    plt.show()


def computeBoth(idsa, geolife, total_number_parameter_file):
    logging.debug("Elaborating -> " + idsa)
    directories = os.listdir(idsa)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    for x in range(total_number_parameter_file + 1):
        pp = "p" + str(x)
        if pp in directories:
            directories.remove(pp)
    totalTop = []
    totalLength = []
    rules = []
    for el in directories:
        path = idsa + el
        nameExp = el
        listLength, numberPoi, top5, top10, top, perf = loadOtherFile(path, nameExp)
        totalTop.append(top)
        totalLength.append(listLength)
        rules.append(readParameters(idsa, nameExp, total_number_parameter_file))

    total_percentage = []
    for x in range(len(totalTop)):
        percentage = []
        for y in range(len(totalTop[x])):
            newNewMeasure = []
            for z in range(len(totalTop[x][y])):
                newNewMeasure.append((100 * totalTop[x][y][z]) / totalLength[x][y][z])
            percentage.append(np.median(newNewMeasure))
        total_percentage.append(percentage)

    h = []
    z1 = []
    z2 = []
    s2 = []
    w2 = []
    rapp = []
    result_value = []
    rules_value = []
    dataset = []
    for x in range(len(total_percentage)):
        for y in range(len(total_percentage[x])):
            h.append(float(rules[x][y][0]))
            z1.append(float(rules[x][y][1]))
            z2.append(float(rules[x][y][2]))
            s2.append(float(rules[x][y][3]))
            w2.append(float(rules[x][y][4]))
            rapp.append(float(rules[x][y][1]) / float(rules[x][y][2]))
            result_value.append(total_percentage[x][y])
            rules_value.append(dict3[x])
            dataset.append("IDSA")

    logging.debug("Elaborating -> " + geolife)
    directories = os.listdir(geolife)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    for x in range(total_number_parameter_file + 1):
        pp = "p" + str(x)
        if pp in directories:
            directories.remove(pp)
    totalTop = []
    totalLength = []
    rules = []
    for el in directories:
        path = geolife + el
        nameExp = el
        listLength, numberPoi, top5, top10, top, perf = loadOtherFile(path, nameExp)
        totalTop.append(top)
        totalLength.append(listLength)
        rules.append(readParameters(geolife, nameExp, total_number_parameter_file))

    total_percentage = []
    for x in range(len(totalTop)):
        percentage = []
        for y in range(len(totalTop[x])):
            newNewMeasure = []
            for z in range(len(totalTop[x][y])):
                newNewMeasure.append((100 * totalTop[x][y][z]) / totalLength[x][y][z])
            percentage.append(np.median(newNewMeasure))
        total_percentage.append(percentage)

    for x in range(len(total_percentage)):
        for y in range(len(total_percentage[x])):
            h.append(float(rules[x][y][0]))
            z1.append(float(rules[x][y][1]))
            z2.append(float(rules[x][y][2]))
            s2.append(float(rules[x][y][3]))
            w2.append(float(rules[x][y][4]))
            rapp.append(float(rules[x][y][1]) / float(rules[x][y][2]))
            result_value.append(total_percentage[x][y])
            rules_value.append(dict3[x])
            dataset.append("Geolife")

    z2_section = []
    for el in z2:
        if el < 0.5:
            z2_section.append("0.01-0.05")
        elif el < 4.01:
            z2_section.append("2.01-4.01")
        elif el < 6.01:
            z2_section.append("4.01-6.01")
        elif el < 8.01:
            z2_section.append("6.01-8.01")
        elif el < 10.01:
            z2_section.append("8.01-10")


    zz = {"h": h, "z1": z1, "z2": z2, "Performance": result_value, "Rules": rules_value, "Dataset": dataset, "z1/z2": rapp, "slice":z2_section, "w2": w2, "s2": s2}
    dfs = DataFrame(data=zz)
    dfs.to_csv("500.csv")

    # z2_sub = dfs[dfs["z1"] == 0.01]
    # sns.lmplot("h", "Performance", hue="Dataset", data=z2_sub)
    # sns.despine(trim=True)
    #
    # z2_sub = dfs[dfs["z1"] == 0.1]
    # sns.lmplot("h", "Performance", hue="Dataset", data=z2_sub)
    # sns.despine(trim=True)
    #
    # z2_sub = dfs[dfs["z1"] == 0.2]
    # sns.lmplot("h", "Performance", hue="Dataset", data=z2_sub)
    # sns.despine(trim=True)
    #
    # z2_sub = dfs[dfs["z1"] == 0.5]
    # sns.lmplot("h", "Performance", hue="Dataset", data=z2_sub)
    # sns.despine(trim=True)

    # idsa_sub = dfs[dfs["Dataset"] == "IDSA"]
    # idsa_sub_2 = idsa_sub[idsa_sub["z1/z2"] <= 1.0]

    # a = dfs[dfs["Dataset"] == "Geolife"]
    # b = a[a["z1/z2"] <= 0.1]
    # b.to_csv("both.csv")
    # sns.color_palette("Blues")
    # sns.lmplot("z1", "z2", data=b, x_jitter=0.5, fit_reg=False)
    #
    # sns.despine(trim=True)
    #
    # plt.show()
    # sns.lmplot("Performance", "Rules", data=dfs)
    # sns.despine(trim=True)

    # subpartz2 = dfs[dfs["slice"] == "0.01-0.05"]
    # subpartz2disatnce = subpartz2[subpartz2["Rules"] == "P_Distance"]
    #
    # sns.lmplot(x="z1", y="Performance", hue="Dataset", data=subpartz2disatnce, fit_reg=False)
    # plt.ylim(0, 35)

    sns.boxplot(x="Performance", y="Rules", hue="Dataset", data=dfs, palette="PRGn")
    # sns.stripplot(x="Performance", y="Rules", data=dfs,
    #               jitter=True, size=3, color=".3", linewidth=0,
    #               palette=sns.diverging_palette(10, 220, sep=80, n=7))

    # sns.despine(offset=10, trim=True)
    # sns.stripplot(x="data", y="name", data=dfs,
    #               jitter=True, size=3, color=".3", linewidth=0)

    sns.despine(trim=True)

    plt.show()


def merge():
    idsa = "/Users/alessandrozonta/Documents/ResultsExp/newangle/idsa/"
    geoset = "/Users/alessandrozonta/Documents/ResultsExp/newangle/geoset/"

    directories = os.listdir(idsa)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    if "p0" in directories:
        directories.remove("p0")
    totalTop = []
    totalLength = []
    rules = []
    for el in directories:
        path = idsa + el
        nameExp = el
        listLength, numberPoi, top5, top10, top, perf = loadOtherFile(path, nameExp)
        totalTop.append(top)
        totalLength.append(listLength)
        rules.append(readParameters(idsa, nameExp))

    directories = os.listdir(geoset)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    if "p0" in directories:
        directories.remove("p0")
    for el in directories:
        path = geoset + el
        nameExp = el
        listLength, numberPoi, top5, top10, top, perf = loadOtherFile(path, nameExp)
        totalTop.append(top)
        totalLength.append(listLength)
        rules.append(readParameters(geoset, nameExp))

    total_percentage = []
    for x in range(len(totalTop)):
        percentage = []
        for y in range(len(totalTop[x])):
            newNewMeasure = []
            for z in range(len(totalTop[x][y])):
                newNewMeasure.append((100 * totalTop[x][y][z]) / totalLength[x][y][z])
            percentage.append(np.median(newNewMeasure))
        total_percentage.append(percentage)

    h = []
    z1 = []
    z2 = []
    s2 = []
    w2 = []
    result_value = []
    rules_value = []
    dataset = []
    for x in range(len(total_percentage)):
        for y in range(len(total_percentage[x])):
            h.append(float(rules[x][y][0]))
            z1.append(float(rules[x][y][1]))
            z2.append(float(rules[x][y][2]))
            s2.append(float(rules[x][y][3]))
            w2.append(float(rules[x][y][4]))

            result_value.append(total_percentage[x][y])
            rules_value.append(x)
            if x < 4:
                dataset.append("idsa")
            else:
                dataset.append("Geosat")

    zz = {"h": h, "z1": z1, "z2": z2, "Performance": result_value, "Rules": rules_value, "s2": s2, "w2": w2,
          "Dataset": dataset}
    dfs = DataFrame(data=zz)
    # dfs.to_csv("total_two.csv")



if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None

    # computeGeneral("/Users/alessandrozonta/Documents/ResultsExp/latest/china/",
    #                "/Volumes/TheMaze/Results/newangle/geoset/")
    # computeGeneral("/Users/alessandrozonta/Documents/ResultsExp/newangle/idsa/")
    # merge()

    computeBoth(idsa="/Users/alessandrozonta/Documents/ResultsExp/newangle/500/idsa/",
                geolife="/Users/alessandrozonta/Documents/ResultsExp/newangle/500/geoset/", total_number_parameter_file=1)

    logging.debug("End Program")
