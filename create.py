# read folder
import filecmp
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import logging
import seaborn as sns;

import numpy

# this file computes the graph for every single folder or for all the folder together
from pandas import DataFrame

nameExp = "PacmanDistancePath"
# path = "/Users/alessandrozonta/Documents/Results Exp/250/"
path = "/Users/alessandrozonta/Documents/ResultsExp/fix/1500/"
path += nameExp
save = False
show = True
general = False
dict = {'PacmanDistance': 'PD', 'PacmanDistancePF': 'PDPF', 'PacmanNormal': 'Normal', 'PacmanNormalPF': 'Normal APF',
        'PacmanDistancePath': 'PDP', 'PacmanDistancePathPF': 'PDPPF', 'PacmanNormalPath': 'PNP',
        'PacmanNormalPathPF': 'PNPPF', 'PacmanNormalPath2': 'PNP2', 'PacmanNormalPFOld': 'Normal APF OLD'
    , 'PacmanNormalChina': 'Normal China', 'PacmanNormalPFChina': 'Normal APF China', 'PacmanDistancePath2': 'PDP2'}


def differentCompute():
    listLength, numberPoi, top5, top10, top, perf = loadOtherFile()
    median1 = []
    median = []
    realTop = []
    for x in range(len(top)):
        appo = []
        for y in range(len(top[x])):
            appo.append((100 * top[x][y]) / listLength[x][y])
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))
        median1.append(np.median(el))

    global path
    path += "/mix/"

    listLength, numberPoi, top5, top10, top, perf = loadOtherFile()
    median2 = []
    realTop = []
    for x in range(len(top)):
        appo = []
        for y in range(len(top[x])):
            appo.append((100 * top[x][y]) / listLength[x][y])
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))
        median2.append(np.median(el))

    path += "mix/"
    listLength, numberPoi, top5, top10, top, perf = loadOtherFile()
    median3 = []
    realTop = []
    for x in range(len(top)):
        appo = []
        for y in range(len(top[x])):
            appo.append((100 * top[x][y]) / listLength[x][y])
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))
        median3.append(np.median(el))

    plt.figure(1)
    # x = np.arange(len(median))
    # a = plt.scatter(x, median, c="r")
    #
    # plt.legend([a], ["median target highest charge"],
    #            scatterpoints=1, loc='upper left')
    # names = [" ", "30 degree", " ", "60 degree", " ", "120 degree", " ", "160 degree", " ", "180 degree"]
    # plt.xticks(np.arange(0, len(x), 40), names)
    # plt.ylabel("Different settings")
    #
    # plt.ylabel('Percentage before the end of the tracking path')
    # plt.ylim(0, 50)
    # plt.xlim(-1, len(median)+1)




    median11 = median1[:80]
    median12 = median1[81:160]
    median13 = median1[161:]

    x = [median11, median12, median13, median2, median3]
    plt.boxplot(x, whis=50)
    plt.xticks([1, 2, 3, 4, 5], ['30 degrees', '60 degrees', '120 degrees', '160 degrees', '180 degrees'])
    plt.ylabel('medianBoxPlot')



    plt.show()


def compute():
    # result contains the list of everything
    # do whatever you want
    # printGraphPOIs(result)

    listLenght, numberPoi, top5, top10, top, perf = loadOtherFile()
    # listLenghtR = listLenght[:113]
    # numberPoiR = numberPoi[:113]
    # top5R = top5[:113]
    # top10R = top10[:113]
    # topR = top[:113]
    # perfR = perf[:113]

    # for el in top5:
    # plt.figure(1)
    # plt.boxplot(top5, whis=99)
    # plt.figure(2)
    # plt.boxplot(top10, whis=99)
    # plt.figure(3)
    # plt.boxplot(top, whis=99)

    # plt.figure(1)
    # x = (median, median5, median10)
    # plt.hist(median, bins=len(median))
    # plt.hist(median5, bins=len(median5))
    # plt.hist(x, bins=len(median10), histtype='bar', color=['crimson', 'burlywood', 'chartreuse'],
    #                     label=['Crimson', 'Burlywood', 'Chartreuse'])
    # plt.figure(2)
    # plt.hist(top5, bins=len(top5))
    # plt.figure(3)
    # plt.hist(top10, bins=len(top10))


    # printGraphRelationWithLength(listLenght, top5, top10, top)

    # printGraphRelationWithNumberPOI(numberPoi, top5, top10, top)

    printGraphMedianRelation(top5, top10, top, listLenght)

    # printPerformance(perf)

    # printperfVSlenght(perf,listLenght)


