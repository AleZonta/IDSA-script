import json
import logging
import os
import zipfile
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# find the highest charge in data
from pandas import DataFrame


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


def read_files(path):
    directories = os.listdir(path)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")

    listTopPerRule = []
    listLength = []
    countPOI = []
    listPerformancePerPerson = []

    for el in directories:
        # logging.debug("laoding {}".format(el))
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
            # how many time step I tracked the person
            listLength.append(len(data["POIsCharge"]))
            # count the number of the POI
            countPOI.append(len(data['POIsLocation']))
        except:
            logging.warning(pathLocal + " File non present")

    return listTopPerRule, listLength, countPOI, listPerformancePerPerson


def fight(number, name, old):
    if old:
        logging.debug("Which setting am I checking? -> Old Version ")
    else:
        logging.debug("Which setting am I checking? -> New Angle")
    idsa = "/Volumes/TheMaze/Results/single_eq/idsa/" + name + "/" + number
    if old:
        idsa = "/Volumes/TheMaze/Results/smart-ct2017/idsa/" + name + "/" + number
    geoset = "/Volumes/TheMaze/Results/single_eq/geoset/" + name + "/" + number
    if old:
        geoset = "/Volumes/TheMaze/Results/smart-ct2017/china/" + name + "/" + number

    logging.debug("Reading IDSA")
    listTopPerRuleIdsa, listLengthIdsa, countPOIIdsa, listPerformancePerPersonIdsa = read_files(idsa)

    logging.debug("Reading Geolife")
    listTopPerRuleGeoset, listLengthGeoset, countPOIGeoset, listPerformancePerPersonGeoset = read_files(geoset)

    realTop = []
    for x in range(len(listTopPerRuleIdsa)):
        realTop.append((100 * listTopPerRuleIdsa[x]) / listLengthIdsa[x])
        # realTop.append(listTopPerRuleIdsa[x])

    for x in range(len(listTopPerRuleGeoset)):
        realTop.append((100 * listTopPerRuleGeoset[x]) / listLengthGeoset[x])
        # realTop.append(listTopPerRuleGeoset[x])

    realLength = []
    for el in listLengthIdsa:
        realLength.append(el)
    for el in listLengthGeoset:
        realLength.append(el)

    realPOI = []
    for el in countPOIIdsa:
        realPOI.append(el)
    for el in countPOIGeoset:
        realPOI.append(el)

    dataset = []
    realP = []
    for el in listPerformancePerPersonIdsa:
        realP.append(el)
        dataset.append("Idsa")
    for el in listPerformancePerPersonGeoset:
        realP.append(el)
        dataset.append("Geosat")

    return realTop, realLength, realPOI, realP, dataset
    # zz = {"Performance": realTop, "Length": realLength, "NumberPOI": realPOI, "Perf": realP, "Dataset": dataset}
    # dfs = DataFrame(data=zz)

    # lmplot
    # sns.lmplot("Length", "Performance", data=dfs, hue='Dataset', fit_reg=False)
    # sns.despine(trim=True)
    # # dfs.to_csv("lengthNew.csv")
    #
    # plt.show()


def old_vs_new():
    # result = None
    # old False 363 OutputPacmanDistance
    # old True 87 PacmanDistance
    realTop, realLength, realPOI, realP, dataset = fight(number="363", name="OutputPacmanDistance", old=False)
    realTopOld, realLengthOld, realPOIOld, realPOld, datasetOld = fight(number="87", name="PacmanDistance", old=True)

    top = []
    length = []
    poi = []
    p = []
    dat = []
    age = []
    for x in range(len(realTop)):
        top.append(realTop[x])
        length.append(realLength[x])
        poi.append(realPOI[x])
        p.append(realP[x])
        dat.append(dataset[x])
        age.append("New")

    for x in range(len(realTopOld)):
        top.append(realTopOld[x])
        length.append(realLengthOld[x])
        poi.append(realPOIOld[x])
        p.append(realPOld[x])
        dat.append(datasetOld[x])
        age.append("Old")

    zz = {"Performance": top, "Length": length, "NumberPOI": poi, "Perf": p, "Dataset": dat, "Age": age}
    dfs = DataFrame(data=zz)
    # dfs.to_csv("lengt.csv")

    plt.figure(0)
    for el in realP:
        x = np.arange(len(el))
        plt.plot(x, el)

    plt.figure(1)
    for el in realPOld:
        x = np.arange(len(el))
        plt.plot(x, el)

    plt.show()

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    # realTopOld, realLengthOld, realPOIOld, realPOld, datasetOld = fight(number="87", name="PacmanDistance", old=True)
    #
    # zz = {"Performance": realTopOld, "Length": realLengthOld, "NumberPOI": realPOIOld, "Perf": realPOld, "Dataset": datasetOld}
    # dfs = DataFrame(data=zz)
    #
    # idsa_section = dfs[dfs["Dataset"] == "Idsa"]
    # median = np.median(idsa_section["Performance"])
    # count = 0
    # for el in idsa_section["Performance"]:
    #     if el >= median:
    #         count += 1
    # print count
    # print len(idsa_section["Performance"])

    old_vs_new()

    logging.debug("End Program")
