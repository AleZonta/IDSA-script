# main
import json
import logging
import os
import zipfile

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from math import fabs, exp

from pandas import DataFrame
from scipy.spatial.distance import squareform, pdist


def read_files(path, perc):
    directories = os.listdir(path)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")

    countPOI = []

    distance_for_all_the_people = []
    for el in directories:
        fileName = "/POIs.zip"
        pathLocal = path + "/" + el + fileName
        # totalList.append(pathLocal)
        try:
            zf = zipfile.ZipFile(pathLocal)
            filename = "/POIs.JSON"
            zipdata = zf.read(filename)
            json_data = zipdata.replace("(", '"').replace(")", '"')
            data = json.loads(json_data)
            # how many time step I tracked the person
            total_len = len(data["POIsCharge"])
            real_perc = []
            for el in perc:
                real_perc.append(int(float(el)/100 * total_len))
            real_perc[len(real_perc)-1] -= 1
            target = data["target"]
            pois = data["POIsLocation"]
            distance = []
            for el in real_perc:
                array = data["POIsCharge"][el]
                ind = np.argmax(array)
                highest_charged = pois[ind]
                target_list = target.split(",")
                highest_charged_list = highest_charged.split(",")
                distance.append(np.math.hypot(float(target_list[0]) - float(highest_charged_list[0]), float(target_list[1]) - float(highest_charged_list[1])))
            distance_for_all_the_people.append(distance)

            # count the number of the POI
            countPOI.append(len(data['POIsLocation']))
        except:
            logging.warning(pathLocal + " File non present")

    return distance_for_all_the_people


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    geoset = "/Volumes/TheMaze/Results/single_eq/geoset/OutputPacmanDistance/363/"
    idsa = "/Users/alessandrozonta/Documents/ResultsExp/newangle/idsa/OutputPacmanDistance/363/"

    perc = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    dist = read_files(geoset, perc)

    distance = []
    for el in perc:
        vect = []
        distance.append(vect)

    for el in dist:
        for x in range(len(el)):
            distance[x].append(float(el[x]))

    real_dist = []
    real_perc = []
    for x in range(len(distance)):
        for el in dist[x]:
            real_dist.append(float(el))
            real_perc.append(perc[x])




    zz = {"Percentage": real_perc, "Distance": real_dist}
    dfs = DataFrame(data=zz)
    dfs.to_csv("accuracy.csv")

    sns.lmplot("Percentage", "Distance", data=dfs, x_jitter=.8 )
    sns.despine(trim=True)
    # plt.xscale('log')

    # sns.violinplot(x="Percentage", y="Distance", data=dfs)
    # sns.despine(trim=True)

    plt.show()


    logging.debug("End Program")