def computeGeneral():
    subpath = "/Users/alessandrozonta/Documents/Results Exp/challenge/"
    directories = os.listdir(subpath)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")

    totalTop = []
    totalTop5 = []
    totalTop10 = []
    totalPerf = []
    totalLength = []
    for el in directories:
        global path
        global nameExp
        path = subpath + el
        nameExp = el
        listLength, numberPoi, top5, top10, top, perf = loadOtherFile()
        totalTop.append(top)
        totalTop5.append(top5)
        totalTop10.append(top10)
        totalPerf.append(perf)
        totalLength.append(listLength)

    totalNewMeasure = []
    for x in range(len(totalLength)):
        newMeasure = []
        for y in range(len(totalLength[x])):
            newNewMeasure = []
            for z in range(len(totalLength[x][y])):
                newNewMeasure.append((100 * totalTop[x][y][z])/totalLength[x][y][z])
            newMeasure.append(np.median(newNewMeasure))
        totalNewMeasure.append(newMeasure)

    totalNewMeasure5 = []
    # for x in range(len(totalLength)):
    #     newMeasure = []
    #     for y in range(len(totalLength[x])):
    #         newNewMeasure = []
    #         for z in range(len(totalLength[x][y])):
    #             newNewMeasure.append((100 * totalTop5[x][y][z]) / totalLength[x][y][z])
    #         newMeasure.append(np.median(newNewMeasure))
    #     totalNewMeasure.append(newMeasure)
    #
    # totalNewMeasure10 = []
    # for x in range(len(totalLength)):
    #     newMeasure = []
    #     for y in range(len(totalLength[x])):
    #         newNewMeasure = []
    #         for z in range(len(totalLength[x][y])):
    #             newNewMeasure.append((100 * totalTop10[x][y][z]) / totalLength[x][y][z])
    #         newMeasure.append(np.median(newNewMeasure))
    #     totalNewMeasure.append(newMeasure)


    realMedian = []
    nameGraph = []
    for x in range(0, len(directories)):
        median = []
        for el in totalTop[x]:
            median.append(np.median(el))
        realMedian.append(median)
        nameGraph.append(dict[directories[x]] + " HC")

    # cd

    # plt.figure(1)
    # plt.boxplot(realMedian, whis=10)
    # x = np.arange(1, len(nameGraph) + 1)
    # plt.xticks(x, nameGraph, rotation=30)

    # plt.figure(2)
    # for el in totalPerf:
    #     x = np.arange(len(el))
    #     plt.scatter(x, el)

    plt.figure(2)
    plt.boxplot(totalNewMeasure, whis=50)
    x = np.arange(1, len(nameGraph) + 1)
    plt.xticks(x, nameGraph, rotation=15)
    plt.ylabel("Percentage of the tracking path before the end")

    plt.show()


