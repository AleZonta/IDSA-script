import logging
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def elab():
    listLenght = []
    pathFastRead = "/Users/alessandrozonta/Documents/ResultsExp/folderfix/old_new/new/314/314listLength-PacmanDistancePath.txt"
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

    average = 7.5

    listLenght_converted = []
    for el in listLenght[0]:
        listLenght_converted.append(el * average)


    plt.figure(1)
    sns.distplot(listLenght_converted, bins=90, kde=False, rug=False)
    plt.xlabel("Length trajectories")
    plt.ylim(0, 100)


    nameExp = "PacmanDistancePath"
    path = "/Users/alessandrozonta/Documents/ResultsExp/china/"
    path += nameExp
    listLenght2 = []
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
                    listLenght2.append(valueReal)
    except Exception as e:
        logging.debug(e.message)

    # 5/10 meters per point
    # average 7.5 meters
    average = 7.5

    listLenght_converted = []
    for el in listLenght2[0]:
        listLenght_converted.append(el * average)

    plt.figure(2)
    sns.distplot(listLenght_converted, bins=400, kde=False, rug=False)
    plt.xlabel("Length trajectories")
    plt.ylim(0, 100)
    plt.xlim(0, 60000)

    plt.show()


def elab2():
    listLenght = []
    pathFastRead = "/Volumes/TheMaze/Results/newDas5/china/PacmanDistancePath/distance-PacmanDistancePath.txt"
    try:
        with open(pathFastRead) as f:
            for content in f:
                value = content.split(" ")
                if "\n" in value:
                    value.remove("\n")
                valueReal = []
                for el in value:
                    valueReal.append(float(el))
                listLenght = valueReal
    except Exception as e:
        logging.debug(e.message)

    logging.debug(listLenght)
    fin = np.array(listLenght)
    logging.debug("Max -> {}".format(np.amax(fin)))
    logging.debug("Min -> {}".format(np.amin(fin)))
    logging.debug("Median -> {}".format(np.median(fin)))
    # plt.figure(0)
    # sns.distplot(listLenght, kde=False, rug=False)
    # plt.xlabel("Length trajectories")
    # plt.show()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    elab2()

    logging.debug("End Program")