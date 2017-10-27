import json
import logging
import os
import random
import shutil
import zipfile

import seaborn as sns

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

nameExp = "OutputtestGH"
path = "/Users/alessandrozonta/Documents/Results Exp/folderfix/"
number = "1"
# path = "/Users/alessandrozonta/Documents/Results Exp/new30/OutputLisa/"
path += nameExp + "/" + number
zipFile = "True"


def readData():
    directories = os.listdir(path)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    listPerformancePerPerson = []
    listTopPerRule = []
    listTopFivePerRule = []
    listTopTenPerRule = []
    listLength = []
    countPOI = []
    listSingleCharge = []
    lengthTrajectories = []
    for el in directories:
        logging.debug("laoding {}".format(el))
        fileName = "/Performance.zip"
        pathLocalSecond = path + "/" + el + fileName
        try:
            zf = zipfile.ZipFile(pathLocalSecond)
            filename = "/Performance.JSON"
            json_data = zf.read(filename)
            data = json.loads(json_data)
            try:
                listPerformancePerPerson.append(np.array(data["Perf"]))
            except:
                listPerformancePerPerson.append(np.array(data))
        except:
            logging.warning(pathLocalSecond + " File non present")

        # -----------------------------------------------------

        fileName = "/POIs.zip"
        pathLocal = path + "/" + el + fileName
        # totalList.append(pathLocal)
        try:
            zf = zipfile.ZipFile(pathLocal)
            filename = "/POIs.JSON"
            zipdata = zf.read(filename)
            json_data = zipdata.replace("(", '"').replace(")", '"')
            data = json.loads(json_data)
            listTopPerRule.append(findForHowLong(data))
            listTopFivePerRule.append(findTopFive(data))
            listTopTenPerRule.append(findTopTen(data))
            # how many time step I tracked the person
            listLength.append(len(data["POIsCharge"]))
            # count the number of the POI
            countPOI.append(len(data['POIsLocation']))
        except:
            logging.warning(pathLocal + " File non present")

        # -----------------------------------------------------

        fileName = "/waypoint.zip"
        pathLocal = path + "/" + el + fileName
        try:
            zf = zipfile.ZipFile(pathLocal)
            filename = "/waypoint.JSON"
            zipdata = zf.read(filename)
            json_data = zipdata.replace("(", '"').replace(")", '"')
            data = json.loads(json_data)
            biglist = data["waypoints"]

            total = []
            for el in biglist:
                sub_x = []
                sub_y = []
                for sub_el in el:
                    div = sub_el.split(",")
                    if len(div) == 1:
                        sub_x.append(None)
                        sub_y.append(None)
                    else:
                        sub_x.append(div[0])
                        sub_y.append(div[1])
                sub_values = [sub_x, sub_y]
                total.append(sub_values)
            dsfefrse = ""

        except:
            logging.warning(pathLocal + " File non present")

         # -----------------------------------------------------

    return listPerformancePerPerson, listTopPerRule, listTopFivePerRule, listTopTenPerRule, listLength, countPOI, lengthTrajectories


def computePerfAndNumb(listPerformancePerPerson, numPOI):

    plt.figure(1)
    count = 0
    for el in listPerformancePerPerson:
        plt.scatter(numPOI[count], el[:len(numPOI[count])])
        count += 1

    plt.show()


def computePerformance(listPerformancePerPerson):
    res = []

    for el in listPerformancePerPerson:
        res.append(np.sum(np.array(el)))


    plt.figure(1)
    x = np.arange(len(res))
    plt.scatter(x, res)

    plt.figure(2)
    for el in listPerformancePerPerson:
        x = np.arange(len(el))
        plt.plot(x, el)

    plt.figure(3)
    plt.boxplot(listPerformancePerPerson, whis=10)
    plt.xlim()

    plt.show()


def computeWorstPerformance(listPerformancePerPerson):
    res = []

    for el in listPerformancePerPerson:
        res.append(np.sum(np.array(el)))

    ind = np.argpartition(np.array(res), -6)[-6:]
    values = np.array(res)[ind]

    plt.figure(1)
    x = np.arange(len(values))
    plt.scatter(x, values)

    listValues = np.array(listPerformancePerPerson)[ind]
    plt.figure(2)
    for el in listValues:
        x = np.arange(len(el))
        plt.plot(x, el)

    plt.figure(3)
    plt.boxplot(listValues, whis=10)

    plt.show()


def computePOIs(listTopPerRule, listTopFivePerRule, listTopTenPerRule, listLength, countPOI):
    realTop = []
    for x in range(len(listTopPerRule)):
        realTop.append((100 * listTopPerRule[x]) / listLength[x])

    plt.figure(1)
    plt.scatter(countPOI, realTop)
    plt.show()