#
# # function for the performance
# def performance(realList, path):
#     sumlist = []
#     meanList = []
#     standardDeviationList = []
#     varianceList = []
#     listForGraph = []
#
#     # loop for all the rules
#     for y in range(0, len(realList)):
#         listPerformancePerRule = []
#         # for every rules I have to read all the json filesf or every person tracked
#         # with this loop I loop inside every folder and I read the performance array of every people
#         for z in range(0, len(realList[y]["list"]["list"])):
#             logging.debug("loading people n {} rules {}".format(z, y))
#             name = realList[y]["list"]["list"][z]
#             if name != ".DS_Store":
#                 number = realList[y]["list"]["number"]
#                 pathLocal = path + "/" + str(number) + "/" + str(name) + "/Performance.JSON"
#                 try:
#                     json_data = open(pathLocal).read()
#                     data = json.loads(json_data)
#                     listPerformancePerRule.append(np.array(data["Perf"]))
#                 except:
#                     logging.warning(pathLocal + " File non present")
#         # after the loop listperformanceper rule contains all the performance of all the tracked person
#         # do i need to normalise here?
#
#         value = []
#         listForGraph.append(listPerformancePerRule)
#
#         for el in listPerformancePerRule:
#             value.append(np.sum(el))
#             # plt.hist(el, bins=len(el))
#             # plt.show()
#             # x_value = list(range(0, len(el)))
#             # line, = plt.plot(x_value, el, '-', linewidth=2)
#
#         # y = np.array(listPerformancePerRule)
#
#         # plt.hist(y, bins=len(value))
#         # plt.show()
#         sumlist.append(np.sum(np.array(value)))
#         meanList.append(np.median(np.array(value)))
#         q75, q25 = np.percentile(np.array(value), [75, 25])
#         standardDeviationList.append(q75 - q25)
#         varianceList.append(np.var(np.array(value)))
#
#     # now in every position there is the sum of the performance value per every rules per all the tracked person
#     logging.debug(sumlist)
#     logging.debug(meanList)
#     logging.debug(standardDeviationList)
#     logging.debug(varianceList)
#
#     x = np.arange(len(sumlist))
#
#     y = np.array(meanList)
#     e = np.array(standardDeviationList)
#
#     plt.errorbar(x, y, e, linestyle='None', marker='^', c='g')
#     plt.savefig(path + "/positive-" + nameExp + ".png")
#     # plt.show()


