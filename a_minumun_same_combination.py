import logging
import os
import numpy as np

from pandas import DataFrame


def loadOtherFile(path, nameExp):
    nameExp = nameExp.replace("Output", "")
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
    pathFastRead = path + "p0"
    for x in range(0, total_number_parameter_file):
        pathFastRead = path + "p" + str(x)
        with open(pathFastRead) as f:
            for content in f:
                value = content.split(" ")
                if value[5] == nameExp:
                    listRules.append(value)
    return listRules


def merge(old, total_number_parameter_file):
    if old:
        logging.debug("Which setting am I checking? -> Old Version ")
    else:
        logging.debug("Which setting am I checking? -> New Angle")
    idsa = "/Volumes/TheMaze/Results/ratio_results/idsa/"
    if old:
        idsa = "/Users/alessandrozonta/Documents/ResultsExp/latest/idsa/"
    geoset = "/Volumes/TheMaze/Results/ratio_results/geoset/"
    if old:
        geoset = "/Users/alessandrozonta/Documents/ResultsExp/latest/china/"

    directories = os.listdir(idsa)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    for x in range(0, total_number_parameter_file + 1):
        pp = "p" + str(x)
        if pp in directories:
            directories.remove(pp)
    if old:
        directories = ["PacmanDistance"]
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

    directories = os.listdir(geoset)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    if "elaborate.py" in directories:
        directories.remove("elaborate.py")
    for x in range(0, total_number_parameter_file + 1):
        pp = "p" + str(x)
        if pp in directories:
            directories.remove(pp)
    if old:
        directories = ["PacmanDistance"]
    for el in directories:
        path = geoset + el
        nameExp = el
        listLength, numberPoi, top5, top10, top, perf = loadOtherFile(path, nameExp)
        totalTop.append(top)
        totalLength.append(listLength)
        rules.append(readParameters(geoset, nameExp, total_number_parameter_file))

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
    pos = []
    name = []
    for x in range(len(total_percentage)):
        for y in range(len(total_percentage[x])):
            h.append(float(rules[x][y][0]))
            z1.append(float(rules[x][y][1]))
            z2.append(float(rules[x][y][2]))
            s2.append(float(rules[x][y][3]))
            w2.append(float(rules[x][y][4]))
            pos.append(float(rules[x][y][6]))
            name.append(rules[x][y][5])
            result_value.append(total_percentage[x][y])
            if x > 2:
                z = x - 4
                rules_value.append(z)
            else:
                rules_value.append(x)
            if old:
                if x < 1:
                    dataset.append("idsa")
                else:
                    dataset.append("Geosat")
            else:
                if x < 2: # <----------------------------------------------------- be careful about this parameter
                    dataset.append("idsa")
                else:
                    dataset.append("Geosat")

    zz = {"h": h, "z1": z1, "z2": z2, "Performance": result_value, "Rules": rules_value, "s2": s2, "w2": w2,
          "Dataset": dataset, "Position": pos, "Name": name}
    dfs = DataFrame(data=zz)

    dfs = dfs[dfs["Name"] != "PacmanDistancePF"]
    dfs = dfs[dfs["Name"] != "PacmanNormalPF"]

    idsa_section = dfs[dfs["Dataset"] == "idsa"]
    idsa_ordered = idsa_section.sort_values(by=["Performance"], ascending=[False])
    print("Best setting for idsa")
    print("first->")
    print idsa_ordered.iloc[0]
    print("second->")
    print idsa_ordered.iloc[1]
    print("third->")
    print idsa_ordered.iloc[2]
    print("fourth->")
    print idsa_ordered.iloc[3]
    print("fifth->")
    print idsa_ordered.iloc[4]
    print("----------------------------------------")
    print("Worst setting for idsa")
    print("first->")
    print idsa_ordered.iloc[len(idsa_ordered)-1]
    print("second->")
    print idsa_ordered.iloc[len(idsa_ordered)-2]
    print("third->")
    print idsa_ordered.iloc[len(idsa_ordered)-3]
    print("fourth->")
    print idsa_ordered.iloc[len(idsa_ordered)-4]
    print("fifth->")
    print idsa_ordered.iloc[len(idsa_ordered)-5]
    print("----------------------------------------")
    print("----------------------------------------")
    print("----------------------------------------")
    print("----------------------------------------")
    geosat_section = dfs[dfs["Dataset"] == "Geosat"]
    geosat_ordered = geosat_section.sort_values(by=["Performance"], ascending=[False])
    print("Best setting for geosat")
    print("first->")
    print geosat_ordered.iloc[0]
    print("second->")
    print geosat_ordered.iloc[1]
    print("third->")
    print geosat_ordered.iloc[2]
    print("fourth->")
    print geosat_ordered.iloc[3]
    print("fifth->")
    print geosat_ordered.iloc[4]
    print("----------------------------------------")
    print("Worst setting for geosat")
    print("first->")
    print geosat_ordered.iloc[len(idsa_ordered) - 1]
    print("second->")
    print geosat_ordered.iloc[len(idsa_ordered) - 2]
    print("third->")
    print geosat_ordered.iloc[len(idsa_ordered) - 3]
    print("fourth->")
    print geosat_ordered.iloc[len(idsa_ordered) - 4]
    print("fifth->")
    print geosat_ordered.iloc[len(idsa_ordered) - 5]

    # print geosat_ordered.iloc[3]
    # # df.loc[(df['column_name'] == some_value) & df['other_column'].isin(some_values)]
    # #
    # print idsa_ordered.iloc[list(np.where((idsa_ordered["h"] == geosat_ordered.iloc[3]["h"]) & (
    #                                             idsa_ordered["s2"] == geosat_ordered.iloc[3]["s2"]) & (
    #                                             idsa_ordered["w2"] == geosat_ordered.iloc[3]["w2"]) & (
    #                                             idsa_ordered["z1"] == geosat_ordered.iloc[3]["z1"]) & (
    #                                             idsa_ordered["z2"] == geosat_ordered.iloc[3]["z2"]))[0])[0]]
    # print idsa_ordered.loc[(idsa_ordered["Rules"] == geosat_ordered.iloc[0]["Rules"]) & (
    #                         idsa_ordered["h"] == geosat_ordered.iloc[0]["h"]) & (
    #                        idsa_ordered["s2"] == geosat_ordered.iloc[0]["s2"]) & (
    #                        idsa_ordered["w2"] == geosat_ordered.iloc[0]["w2"]) & (
    #                        idsa_ordered["z1"] == geosat_ordered.iloc[0]["z1"]) & (
    #                        idsa_ordered["z2"] == geosat_ordered.iloc[0]["z2"])]
    print("---------")
    print("Best setting for both dataset and also distance variable")

    # tuple_list = []
    # for x in range(len(geosat_ordered)):
    #     tuple_list.append((x, list(np.where((idsa_ordered["h"] == geosat_ordered.iloc[x]["h"]) & (
    #                                             idsa_ordered["s2"] == geosat_ordered.iloc[x]["s2"]) & (
    #                                             idsa_ordered["w2"] == geosat_ordered.iloc[x]["w2"]) & (
    #                                             idsa_ordered["z1"] == geosat_ordered.iloc[x]["z1"]) & (
    #                                             idsa_ordered["z2"] == geosat_ordered.iloc[x]["z2"]))[0])[0]))
    # winner = min(tuple_list, key=lambda t: t[1])
    winner_idsa = idsa_ordered.iloc[0]

    id = list(np.where((geosat_ordered["s2"] == idsa_ordered.iloc[0]["s2"]) & (
        geosat_ordered["w2"] == idsa_ordered.iloc[0]["w2"]) & (
        geosat_ordered["z1"] == idsa_ordered.iloc[0]["z1"]) & (
        geosat_ordered["z2"] == idsa_ordered.iloc[0]["z2"]))[0])

    winner_geosat = geosat_ordered.iloc[id]

    # print geosat_ordered.iloc[winner[0]]
    # print idsa_ordered.iloc[winner[1]]
    print winner_geosat.iloc[0]
    print winner_idsa

    print("---------")
    print("Best setting for both dataset ")

    # tuple_list = []
    # for x in range(len(geosat_ordered)):
    #     tuple_list.append((x, list(np.where((idsa_ordered["h"] == geosat_ordered.iloc[x]["h"]) & (
    #                                             idsa_ordered["s2"] == geosat_ordered.iloc[x]["s2"]) & (
    #                                             idsa_ordered["w2"] == geosat_ordered.iloc[x]["w2"]) & (
    #                                             idsa_ordered["z1"] == geosat_ordered.iloc[x]["z1"]) & (
    #                                             idsa_ordered["z2"] == geosat_ordered.iloc[x]["z2"]))[0])[0]))
    # winner = min(tuple_list, key=lambda t: t[1])
    winner_idsa = idsa_ordered.iloc[0]

    id = list(np.where((geosat_ordered["z1"] == idsa_ordered.iloc[0]["z1"]) & (
                           geosat_ordered["z2"] == idsa_ordered.iloc[0]["z2"]))[0])

    winner_geosat = geosat_ordered.iloc[id]

    # print geosat_ordered.iloc[winner[0]]
    # print idsa_ordered.iloc[winner[1]]
    print winner_geosat.iloc[0]
    print winner_idsa


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None

    merge(old=False, total_number_parameter_file=23)
    print("---------")
    print("---------")
    print("---------")
    # merge(old=True, total_number_parameter_file=1)

    logging.debug("End Program")


# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.03, "z1": 0.003, "w2": 0.25, "s2": 0.1, "Exp": 0, "UR": 2, "Number": 1})
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.04, "z1": 0.004, "w2": 0.25, "s2": 0.1, "Exp": 1, "UR": 2, "Number": 1})
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.02, "z1": 0.002, "w2": 0.25, "s2": 0.1, "Exp": 2, "UR": 2, "Number": 1})
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.01, "z1": 0.001, "w2": 0.25, "s2": 0.1, "Exp": 3, "UR": 2, "Number": 1})
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.05, "z1": 0.005, "w2": 0.25, "s2": 0.1, "Exp": 4, "UR": 2, "Number": 1})
#
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 1.99, "z1": 0.199, "w2": 0.0, "s2": 0.0, "Exp": 0, "UR": 1, "Number": 1})
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 1.9, "z1": 0.19, "w2": 0.0, "s2": 0.0, "Exp": 1, "UR": 1, "Number": 1})
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 1.91, "z1": 0.191, "w2": 0.0, "s2": 0.0, "Exp": 2, "UR": 1, "Number": 1})
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 1.92, "z1": 0.192, "w2": 0.0, "s2": 0.0, "Exp": 3, "UR": 1, "Number": 1})
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 1.93, "z1": 0.193, "w2": 0.0, "s2": 0.0, "Exp": 4, "UR": 1, "Number": 1})
#
#
#
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.02, "z1": 0.002, "w2": 0.25, "s2": 0.5, "Exp": 0, "UR": 2, "Number": 1})
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.03, "z1": 0.003, "w2": 0.25, "s2": 0.5, "Exp": 1, "UR": 2, "Number": 1})
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.01, "z1": 0.001, "w2": 0.25, "s2": 0.5, "Exp": 2, "UR": 2, "Number": 1})
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.04, "z1": 0.004, "w2": 0.25, "s2": 0.5, "Exp": 3, "UR": 2, "Number": 1})
# comb.append({"Name": "PacmanDistance", "h": 1.0, "z2": 0.05, "z1": 0.005, "w2": 0.25, "s2": 0.5, "Exp": 4, "UR": 2, "Number": 1})
#
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 9.44, "z1": 0.944, "w2": 0.0, "s2": 0.0, "Exp": 0, "UR": 1, "Number": 1})
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 9.45, "z1": 0.945, "w2": 0.0, "s2": 0.0, "Exp": 1, "UR": 1, "Number": 1})
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 9.46, "z1": 0.946, "w2": 0.0, "s2": 0.0, "Exp": 2, "UR": 1, "Number": 1})
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 9.47, "z1": 0.947, "w2": 0.0, "s2": 0.0, "Exp": 3, "UR": 1, "Number": 1})
# comb.append({"Name": "PacmanNormal", "h": 1.0, "z2": 9.48, "z1": 0.948, "w2": 0.0, "s2": 0.0, "Exp": 4, "UR": 1, "Number": 1})