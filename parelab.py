import json
import logging
import multiprocessing
import os

import sys
import threading
import zipfile

import numpy as np


def worker(folder, subpath):
    listTopPerRule = []
    listTopFivePerRule = []
    listTopTenPerRule = []
    listLength = []
    countPOI = []
    lengthTrajectories = []
    listPerformancePerRule = []

    # for every rules I have to read all the json filesf or every person tracked
    # with this loop I loop inside every folder and I read the performance array of every people
    for z in range(0, len(folder["list"])):
        logging.debug("loading people n {} rules {}".format(z, folder["number"]))
        namePerson = folder["list"][z]
        if namePerson != ".DS_Store":
            number = folder["number"]

            target = ""
            # Third file -------------------------------------------------------------------------------------------
            fileName = "/path.zip"
            pathLocalThird = subpath + "/" + number + "/" + namePerson + fileName
            try:
                zf = zipfile.ZipFile(pathLocalThird)
                filename = "/path.JSON"
                zipdata = zf.read(filename)
                json_data = zipdata.replace("(", '"').replace(")", '"')
                data = json.loads(json_data)
                # check length trajectory tracked
                lengthTrajectories.append(len(data["Path"]))
                target = data["Path"][len(data["Path"]) - 1]
            except:
                logging.warning(pathLocalThird + " File non present of person number {}".format(z))


            # First file -------------------------------------------------------------------------------------------
            fileName = "/POIs.zip"
            pathLocal = subpath + "/" + number + "/" + namePerson + fileName
            # totalList.append(pathLocal)
            try:
                zf = zipfile.ZipFile(pathLocal)
                filename = "/POIs.JSON"
                zipdata = zf.read(filename)
                json_data = zipdata.replace("(", '"').replace(")", '"')
                data = json.loads(json_data)
                listTopPerRule.append(findForHowLong(data, target))
                listTopFivePerRule.append(findTopFive(data, target))
                listTopTenPerRule.append(findTopTen(data, target))
                # how many time step I tracked the person
                listLength.append(len(data["POIsCharge"]))
                # count the number of the POI
                countPOI.append(len(data['POIsLocation']))
            except:
                logging.warning(pathLocal + " File non present of person number {}".format(z))

            # Second file ------------------------------------------------------------------------------------------
            fileName = "/Performance.zip"
            pathLocalSecond = subpath + "/" + number + "/" + namePerson + fileName
            try:
                zf = zipfile.ZipFile(pathLocalSecond)
                filename = "/Performance.JSON"
                json_data = zf.read(filename)
                data = json.loads(json_data)
                try:
                    listPerformancePerRule.append(np.array(data["Perf"]))
                except:
                    listPerformancePerRule.append(np.array(data))

            except:
                logging.warning(pathLocalSecond + " File non present of persnn number {}".format(z))

            logging.debug(
                "----------------------> {} {} {} {} {} {}".format(len(listTopPerRule), len(listTopFivePerRule),
                                                                   len(listTopTenPerRule), len(listLength),
                                                                   len(countPOI), len(listPerformancePerRule)))


    # a single data contains the charge and the position of all the POIs at every time steps
    # listPerformancePerRule contains for how many time from the end the highest POI was the target per person
    # totalList keep track of the sum/mean/standardDeviation and variance per rule of that value
    vect = listTopPerRule
    secVect = listLength
    top5Vect = listTopFivePerRule
    top10Vect = listTopTenPerRule

    logging.debug("Added line to table file...")
    with open(subpath + "/" + str(folder["number"]) + "listTop5-" + nameExp + ".txt", 'a') as h:
        for el in top5Vect:
            h.write("{} ".format(el))
        h.write("\n")
    logging.debug("Added line to top5 file...")

    with open(subpath + "/" + str(folder["number"]) + "listTop10-" + nameExp + ".txt", 'a') as i:
        for el in top10Vect:
            i.write("{} ".format(el))
        i.write("\n")
    logging.debug("Added line to top10 file...")

    with open(subpath + "/" + str(folder["number"]) + "listTop-" + nameExp + ".txt", 'a') as l:
        for el in vect:
            l.write("{} ".format(el))
        l.write("\n")
    logging.debug("Added line to target file...")

    with open(subpath + "/" + str(folder["number"]) + "listLength-" + nameExp + ".txt", 'a') as m:
        for el in secVect:
            m.write("{} ".format(el))
        m.write("\n")
    logging.debug("Added line to times tep file...")

    with open(subpath + "/" + str(folder["number"]) + "numberPoi-" + nameExp + ".txt", 'a') as n:
        for el in countPOI:
            n.write("{} ".format(el))
        n.write("\n")
    logging.debug("Added line to number of POI file...")

    # with open(subpath + "/lengthTracks-" + nameExp + ".txt", 'a') as o:
    #     for el in lengthTrajectories:
    #         o.write("{} ".format(el))
    #     o.write("\n")
    # logging.debug("Added line to length of tracking file...")

    # compute integral of all the trajectories
    value = []
    for el in listPerformancePerRule:
        value.append(np.sum(el))

    with open(subpath + "/" + str(folder["number"]) + "Performance-" + nameExp + ".txt", 'a') as p:
        for el in value:
            p.write("{} ".format(el))
        p.write("\n")
    logging.debug("Added line to performance file...")


# find the highest charge in data
def findForHowLong(data, targetq):
    # target = data["target"]
    target = targetq
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
def findTopFive(data, targetq):
    target = data["target"]
    target = targetq
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
def findTopTen(data, targetq):
    target = data["target"]
    target = targetq
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


def preprocess(path, name):
    subpath = path + "/Output" + name
    directories = os.listdir(subpath)

    list = []
    for el in directories:
        try:
            v = int(el)
            list.append(v)
        except:
            pass
    list.sort()
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    folderAndSub = []
    for direct in list:
        try:
            subdirectories = os.listdir(subpath + "/" + str(direct))
            folderAndSub.append({"number": str(direct), "list": subdirectories})
        except:
            pass

    # in folder and sub now I have all the folder corresponding to the rules and for each rules I have the 30
    #  people tracked
    logging.debug(" {} folder".format(len(folderAndSub)))

    # appo = []
    # for el in folderAndSub:
    #     if el["number"] == "314" or el["number"] == "315" or el["number"] == "316":
    #         appo.append(el)

    # for el in appo:ls
    #     worker(el, subpath)
    jobs = []
    for el in folderAndSub:
        t = multiprocessing.Process(target=worker, args=(el, subpath, ))
        jobs.append(t)
        t.start()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    print(sys.argv)
    path = sys.argv[1]
    nameExp = sys.argv[2]

    preprocess(path, nameExp)

    logging.debug("End Program")