# function for reading the POI and compute the graph
# def poi(realList, path):
#     totalList = []
#     totalListlistForCheckTheValue = []
#     totalListPerformancePerRule = []
#     totalListTopFivePerRule = []
#     totalListTopTenPerRule = []
#     # loop for all the rules
#     for y in range(0, len(realList)):
#         listPerformancePerRule = []
#         listTopFivePerRules = []
#         listTopTenPerRules = []
#         listLength = []
#         listForCheckTheValue = []
#         listForCheckTheValuePosition = []
#         # for every rules I have to read all the json filesf or every person tracked
#         # with this loop I loop inside every folder and I read the performance array of every people
#         for z in range(0, len(realList[y]["list"]["list"])):
#             logging.debug("loading people n {} rules {}".format(z, y))
#             nameHere = realList[y]["list"]["list"][z]
#             if nameHere != ".DS_Store":
#                 number = realList[y]["list"]["number"]
#                 pathLocal = path + "/" + number + "/" + nameHere + "/POIs.JSON"
#                 # totalList.append(pathLocal)
#                 try:
#                     json_data = open(pathLocal).read()
#                     json_data = json_data.replace("(", '"').replace(")", '"')
#                     data = json.loads(json_data)
#                     listPerformancePerRule.append(findForHowLong(data))
#                     listTopFivePerRules.append(findTopFive(data))
#                     listTopTenPerRules.append(findTopTen(data))
#                     for timestep in data["POIs"]:
#                         for poi in timestep:
#                             listForCheckTheValue.append(poi["Charge"])
#                             listForCheckTheValuePosition.append(poi["Loc"])
#                     # how many time step I tracked the person
#                     listLength.append(len(data["POIs"]))
#                 except:
#                     logging.warning(pathLocal + " File non present")
#         # totalListTarget.append(listTarget)
#         totalListPerformancePerRule.append(listPerformancePerRule)
#         totalListlistForCheckTheValue.append(listForCheckTheValue)
#         totalListTopFivePerRule.append(listTopFivePerRules)
#         totalListTopTenPerRule.append(listTopTenPerRules)
#         # totalListlistForCheckTheValuePosition.append(listForCheckTheValuePosition)
#         # a single data contains the charge and the position of all the POIs at every time steps
#         # listPerformancePerRule contains for how many time from the end the highest POI was the target per person
#         # totalList keep track of the sum/mean/standardDeviation and variance per rule of that value
#         vect = np.array(listPerformancePerRule)
#         secVect = np.array(listLength)
#         top5Vect = np.array(listTopFivePerRules)
#         top10Vect = np.array(listTopTenPerRules)
#
#         q75, q25 = np.percentile(vect, [75, 25])
#         iqr = q75 - q25
#         q75s, q25s = np.percentile(secVect, [75, 25])
#         iqrs = q75s - q25s
#         q755, q255 = np.percentile(top5Vect, [75, 25])
#         iqr5 = q755 - q255
#         q751, q251 = np.percentile(top10Vect, [75, 25])
#         iqr1 = q751 - q251
#
#         elHere = ({"sum": np.sum(vect), "median": np.median(vect), "iqr": iqr, "var": np.var(vect),
#                    "sumLength": np.sum(secVect), "medianLength": np.median(secVect),
#                    "iqrLength": iqrs,
#                    "varLength": np.var(secVect), "sumtop5": np.sum(top5Vect), "mediantop5": np.median(top5Vect),
#                    "iqrtop5": iqr5, "vartop5": np.var(top5Vect), "sumtop10": np.sum(top10Vect),
#                    "mediantop10": np.median(top10Vect), "iqrtop10": iqr1,
#                    "vartop10": np.var(top10Vect)})
#         logging.debug(
#             "Median of the length {}, Median of the count {} , median of the top 5 {} and media of the top 10 {} ".format(
#                 np.median(secVect), np.median(vect), np.median(top5Vect), np.median(top10Vect)))
#
#         with open(path + "/testpois-" + nameExp + ".txt", 'a') as f:
#             f.write("sum:{}; median:{}; iqr:{}; var:{}; sumLength:{}; medianLength:{}; iqrLength:{}; varLength:{};"
#                     "sumTop5:{}; medianTop5:{}; iqrTop5:{}; varTop5:{}; sumTop10:{}; medianTop10:{}; iqrTop10:{}; "
#                     "varTop10:{}; "
#                     "rule:{}; \n\n".format(elHere["sum"], elHere["median"], elHere["iqr"], elHere["var"],
#                                            elHere["sumLength"],
#                                            elHere["medianLength"],
#                                            elHere["iqrLength"], elHere["varLength"], elHere["sumtop5"],
#                                            elHere["mediantop5"], elHere["iqrtop5"],
#                                            elHere["vartop5"], elHere["sumtop10"], elHere["mediantop10"],
#                                            elHere["iqrtop10"], elHere["vartop10"],
#                                            realList[y]["rule"]))
#         logging.debug("Added line to first file...")
#         with open(path + "/testpois-table" + nameExp + ".txt", 'a') as g:
#             g.write("{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} \n\n".format(elHere["sum"], elHere["median"],
#                                                                                         elHere["iqr"],
#                                                                                         elHere["sumLength"],
#                                                                                         elHere["medianLength"],
#                                                                                         elHere["iqrLength"],
#                                                                                         elHere["sumtop5"],
#                                                                                         elHere["mediantop5"],
#                                                                                         elHere["vartop5"],
#                                                                                         elHere["sumtop10"],
#                                                                                         elHere["mediantop10"],
#                                                                                         elHere["iqrtop10"],
#                                                                                         realList[y]["rule"]["Alpha"],
#                                                                                         realList[y]["rule"]["w1"],
#                                                                                         realList[y]["rule"]["s1"],
#                                                                                         realList[y]["rule"]["w2"],
#                                                                                         realList[y]["rule"]["s2"],
#                                                                                         realList[y]["rule"]["UR"]))
#         logging.debug("Added line to second file...")
#
#         with open(path + "/listTop5-" + nameExp + ".txt", 'a') as h:
#             for el in top5Vect:
#                 h.write("{} ".format(el))
#             h.write("\n")
#
#         with open(path + "/listTop10-" + nameExp + ".txt", 'a') as i:
#             for el in top10Vect:
#                 i.write("{} ".format(el))
#             i.write("\n")
#
#         with open(path + "/listTop-" + nameExp + ".txt", 'a') as l:
#             for el in vect:
#                 l.write("{} ".format(el))
#             l.write("\n")
#
#     # print graph
#     printGraphPOIs(totalList)


