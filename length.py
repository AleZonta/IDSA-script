import logging
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns

def elab():
    # with open("/Users/alessandrozonta/Documents/Results Exp/traces/traces.txt", "r") as ins:
    #     length_line = []
    #     for line in ins:
    #         length_line.append(len(line.split(';')))
    #
    # nameExp = "PacmanNormal"
    # path = "/Users/alessandrozonta/Documents/Results Exp/400/"
    # path += nameExp
    # listLenght = []
    # pathFastRead = path + "/listlength-" + nameExp + ".txt"
    # try:
    #     with open(pathFastRead) as f:
    #         for content in f:
    #             value = content.split(" ")
    #             if "\n" in value:
    #                 value.remove("\n")
    #             valueReal = []
    #             for el in value:
    #                 valueReal.append(float(el))
    #             listLenght.append(valueReal)
    # except Exception as e:
    #     logging.debug(e.message)
    #
    # average = 0.37
    # length_line_converted = []
    # for el in length_line:
    #     length_line_converted.append(el * average)
    #
    # listLenght_converted = []
    # for el in listLenght[0]:
    #     listLenght_converted.append(el * average)
    #
    # plt.figure(0)
    # sns.distplot(length_line_converted, kde=False, rug=False)
    # plt.xlabel("Length trajectories")
    #
    # plt.figure(1)
    # sns.distplot(listLenght_converted, kde=False, rug=False)
    # plt.xlabel("Length trajectories")
    #
    # plt.show()





    nameExp = "PacmanDistancePath"
    path = "/Users/alessandrozonta/Documents/Results Exp/china/"
    path += nameExp
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

    # 5/10 meters per point
    # average 7.5 meters
    average = 7.5

    listLenght_converted = []
    for el in listLenght[0]:
        listLenght_converted.append(el * average)


    plt.figure(1)
    sns.distplot(listLenght_converted, kde=False, rug=False)
    plt.xlabel("Length trajectories")
    plt.xlim(0,50000)

    plt.show()

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    elab()

    logging.debug("End Program")