def computeLength(listTopPerRule, lengthTrajectories, listLength):
    realTop = []
    for x in range(len(listTopPerRule)):
        realTop.append((100 * listTopPerRule[x]) / listLength[x])

    # a = plt.scatter(lengthTrajectories, realTop, c="r")

    zz = {"realTop": realTop, "lengthTrajectories": lengthTrajectories}
    #
    dfs = DataFrame(data=zz)
    plt.figure(1)
    sns.set(style="white", color_codes=True)
    ax = sns.regplot(x="lengthTrajectories", y="realTop", data=dfs)
    plt.xlabel("Length of the trajectories")
    plt.ylabel("Percentage before the end of the tracking path")

    plt.show()


# find the highest charge in data
def findForHowLong(data):
    target = data["target"]
    array = []
    # start from the back to the start
    for i in range(len(data["POIsCharge"]) - 1, -1, -1):
        array.append(data["POIsCharge"][i])

    pois = data["POIsLocation"]


    count = 0
    # find the highest charge
    for timestep in array:
        charge = -9999
        loc = ""
        for poi in timestep:
            if charge < poi:
                charge = poi
                loc = pois[timestep.index(poi)]
        # now in charge i have the highest POI charge in this timestep
        if loc == target:
            count += 1
        else:
            return count
    return count


# find the top five element in data
def findTopFive(data):
    target = data["target"]
    array = []
    # start from the back to the start
    for i in range(len(data["POIsCharge"]) - 1, -1, -1):
        array.append(data["POIsCharge"][i])
    count = 0

    pois = data["POIsLocation"]

    # find the highest five charges
    for timestep in array:
        loc = ["", "", "", "", ""]
        arr = []
        for poi in timestep:
            arr.append(poi)
        realArray = np.array(arr)
        realArray.sort()
        res = realArray[-5:]

        for poi in timestep:
            if res[0] == poi:
                loc[0] = pois[timestep.index(poi)]
            elif res[1] == poi:
                loc[1] = pois[timestep.index(poi)]
            elif res[2] == poi:
                loc[2] = pois[timestep.index(poi)]
            elif res[3] == poi:
                loc[3] = pois[timestep.index(poi)]
            elif res[4] == poi:
                loc[4] = pois[timestep.index(poi)]

        # now in charge i have the highest 5 POI charge in this timestep
        if target in loc:
            count += 1
        else:
            return count
    return count


# find the top ten element in data
def findTopTen(data):
    target = data["target"]
    array = []
    # start from the back to the start
    for i in range(len(data["POIsCharge"]) - 1, -1, -1):
        array.append(data["POIsCharge"][i])
    count = 0
    pois = data["POIsLocation"]
    # find the highest ten charges
    for timestep in array:
        loc = ["", "", "", "", "", "", "", "", "", ""]
        arr = []
        for poi in timestep:
            arr.append(poi)
        realArray = np.array(arr)
        realArray.sort()
        res = realArray[-10:]

        for poi in timestep:
            if res[0] == poi:
                loc[0] = pois[timestep.index(poi)]
            elif res[1] == poi:
                loc[1] = pois[timestep.index(poi)]
            elif res[2] == poi:
                loc[2] = pois[timestep.index(poi)]
            elif res[3] == poi:
                loc[3] = pois[timestep.index(poi)]
            elif res[4] == poi:
                loc[4] = pois[timestep.index(poi)]
            elif res[5] == poi:
                loc[5] = pois[timestep.index(poi)]
            elif res[6] == poi:
                loc[6] = pois[timestep.index(poi)]
            elif res[7] == poi:
                loc[7] = pois[timestep.index(poi)]
            elif res[8] == poi:
                loc[8] = pois[timestep.index(poi)]
            elif res[9] == poi:
                loc[9] = pois[timestep.index(poi)]

        # now in charge i have the highest 5 POI charge in this timestep
        if target in loc:
            count += 1
        else:
            return count
    return count


def bootstrap(listTopPerRule, listLength):
    percentage = []
    count = 0
    for el in listTopPerRule:
        percentage.append((100 * el) / listLength[count])
        count += 1

    sample = 20
    list_sub_percentage = []
    label = []
    for x in range(sample):
        val = random.randrange(len(percentage))
        label.append(val)
        sub_percentage = []
        for y in range(val):
            sub_percentage.append(percentage[random.randrange(len(percentage))])
        list_sub_percentage.append(np.array(sub_percentage))

    plt.boxplot(list_sub_percentage, whis=10)
    x = np.arange(1, len(label)+1)
    final_label = []
    for el in label:
        final_label.append(str(el) + " Elem")
    plt.xticks(x, final_label, rotation=45)
    plt.show()


