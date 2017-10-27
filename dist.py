import json
import logging
import os

import sys
import zipfile

from decimal import Decimal
from haversine import haversine


def preprocess(path, name):
    subpath = path + "/" + name
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
    logging.debug(len(folderAndSub))

    realList = []

    for x in range(0, len(folderAndSub)):
        realList.append({"list": folderAndSub[x]})

    count = 0
    # loop for all the rules
    for y in range(0, len(realList)):
        listRealDistance =[]
        for z in range(0, len(realList[y]["list"]["list"])):
            logging.debug("loading people n {} rules {}".format(z, y))
            namePerson = realList[y]["list"]["list"][z]
            if namePerson != ".DS_Store":
                number = realList[y]["list"]["number"]
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
                    if data["Path"][0].split(",")[0] == '0.0':
                        list = data["Path"][1:]
                    else:
                        list = data["Path"]
                    first = list[0]
                    list = list[1:]
                    total = 0.0
                    first_coord_x = Decimal(first.split(",")[0])
                    first_coord_y = Decimal(first.split(",")[1])
                    for el in list:
                        second_coord_x = Decimal(el.split(",")[0])
                        second_coord_y = Decimal(el.split(",")[1])
                        total += haversine((first_coord_x, first_coord_y), (second_coord_x,second_coord_y)) * 1000
                        first_coord_x = second_coord_x
                        first_coord_y = second_coord_y
                    # logging.debug(total)
                    listRealDistance.append(total)
                except:
                    logging.warning(pathLocalThird + " File non present of person number {}".format(z))
        with open(subpath + "/distance-" + name + ".txt", 'a') as h:
            for el in listRealDistance:
                h.write("{} ".format(el))
            h.write("\n")
        logging.debug("Added line to Distance file...")
        return
# main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None
    # if general:
    # computeGeneral()
    # else:
    print(sys.argv)

    # path = sys.argv[1]
    # nameExp = sys.argv[2]

    preprocess("/Volumes/TheMaze/Results/latest/idsa/", "OutputPacmanDistancePath")
    # differentCompute()
    logging.debug("End Program")