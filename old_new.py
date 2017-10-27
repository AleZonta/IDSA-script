import logging
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def loadOtherFile(path, nameExp, number):
    listLenght = []
    top = []
    pathFastRead = path + "/" + number + "/" + number + "listlength-" + nameExp + ".txt"
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

    # pathFastRead = path + "/" + number + "/" + number + "numberPoi-" + nameExp + ".txt"
    # numberPoi = []
    # try:
    #     with open(pathFastRead) as f:
    #         for content in f:
    #             value = content.split(" ")
    #             if "\n" in value:
    #                 value.remove("\n")
    #             valueReal = []
    #             for el in value:
    #                 valueReal.append(float(el))
    #             numberPoi.append(valueReal)
    # except:
    #     pass
    # pathFastRead = path + "/" + number + "/" + number + "listTop5-" + nameExp + ".txt"
    # top5 = []
    # with open(pathFastRead) as f:
    #     for content in f:
    #         value = content.split(" ")
    #         if "\n" in value:
    #             value.remove("\n")
    #         valueReal = []
    #         for el in value:
    #             valueReal.append(float(el))
    #         top5.append(valueReal)
    # pathFastRead = path + "/" + number +  "/" + number + "listTop10-" + nameExp + ".txt"
    # top10 = []
    # with open(pathFastRead) as f:
    #     for content in f:
    #         value = content.split(" ")
    #         if "\n" in value:
    #             value.remove("\n")
    #         valueReal = []
    #         for el in value:
    #             valueReal.append(float(el))
    #         top10.append(valueReal)
        pathFastRead = path + "/" + number + "/" + number + "listTop-" + nameExp + ".txt"

        with open(pathFastRead) as f:
            for content in f:
                value = content.split(" ")
                if "\n" in value:
                    value.remove("\n")
                valueReal = []
                for el in value:
                    valueReal.append(float(el))
                top.append(valueReal)
    except:
        pass
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

    return top, listLenght


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    totalNumber = []
    for x in range(1,323):
        totalNumber.append(str(x))

    number = ["314", "315", "316"]
    path = ["/Users/alessandrozonta/Documents/ResultsExp/folderfix/old_new/old", "/Users/alessandrozonta/Documents/ResultsExp/folderfix/old_new/new"]
    # path = ["/Users/alessandrozonta/Documents/ResultsExp/folderfix/newfolder"]

    results = []
    for el in path:
        for nu in number:
            results.append(loadOtherFile(el, "PacmanDistancePath", nu))


    totalMedian = []
    for el in results:
        try:
            median = []
            for y in range(len(el[0][0])):
                median.append((100 * el[0][0][y])/el[1][0][y])
            totalMedian.append(median)
        except:
            pass




    plt.figure(1)
    sns.set(style="white", color_codes=True)
    plt.boxplot(totalMedian, whis=50)
    plt.show()

    logging.debug("End Program")