# find the highest charge in data
# def findForHowLong(data):
#     target = data["target"]
#     array = []
#     # start from the back to the start
#     for i in range(len(data["POIs"]) - 1, -1, -1):
#         array.append(data["POIs"][i])
#     count = 0
#     # find the highest charge
#     for timestep in array:
#         charge = -9999
#         loc = ""
#         for poi in timestep:
#             if charge < poi["Charge"]:
#                 charge = poi["Charge"]
#                 loc = poi["Loc"]
#         # now in charge i have the highest POI charge in this timestep
#         if loc == target:
#             count += 1
#         else:
#             return count
#     return count
#
#
# # find the top five element in data
# def findTopFive(data):
#     target = data["target"]
#     array = []
#     # start from the back to the start
#     for i in range(len(data["POIs"]) - 1, -1, -1):
#         array.append(data["POIs"][i])
#     count = 0
#
#     # find the highest five charges
#     for timestep in array:
#         loc = ["", "", "", "", ""]
#         arr = []
#         for poi in timestep:
#             arr.append(poi["Charge"])
#         realArray = np.array(arr)
#         realArray.sort()
#         res = realArray[-5:]
#
#         for poi in timestep:
#             if res[0] == poi["Charge"]:
#                 loc[0] = poi["Loc"]
#             elif res[1] == poi["Charge"]:
#                 loc[1] = poi["Loc"]
#             elif res[2] == poi["Charge"]:
#                 loc[2] = poi["Loc"]
#             elif res[3] == poi["Charge"]:
#                 loc[3] = poi["Loc"]
#             elif res[4] == poi["Charge"]:
#                 loc[4] = poi["Loc"]
#
#         # now in charge i have the highest 5 POI charge in this timestep
#         if target in loc:
#             count += 1
#         else:
#             return count
#     return count
#
#
# # find the top ten element in data
# def findTopTen(data):
#     target = data["target"]
#     array = []
#     # start from the back to the start
#     for i in range(len(data["POIs"]) - 1, -1, -1):
#         array.append(data["POIs"][i])
#     count = 0
#     # find the highest ten charges
#     for timestep in array:
#         loc = ["", "", "", "", "", "", "", "", "", ""]
#         arr = []
#         for poi in timestep:
#             arr.append(poi["Charge"])
#         realArray = np.array(arr)
#         realArray.sort()
#         res = realArray[-10:]
#
#         for poi in timestep:
#             if res[0] == poi["Charge"]:
#                 loc[0] = poi["Loc"]
#             elif res[1] == poi["Charge"]:
#                 loc[1] = poi["Loc"]
#             elif res[2] == poi["Charge"]:
#                 loc[2] = poi["Loc"]
#             elif res[3] == poi["Charge"]:
#                 loc[3] = poi["Loc"]
#             elif res[4] == poi["Charge"]:
#                 loc[4] = poi["Loc"]
#             elif res[5] == poi["Charge"]:
#                 loc[5] = poi["Loc"]
#             elif res[6] == poi["Charge"]:
#                 loc[6] = poi["Loc"]
#             elif res[7] == poi["Charge"]:
#                 loc[7] = poi["Loc"]
#             elif res[8] == poi["Charge"]:
#                 loc[8] = poi["Loc"]
#             elif res[9] == poi["Charge"]:
#                 loc[9] = poi["Loc"]
#
#         # now in charge i have the highest 5 POI charge in this timestep
#         if target in loc:
#             count += 1
#         else:
#             return count
#     return count
#
#
# # test if two files are the sam eor not
# def findIfTheyAreTheSame(totalList):
#     countTrue = 0
#     countFalse = 0
#     for i in range(0, len(totalList)):
#         for j in range(0, len(totalList)):
#             if i != j:
#                 try:
#                     res = filecmp.cmp(totalList[i], totalList[j])
#                     if res:
#                         countTrue += 1
#                     else:
#                         countFalse += 1
#                 except:
#                     pass
#     print("true ={} and false={}".format(countTrue, countFalse))


