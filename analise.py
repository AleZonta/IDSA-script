import logging

import numpy as np
import matplotlib.pyplot as plt

# this script reads all the txt file present inside the nameExpList folder and compute the graph of the best results
# it also find the rules corresponding to that case

# nameExpList = ["PacmanDistance", "PacmanDistancePath", "PacmanDistancePathPF", "PacmanDistancePF"]
nameExpList = ["PacmanDistancePath"]
# localpath = "/Users/alessandrozonta/Documents/Results Exp/new30/OutputLisa/"
localpath = "/Users/alessandrozonta/Documents/Results Exp/200/"
path = ""
nameExp = ""
# path += nameExp
numberOfElement = 4


def setNumberOfElement(number):
    global numberOfElement
    numberOfElement = number


def compute():
    totalTop, totalTop5, totalTop10, totalIndex = computeByTop()

    # plt.figure(1)
    # x = np.arange(len(totalTop))
    # a = plt.scatter(x, totalTop, c="r")
    # b = plt.scatter(x, totalTop5, c="b")
    # c = plt.scatter(x, totalTop10, c="g")
    # plt.legend((a, b, c), ("Best {} highest charge".format(numberOfElement), "Best {} top 5".format(numberOfElement),
    #                        "Best {} top 10".format(numberOfElement)),
    #            scatterpoints=1, loc='upper left')
    #
    # numb = numberOfElement * 4
    # x = np.arange(numb)
    # name1 = "PD"
    # name2 = "PDP"
    # name3 = "PDPPF"
    # name4 = "PDPF"
    # y = []
    # for i in range(numberOfElement):
    #     y.append(name1)
    # for i in range(numberOfElement):
    #     y.append(name2)
    # for i in range(numberOfElement):
    #     y.append(name3)
    # for i in range(numberOfElement):
    #     y.append(name4)
    # if numb > 15:
    #     plt.xticks(x, y, rotation=90)
    # else:
    #     plt.xticks(x, y)
    # plt.xlim([0 - 1, numb])
    # plt.ylim([0, 1500])
    #
    # totalTop, totalTop5, totalTop10, totalIndex = computeByTop5()
    # plt.figure(2)
    # x = np.arange(len(totalTop))
    # a = plt.scatter(x, totalTop, c="r")
    # b = plt.scatter(x, totalTop5, c="b")
    # c = plt.scatter(x, totalTop10, c="g")
    # plt.legend((a, b, c), ("Best {} highest charge".format(numberOfElement), "Best {} top 5".format(numberOfElement),
    #                        "Best {} top 10".format(numberOfElement)),
    #            scatterpoints=1, loc='upper left')
    # if numb > 15:
    #     plt.xticks(x, y, rotation=90)
    # else:
    #     plt.xticks(x, y)
    # plt.xlim([0 - 1, numb])
    # plt.ylim([0, 1500])
    #
    # totalTop, totalTop5, totalTop10, totalIndex = computeByTop10()
    # plt.figure(3)
    # x = np.arange(len(totalTop))
    # a = plt.scatter(x, totalTop, c="r")
    # b = plt.scatter(x, totalTop5, c="b")
    # c = plt.scatter(x, totalTop10, c="g")
    # plt.legend((a, b, c), ("Best {} highest charge".format(numberOfElement), "Best {} top 5".format(numberOfElement),
    #                        "Best {} top 10".format(numberOfElement)),
    #            scatterpoints=1, loc='upper left')
    # if numb > 15:
    #     plt.xticks(x, y, rotation=90)
    # else:
    #     plt.xticks(x, y)
    # plt.xlim([0 - 1, numb])
    # plt.ylim([0, 1500])
    #
    # plt.figure(4)
    # vectorTest = []
    # for x in range(0, len(totalTop)):
    #     vec = [totalTop[x], totalTop5[x], totalTop10[x]]
    #     vectorTest.append(vec)
    # plt.boxplot(vectorTest, whis=10)
    # plt.ylim([0, 1500])
    #
    # totalTop, totalTop5, totalTop10, totalIndex = computeByTop5()
    # plt.figure(5)
    # vectorTest = []
    # for x in range(0, len(totalTop)):
    #     vec = [totalTop[x], totalTop5[x], totalTop10[x]]
    #     vectorTest.append(vec)
    # plt.boxplot(vectorTest, whis=10)
    # plt.ylim([0, 1500])
    #
    # totalTop, totalTop5, totalTop10, totalIndex = computeByTop10()
    # plt.figure(6)
    # vectorTest = []
    # for x in range(0, len(totalTop)):
    #     vec = [totalTop[x], totalTop5[x], totalTop10[x]]
    #     vectorTest.append(vec)
    # plt.boxplot(vectorTest, whis=10)
    # plt.ylim([0, 1500])

    plt.show()