def perfWithTop(listTopPerRule, listLength, listPerformancePerPerson):
    realTop = []
    for x in range(len(listTopPerRule)):
        realTop.append((100 * listTopPerRule[x]) / listLength[x])

    res = []

    for el in listPerformancePerPerson:
        res.append(np.sum(np.array(el)))

    a = plt.scatter(res, realTop, c="r")

    # zz = {"realTop": realTop, "res": res}
    #
    # dfs = DataFrame(data=zz)
    #
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='realTop', y='res', data=dfs, jitter=True, edgecolor='none', alpha=.40,
    #                      palette="ocean")
    # # plot.get_legend().set_visible(False)
    # sns.despine()

    plt.xlabel("Percentage before the end of the tracking path")
    plt.ylabel("Integrals of the performances")

    plt.show()


def double(listTopPerRule, listLength, listPerformancePerPerson, lengthTrajectories):
    realTop = []
    for x in range(len(listTopPerRule)):
        realTop.append((100 * listTopPerRule[x]) / listLength[x])

    res = []

    for el in listPerformancePerPerson:
        res.append(np.sum(np.array(el)))

    zzz = {"realTop": realTop, "res": res, "lengthTrajectories": lengthTrajectories}
    #
    plt.figure(1)
    dfs = DataFrame(data=zzz)
    sns.set(style="white", color_codes=True)
    plot = sns.stripplot(x='lengthTrajectories', y='res', data=dfs, jitter=True, hue="realTop", edgecolor='none',
                         alpha=.40,
                         palette="ocean")
    plot.get_legend().set_visible(False)
    sns.despine()

    plt.xlabel("Length of the trajectories")
    plt.ylabel("Integrals of the performances")

    plt.figure(2)
    sns.set(style="white", color_codes=True)
    ax = sns.regplot(x="lengthTrajectories", y="res", data=dfs)

    plt.xlabel("Length of the trajectories")
    plt.ylabel("Integrals of the performances")








    # npRes = np.array(res)
    # ind = np.argpartition(npRes, -10)[-10:]
    # values = npRes[ind]
    # for el in values:
    #     res.remove(el)
    #
    # npRealTop = np.array(realTop)
    # values = npRealTop[ind]
    # for el in values:
    #     realTop.remove(el)
    #
    # npLength = np.array(lengthTrajectories)
    # values = npLength[ind]
    # for el in values:
    #     lengthTrajectories.remove(el)
    #
    # zz = {"realTop": realTop, "res": res, "lengthTrajectories": lengthTrajectories}
    # #
    # plt.figure(3)
    # dfs = DataFrame(data=zz)
    # sns.set(style="white", color_codes=True)
    # plot = sns.stripplot(x='lengthTrajectories', y='res', data=dfs, jitter=True, hue="realTop", edgecolor='none', alpha=.40,
    #                      palette="ocean")
    # plot.get_legend().set_visible(False)
    # sns.despine()
    #
    # plt.xlabel("Length of the trajectories")
    # plt.ylabel("Integrals of the performances")
    #
    # plt.figure(4)
    # sns.set(style="white", color_codes=True)
    # ax = sns.regplot(x="lengthTrajectories", y="res", data=dfs)
    #
    # plt.xlabel("Length of the trajectories")
    # plt.ylabel("Integrals of the performances")


    plt.show()


def perfAndTop(listPerformancePerPerson, listTopPerRule, listLength):
    realTop = []
    for x in range(len(listTopPerRule)):
        realTop.append((100 * listTopPerRule[x]) / listLength[x])

    res = []

    for el in listPerformancePerPerson:
        res.append(np.sum(np.array(el)))

    zz = {"realTop": realTop, "res": res}
    dfs = DataFrame(data=zz)
    plt.figure(1)
    sns.set(style="white", color_codes=True)
    # ax = sns.regplot(x="realTop", y="res", data=dfs)
    plot = sns.stripplot(x='realTop', y='res', data=dfs, jitter=True, edgecolor='none',
                         alpha=.40,
                         palette="ocean")
    # plot.get_legend().set_visible(False)
    sns.despine()
    # plt.xlabel("Length of the trajectories")
    # plt.ylabel("Integral Performances")

    plt.show()


# main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None

    # computePOIs()
    # computePerformance();

    listPerformancePerPerson, listTopPerRule, listTopFivePerRule, listTopTenPerRule, listLength, countPOI, lengthTrajectories = readData()

    # bootstrap(listTopPerRule,listLength)
    # computePerformance(listPerformancePerPerson, countPOI)

    # computePOIs(listTopPerRule, listTopFivePerRule, listTopTenPerRule, listLength, countPOI)
    # computePerfAndNumb(listPerformancePerPerson, countPOI)
    # perfWithTop(listTopPerRule, listLength, listPerformancePerPerson)

    # computeLength(listTopPerRule, lengthTrajectories, listLength)
    double(listTopPerRule, listLength, listPerformancePerPerson, lengthTrajectories)

    # perfAndTop(listPerformancePerPerson, lengthTrajectories, listLength)


    logging.debug("End Program")