# read the big big file
def fastRead():
    pathFastRead = path + "/testpois-" + nameExp + ".txt"
    totalList = []
    try:
        with open(pathFastRead) as f:
            for content in f:

                element = content.split(";")
                if "\n" not in content[0]:

                    tot = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

                    for el in element:
                        if "sum:" in el:
                            tot[0] = el[4:].replace("\n", '')
                        elif "median:" in el:
                            tot[1] = el[8:].replace("\n", '')
                        elif "var:" in el:
                            tot[2] = el[5:].replace("\n", '')
                        elif "iqr:" in el:
                            tot[3] = el[5:].replace("\n", '')
                        elif "sumLength:" in el:
                            tot[4] = el[11:].replace("\n", '')
                        elif "medianLength:" in el:
                            tot[5] = el[14:].replace("\n", '')
                        elif "iqrLength:" in el:
                            tot[6] = el[11:].replace("\n", '')
                        elif "varLength:" in el:
                            tot[7] = el[11:].replace("\n", '')
                        elif "sumTop5:" in el:
                            tot[8] = el[8:].replace("\n", '')
                        elif "medianTop5:" in el:
                            tot[9] = el[12:].replace("\n", '')
                        elif "iqrTop5:" in el:
                            tot[10] = el[9:].replace("\n", '')
                        elif "varTop5:" in el:
                            tot[11] = el[9:].replace("\n", '')
                        elif "sumTop10:" in el:
                            tot[12] = el[10:].replace("\n", '')
                        elif "medianTop10:" in el:
                            tot[13] = el[13:].replace("\n", '')
                        elif "iqrTop10:" in el:
                            tot[14] = el[10:].replace("\n", '')
                        elif "varTop10:" in el:
                            tot[15] = el[10:].replace("\n", '')
                        elif "rule:" in el:
                            appo = el[6:].replace("\n", '').split(",")
                            exper = appo[0].split(":")[1]
                            name = appo[1].split(":")[1]
                            s2 = appo[2].split(":")[1]
                            s1 = appo[3].split(":")[1]
                            numb = appo[4].split(":")[1]
                            UR = appo[5].split(":")[1]
                            w2 = appo[6].split(":")[1]
                            w1 = appo[7].split(":")[1]
                            alpha = appo[8].split(":")[1]
                            r = {
                                "Exp": exper,
                                "Name": name,
                                "s2": s2,
                                "s1": s1,
                                "Number": numb,
                                "UR": UR,
                                "w2": w2,
                                "w1": w1,
                                "Alpha": alpha,
                            }
                            rJson = json.dumps(r)
                    totalList.append(
                        {"sum": float(tot[0]), "median": float(tot[1]), "iqr": float(tot[3]), "var": float(tot[2]),
                         "sumLength": float(tot[4]), "medianLength": float(tot[5]),
                         "iqrLength": float(tot[6]),
                         "varLength": float(tot[7]), "sumtop5": float(tot[8]), "mediantop5": float(tot[9]),
                         "iqrtop5": float(tot[10]), "vartop5": float(tot[11]), "sumtop10": float(tot[12]),
                         "mediantop10": float(tot[13]), "iqrtop10": float(tot[14]),
                         "vartop10": float(tot[15]), "rule": rJson})

        # print graph
        # printGraphPOIs(totalList)
        return totalList
    except:
        return None


