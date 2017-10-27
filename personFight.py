import json
import logging
import os
import zipfile

import matplotlib.pyplot as plt
import numpy as np

nameExp = "PacmanDistance"
pathGlobal = "/Users/alessandrozonta/Documents/Results Exp/250/"
path = ""

# path = "/Users/alessandrozonta/Documents/Results Exp/new30/OutputLisa/"
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
        if zipFile == "True":
            fileName = "/Performance.zip"
        else:
            fileName = "/Performance.JSON"
        pathLocalSecond = path + "/" + el + fileName
        try:
            if zipFile == "True":
                zf = zipfile.ZipFile(pathLocalSecond)
                filename = "/Performance.JSON"
                json_data = zf.read(filename)
            else:
                json_data = open(pathLocalSecond).read()
            data = json.loads(json_data)
            listPerformancePerPerson.append(np.array(data["Perf"]))
        except:
            logging.warning(pathLocalSecond + " File non present")

        # -----------------------------------------------------

        if zipFile == "True":
            fileName = "/POIs.zip"
        else:
            fileName = "/POIs.JSON"
        pathLocalSecond = path + "/" + el + fileName
        try:
            if zipFile == "True":
                zf = zipfile.ZipFile(pathLocalSecond)
                filename = "/POIs.JSON"
                zipdata = zf.read(filename)
                json_data = zipdata.replace("(", '"').replace(")", '"')
            else:
                json_data = open(pathLocalSecond).read()
                json_data = json_data.replace("(", '"').replace(")", '"')
            data = json.loads(json_data)
            listTopPerRule.append(findForHowLong(data))
            listTopFivePerRule.append(findTopFive(data))
            listTopTenPerRule.append(findTopTen(data))
            listSingleCharge.append(data["POIs"])
            # how many time step I tracked the person
            listLength.append(len(data["POIs"]))
            # count the number of the POI
            countPOI.append(len(data['POIs'][0]))
        except:
            logging.warning(pathLocalSecond + " File non present")

            # -----------------------------------------------------

        if zip == "True":
            fileName = "/path.zip"
        else:
            fileName = "/path.JSON"
        pathLocalSecond = path + "/" + el + fileName
        try:
            if zip == "True":
                zf = zipfile.ZipFile(pathLocalSecond)
                filename = "/path.JSON"
                zipdata = zf.read(filename)
                json_data = zipdata.replace("(", '"').replace(")", '"')
            else:
                json_data = open(pathLocalSecond).read()
                json_data = json_data.replace("(", '"').replace(")", '"')
            data = json.loads(json_data)
            # check length trajectory tracked
            lengthTrajectories.append(len(data["Path"]))
        except:
            logging.warning(pathLocalSecond + " File non present")

    return listPerformancePerPerson, listTopPerRule, listTopFivePerRule, listTopTenPerRule, listLength, countPOI, lengthTrajectories


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
    for i in range(len(data["POIs"]) - 1, -1, -1):
        array.append(data["POIs"][i])
    count = 0

    # find the highest five charges
    for timestep in array:
        loc = ["", "", "", "", ""]
        arr = []
        for poi in timestep:
            arr.append(poi["Charge"])
        realArray = np.array(arr)
        realArray.sort()
        res = realArray[-5:]

        for poi in timestep:
            if res[0] == poi["Charge"]:
                loc[0] = poi["Loc"]
            elif res[1] == poi["Charge"]:
                loc[1] = poi["Loc"]
            elif res[2] == poi["Charge"]:
                loc[2] = poi["Loc"]
            elif res[3] == poi["Charge"]:
                loc[3] = poi["Loc"]
            elif res[4] == poi["Charge"]:
                loc[4] = poi["Loc"]

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
    for i in range(len(data["POIs"]) - 1, -1, -1):
        array.append(data["POIs"][i])
    count = 0
    # find the highest ten charges
    for timestep in array:
        loc = ["", "", "", "", "", "", "", "", "", ""]
        arr = []
        for poi in timestep:
            arr.append(poi["Charge"])
        realArray = np.array(arr)
        realArray.sort()
        res = realArray[-10:]

        for poi in timestep:
            if res[0] == poi["Charge"]:
                loc[0] = poi["Loc"]
            elif res[1] == poi["Charge"]:
                loc[1] = poi["Loc"]
            elif res[2] == poi["Charge"]:
                loc[2] = poi["Loc"]
            elif res[3] == poi["Charge"]:
                loc[3] = poi["Loc"]
            elif res[4] == poi["Charge"]:
                loc[4] = poi["Loc"]
            elif res[5] == poi["Charge"]:
                loc[5] = poi["Loc"]
            elif res[6] == poi["Charge"]:
                loc[6] = poi["Loc"]
            elif res[7] == poi["Charge"]:
                loc[7] = poi["Loc"]
            elif res[8] == poi["Charge"]:
                loc[8] = poi["Loc"]
            elif res[9] == poi["Charge"]:
                loc[9] = poi["Loc"]

        # now in charge i have the highest 5 POI charge in this timestep
        if target in loc:
            count += 1
        else:
            return count
    return count


def compare(number):
    global path

    x = []
    for el in number:
        path = pathGlobal + nameExp + "/" + el
        listPerformancePerPerson, listTopPerRule, listTopFivePerRule, listTopTenPerRule, listLength, countPOI, lengthTrajectories = readData()
        x.append((listPerformancePerPerson, listTopPerRule, listTopFivePerRule, listTopTenPerRule, listLength, countPOI,
           lengthTrajectories))

    y = []
    for el in x:
        appo = []
        for x in range(len(el[1])):
            appo.append((100 * el[1][x]) / el[4][x])
        y.append(appo)  # append top value
        
    num = np.arange(1, len(y) + 1)
    plt.boxplot(y, whis=10)
    plt.xticks(num,
               number, rotation=17)
    plt.ylabel("Time steps before the end")
    plt.ylim(-10, 110)


    # res = []
    # for el in one[0]:
    #     res.append(np.sum(np.array(el)))
    # res1 = []
    # for el in two[0]:
    #     res1.append(np.sum(np.array(el)))
    #
    # plt.figure(1)
    # x = np.arange(len(res))
    # plt.scatter(x, res, c="b")
    # x = np.arange(len(res1))
    # plt.scatter(x, res1, c="r")

    plt.show()


# main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None

    # computePOIs()
    # computePerformance();
    compare(number=["167", "164"])
    # one = readFile("one")
    # two = readFile("two")
    # x = [one[1], two[1], one[2], two[2], one[3], two[3], one[4], two[4]]
    # plt.boxplot(x, whis=10)
    # plt.xticks([1, 2, 3, 4, 5, 6, 7, 8],
    #            ['target highest charge 1', 'target highest charge 2', 'target top 5 1', 'target top 5 2',
    #             'target top 10 1', 'target top 10 2', 'length 1', 'length 2'], rotation=7)
    # plt.ylabel("Time steps before the end")

    logging.debug("End Program")
