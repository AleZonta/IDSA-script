import logging

import numpy as np

# nameExpList = ["PacmanDistance", "PacmanDistancePath", "PacmanDistancePathPF", "PacmanDistancePF"]
nameExpList = ["PacmanDistance"]
# localpath = "/Users/alessandrozonta/Documents/Results Exp/new30/OutputLisa/"
localpath = "/Users/alessandrozonta/Documents/ResultsExp/latest/200idsa/"
path = ""
nameExp = ""
# path += nameExp
numberOfElement = 4


def computeByTop():
    conf = []
    for el in nameExpList:
        global path
        global nameExp
        path = localpath + str(el)
        nameExp = str(el)
        #
        # logging.debug("Checking rule {}".format(el))

        listLength, numberPoi, top5, top10, top, perf = loadOtherFile()

        median = []
        realTop = []
        for x in range(len(top)):
            appo = []
            try:
                for y in range(len(top[x])):
                    appo.append((100 * top[x][y]) / listLength[x][y])
            except:
                pass
            realTop.append(appo)
        for el in realTop:
            median.append(np.median(el))

        # find the top 10 setting in this rule
        npMedian = np.array(median)

        # logging.debug(npMedian)
        ind = np.argpartition(npMedian, -numberOfElement)[-numberOfElement:]
        # logging.debug(ind)
        values = npMedian[ind]

        logging.debug("Top {}".format(values))

        # read rules
        listParameter = readPar(nameExp, ind)
        # logging.debug("parameter corresponding to the top selected {}".format(listParameter))

        for el in listParameter:
            logging.debug(el[:7])



        # # check amx angle and minimum angle
        # vect = []
        # for elt in listParameter:
        #     vect.append(float(elt[0]))
        # rVect = np.array(vect)
        # ang = (np.min(rVect), np.max(rVect))
        #
        # # check amx angle and minimum s1
        # vect = []
        # for elt in listParameter:
        #     vect.append(float(elt[1]))
        # rVect = np.array(vect)
        # s1 = (np.min(rVect), np.max(rVect))
        #
        # # check amx angle and minimum w1
        # vect = []
        # for elt in listParameter:
        #     vect.append(float(elt[2]))
        # rVect = np.array(vect)
        # w1 = (np.min(rVect), np.max(rVect))
        #
        # # check amx angle and minimum s2
        # vect = []
        # for elt in listParameter:
        #     vect.append(float(elt[3]))
        # rVect = np.array(vect)
        # s2 = (np.min(rVect), np.max(rVect))
        #
        # # check amx angle and minimum w2
        # vect = []
        # for elt in listParameter:
        #     vect.append(float(elt[4]))
        # rVect = np.array(vect)
        # w2 = (np.min(rVect), np.max(rVect))
        #
        # conf.append((ang, w1, s1, s2, w2))
        # logging.debug((el, ang, w1, s1, s2, w2))
    return conf


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


def readPar(name, listNumberRule):
    listRules = []
    files = ["p0"]
    for el in files:
        pathFastRead = path + "/" + el
        try:
            with open(pathFastRead) as f:
                for content in f:
                    value = content.split(" ")
                    if value[5] == name:
                        listRules.append(value)
        except:
            pass

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
    conf = computeByTop()


    logging.debug("End Program")