def computeByTop():
    totalTop = []
    totalTop5 = []
    totalTop10 = []
    totalIndex = []
    totalLenght = []
    for el in nameExpList:
        global path
        global nameExp
        path = localpath + str(el)
        nameExp = str(el)

        logging.debug("Checking rule {}".format(el))

        listLength, numberPoi, top5, top10, top, perf = loadOtherFile()

        median = []
        for ele in top:
            median.append(np.median(ele))
        median5 = []
        for ele in top5:
            median5.append(np.median(ele))
        median10 = []
        for ele in top10:
            median10.append(np.median(ele))

        # find the top 10 setting in this rule
        npMedian = np.array(median)
        npMedian5 = np.array(median5)
        npMedian10 = np.array(median10)
        # logging.debug(npMedian)
        ind = np.argpartition(npMedian, -numberOfElement)[-numberOfElement:]
        logging.debug(ind)
        values = npMedian[ind]
        values5 = npMedian5[ind]
        values10 = npMedian10[ind]

        logging.debug("Top {}".format(values))
        logging.debug("Top5 {}".format(values5))
        logging.debug("Top10 {}".format(values10))

        # read rules
        listParameter = readPar(nameExp, ind)
        logging.debug("parameter corresponding to the top selected {}".format(listParameter))

        for x in range(0, len(values)):
            totalTop.append(values[x])
            totalTop5.append(values5[x])
            totalTop10.append(values10[x])
            totalIndex.append(ind[x])

        logging.debug("Checking if they are the top")
        ind = np.argpartition(npMedian5, -numberOfElement)[-numberOfElement:]
        values5 = npMedian5[ind]
        logging.debug("Top5 {}".format(values5))

        ind = np.argpartition(npMedian10, -numberOfElement)[-numberOfElement:]
        values10 = npMedian10[ind]
        logging.debug("Top10 {}".format(values10))

    logging.debug("Final Vector")
    logging.debug(totalTop)
    logging.debug(totalTop5)
    logging.debug(totalTop10)
    logging.debug(totalIndex)

    return totalTop, totalTop5, totalTop10, totalIndex