# def printGraphPOIs(totalList):
#     x = np.arange(len(totalList))
#     madeY = []
#     madeE = []
#
#     madeYY = []
#     madeEE = []
#
#     madeYYY = []
#     madeEEE = []
#
#     for el in totalList:
#         madeY.append(el["median"])
#         madeE.append(el["iqr"])
#         madeYY.append(el["mediantop5"])
#         madeEE.append(el["iqrtop5"])
#         madeYYY.append(el["mediantop10"])
#         madeEEE.append(el["iqrtop10"])
#     y = np.array(madeY)
#     e = np.array(madeE)
#
#     yy = np.array(madeYY)
#     ee = np.array(madeEE)
#
#     yyy = np.array(madeYYY)
#     eee = np.array(madeEEE)
#
#     plt.figure(1)
#     plt.errorbar(x, y, e, linestyle='None', marker='^', c='g')
#     plt.savefig(path + "/pois-" + nameExp + "0.png")
#
#     plt.figure(2)
#     plt.errorbar(x, yy, ee, linestyle='None', marker='x', c='b')
#     plt.savefig(path + "/pois-" + nameExp + "1.png")
#
#     plt.figure(3)
#     plt.errorbar(x, yyy, eee, linestyle='None', marker='o', c='r')
#     plt.savefig(path + "/pois-" + nameExp + "2.png")
#
#     plt.figure(4)
#     plt.errorbar(x, y, e, linestyle='None', marker='^', c='g')
#     plt.errorbar(x, yy, ee, linestyle='None', marker='x', c='b')
#     plt.errorbar(x, yyy, eee, linestyle='None', marker='o', c='r')
#     plt.savefig(path + "/pois-" + nameExp + ".png")
#     # plt.show()


# def readTracks(realList):
#     # loop for all the rules
#     totalList = []
#     for y in range(0, len(realList)):
#         listPerformancePerRule = []
#         # for every rules I have to read all the json filesf or every person tracked
#         # with this loop I loop inside every folder and I read the performance array of every people
#         for z in range(0, len(realList[y]["list"]["list"])):
#             logging.debug("loading people n {} rules {}".format(z, y))
#             name = realList[y]["list"]["list"][z]
#             if name != ".DS_Store":
#                 number = realList[y]["list"]["number"]
#                 pathLocal = path + "/" + str(number) + "/" + str(name) + "/path.JSON"
#                 try:
#                     json_data = open(pathLocal).read().replace("(", '"').replace(")", '"')
#                     data = json.loads(json_data)
#                     listPerformancePerRule.append(len(data["Path"]))
#                 except:
#                     logging.warning(pathLocal + " File non present")
#         totalList.append(listPerformancePerRule)
#     # check if they are all the same -> test if I am tracking always the same people
#     eq = True
#     first = totalList[0][0]
#     for z in range(1, len(totalList)):
#         if first != totalList[z][0]:
#             ez = False
#     logging.debug(eq)
#     # list length trajectories
#     return totalList[0]
#
#
# def countPOIs(realList):
#     totalList = []
#     for z in range(0, len(realList[0]["list"]["list"])):
#         logging.debug("loading people n {} rules {}".format(z, 0))
#         number = realList[0]["list"]["number"]
#         name = realList[0]["list"]["list"][z]
#         if name != ".DS_Store":
#             pathLocal = path + "/" + number + "/" + name + "/POIs.JSON"
#             try:
#                 json_data = open(pathLocal).read()
#                 json_data = json_data.replace("(", '"').replace(")", '"')
#                 data = json.loads(json_data)
#                 totalList.append(len(data['POIs'][0]))
#             except:
#                 logging.warning(pathLocal + " File non present")
#     return totalList

def printGraphMedianRelation(top5, top10, top, listLength):
    median = []
    realTop = []
    for x in range(len(top)):
        appo = []
        for y in range(len(top[x])):
            appo.append((100 * top[x][y])/listLength[x][y])
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))


    plt.figure(1)
    x = np.arange(len(median))
    logging.debug("Len -> {}".format(len(median)))
    a = plt.scatter(x, median, c="r")

    plt.legend([a], ["median target highest charge"],
               scatterpoints=1, loc='upper left')
    names = [" ", "30 degree", " ", "60 degree", " ", "120 degree", " ", "180 degree"]

    if len(x) < 50:
        plt.xticks(np.arange(0, len(x), 10), names)
    else:
        plt.xticks(np.arange(0, len(x), 40), names)
    plt.ylabel("Different settings")

    plt.ylabel('Percentage before the end of the tracking path')
    # plt.ylim(0, 35)
    plt.xlim(-1, len(x) + 1)
    plt.show()
    # if save:
    #     plt.savefig(path + "/medianScatter.png")

    # plt.figure(2)
    # x = [median, median5, median10]
    # plt.boxplot(x, whis=10)
    # plt.xticks([1, 2, 3], ['target highest charge', 'target top 5', 'target top 10'])
    # plt.ylabel('medianBoxPlot')
    # if save:
    #     plt.savefig(path + "/medianBoxPlot.png")
    #
    # if show:
    #     plt.show()
    # plt.figure(2)
    # sns.set(style="white", color_codes=True)
    # x = np.arange(len(median))
    # zz = {"x": x, "median": median}
    # dfs = DataFrame(data=zz)
    # ax = sns.regplot(x="x", y="median", data=dfs)
    # plt.show()


def printGraphRelationWithNumberPOI(numberPoi, top5, top10, top):

    plt.figure(0)
    for x in range(0, len(top)-1):
        plt.scatter(numberPoi[x], top[x], c="r")

    plt.figure(1)
    for x in range(0, len(top5)-1):
        plt.scatter(numberPoi[x], top5[x], c="b")

    plt.figure(2)
    for x in range(0, len(top10)-1):
        plt.scatter(numberPoi[x], top10[x], c="g")

    # for el in top:
    #     plt.scatter(numberPoi[0], el[0], c=numpy.random.rand(3, 1))
    # plt.ylabel('top')
    plt.show()

    # plt.figure(1)
    # for el in top5:
    #     plt.scatter(numberPoi[0], el, c=numpy.random.rand(3, 1))
    # plt.ylabel('top5')
    # # plt.show()
    #
    # plt.figure(2)
    # for el in top10:
    #     plt.scatter(numberPoi[0], el, c=numpy.random.rand(3, 1))
    # plt.ylabel('top10')
    # plt.show()


def printGraphRelationWithLength(listLenght, top5, top10, top):

    plt.figure(0)
    for i in range(0, len(top)):
        plt.scatter(listLenght[i], top[i], c="r")

    # plt.ylabel('top')
    # plt.show()

    plt.figure(1)
    for i in range(0, len(top5)):
        plt.scatter(listLenght[i], top5[i], c="g")
    # plt.ylabel('top5')
    # plt.show()

    plt.figure(2)
    for i in range(0, len(top10)):
        plt.scatter(listLenght[i], top10[i], c="b")
    # plt.ylabel('top10')

    # for i in range(0, len(top)):
    #     plt.scatter(listLenght[i], top[i], c="r")
    #     # plt.scatter(listLenght[i], top5[i], c="g")
        # plt.scatter(listLenght[i], top10[i], c="b")

    plt.show()


def printPerformance(perf):
    value = []
    for el in perf:
        value.append(np.median(el))

    x = np.arange(len(value))
    plt.scatter(x, value)
    plt.show()

    # plt.boxplot(perf, whis=10)
    # plt.ylabel('performance')
    # if save:
    #     plt.savefig(path + "/performance.png")
    # if show:
    #     plt.show()


def printperfVSlenght(perf,listLenght):
    for x in range(len(perf)):
        plt.scatter(listLenght[x], perf[x])
    plt.show()

def loadOtherFile():
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
    except Exception as e:
        logging.debug(e.message)
        # pass
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
    except Exception as e:
        logging.debug(e.message)
        # pass
    pathFastsRead = path + "/listTop5-" + nameExp + ".txt"
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
    # if general:
    # computeGeneral()
    # else:
    compute()
    # differentCompute()
    logging.debug("End Program")