def computeByTop5():
    totalTop = []
    totalTop5 = []
    totalTop10 = []
    totalIndex = []
    for el in nameExpList:
        global path
        global nameExp
        path = localpath + str(el)
        nameExp = str(el)

        logging.debug("Checking rule {}".format(el))

        listLength, numberPoi, top5, top10, top, perf = loadOtherFile()

        median = []
        for ele in top:
            median.append(np.median(ele))
        median5 = []
        for ele in top5:
            median5.append(np.median(ele))
        median10 = []
        for ele in top10:
            median10.append(np.median(ele))

        # find the top 10 setting in this rule
        npMedian = np.array(median)
        npMedian5 = np.array(median5)
        npMedian10 = np.array(median10)
        # logging.debug(npMedian)
        ind = np.argpartition(npMedian5, -numberOfElement)[-numberOfElement:]
        logging.debug(ind)
        values = npMedian[ind]
        values5 = npMedian5[ind]
        values10 = npMedian10[ind]
        logging.debug("Top {}".format(values))
        logging.debug("Top5 {}".format(values5))
        logging.debug("Top10 {}".format(values10))

        for x in range(0, len(values)):
            totalTop.append(values[x])
            totalTop5.append(values5[x])
            totalTop10.append(values10[x])
            totalIndex.append(ind[x])

        logging.debug("Checking if they are the top")
        ind = np.argpartition(npMedian, -numberOfElement)[-numberOfElement:]
        values = npMedian[ind]
        logging.debug("Top {}".format(values))

        ind = np.argpartition(npMedian10, -numberOfElement)[-numberOfElement:]
        values10 = npMedian10[ind]
        logging.debug("Top10 {}".format(values10))

    logging.debug("Final Vector")
    logging.debug(totalTop)
    logging.debug(totalTop5)
    logging.debug(totalTop10)
    logging.debug(totalIndex)

    return totalTop, totalTop5, totalTop10, totalIndex


def computeByTop10():
    totalTop = []
    totalTop5 = []
    totalTop10 = []
    totalIndex = []
    for el in nameExpList:
        global path
        global nameExp
        path = localpath + str(el)
        nameExp = str(el)

        logging.debug("Checking rule {}".format(el))

        listLength, numberPoi, top5, top10, top, perf = loadOtherFile()

        median = []
        for ele in top:
            median.append(np.median(ele))
        median5 = []
        for ele in top5:
            median5.append(np.median(ele))
        median10 = []
        for ele in top10:
            median10.append(np.median(ele))

        # find the top 10 setting in this rule
        npMedian = np.array(median)
        npMedian5 = np.array(median5)
        npMedian10 = np.array(median10)
        # logging.debug(npMedian)
        ind = np.argpartition(npMedian10, -numberOfElement)[-numberOfElement:]
        logging.debug(ind)
        values = npMedian[ind]
        values5 = npMedian5[ind]
        values10 = npMedian10[ind]
        logging.debug("Top {}".format(values))
        logging.debug("Top5 {}".format(values5))
        logging.debug("Top10 {}".format(values10))

        for x in range(0, len(values)):
            totalTop.append(values[x])
            totalTop5.append(values5[x])
            totalTop10.append(values10[x])
            totalIndex.append(ind[x])

        logging.debug("Checking if they are the top")
        ind = np.argpartition(npMedian, -numberOfElement)[-numberOfElement:]
        values = npMedian[ind]
        logging.debug("Top {}".format(values))

        ind = np.argpartition(npMedian5, -numberOfElement)[-numberOfElement:]
        values5 = npMedian5[ind]
        logging.debug("Top10 {}".format(values5))

    logging.debug("Final Vector")
    logging.debug(totalTop)
    logging.debug(totalTop5)
    logging.debug(totalTop10)
    logging.debug(totalIndex)

    return totalTop, totalTop5, totalTop10, totalIndex


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

    # pathFastRead = path + "/Performance-" + nameExp + ".txt"
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

    return listLenght, numberPoi, top5, top10, top, perf


def readPar(name, listNumberRule):
    listRules = []
    files = ["param1", "param2", "param3", "param4", "param5", "param6", "param7", "param8"]
    for el in files:
        pathFastRead = path + "/" + el
        try:
            with open(pathFastRead) as f:
                for content in f:
                    value = content.split(" ")
                    if value[5] == name:
                        listRules.append(value)
        except:
            logging.debug("No parameters file present")

    if len(listRules) == 0:
        return None
    # now I know all the rules
    # should find the parameters
    # inside listNumberRule I have all the index
    detailsRuleSelected = []
    for el in listNumberRule:
        i = 0
        while (str(listRules[i][6]) != str(el)) & (i < len(listRules) -1 ):
            i += 1
        if i != len(listRules):
            detailsRuleSelected.append(listRules[i])
    return detailsRuleSelected

# main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None

    compute()

    logging.debug("End Program")
