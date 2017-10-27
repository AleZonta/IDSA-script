
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
import seaborn as sns


def loadOtherFile(path, nameExp):
    listLenght = []
    path += nameExp
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


# main
if __name__ == "__main__":
    # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # logging.debug("Starting Program")
    # result = None

    listLength50, numberPoi50, top550, top1050, top50, perf50 = loadOtherFile(
        "/Volumes/TheMaze/Results/smart-ct2017/brandnew/das/50/", "PacmanDistance")

    listLength100, numberPoi100, top5100, top10100, top100, perf100 = loadOtherFile(
        "/Users/alessandrozonta/Documents/ResultsExp/latest/idsa/", "PacmanDistance")

    listLength200, numberPoi200, top5200, top10200, top200, perf200 = loadOtherFile(
        "/Users/alessandrozonta/Documents/ResultsExp/latest/200idsa/", "PacmanDistance")

    listLength50b, numberPoi50b, top550b, top1050b, top50b, perf50b = loadOtherFile(
        "/Volumes/TheMaze/Results/smart-ct2017/brandnew/lisa/50/", "PacmanDistance")

    listLength100b, numberPoi100b, top5100b, top10100b, top100b, perf100b = loadOtherFile(
        "/Users/alessandrozonta/Documents/ResultsExp/latest/china/", "PacmanDistance")

    listLength200b, numberPoi200b, top5200b, top10200b, top200b, perf200b = loadOtherFile(
        "/Users/alessandrozonta/Documents/ResultsExp/latest/200china/", "PacmanDistance")

    median = []
    realTop = []
    for x in range(len(top50)):
        appo = []
        try:
            for y in range(len(top50[x])):
                appo.append((100 * top50[x][y]) / listLength50[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    realTop = []
    for x in range(len(top100)):
        appo = []
        try:
            for y in range(len(top100[x])):
                appo.append((100 * top100[x][y]) / listLength100[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))
    #
    realTop = []
    for x in range(len(top200)):
        appo = []
        try:
            for y in range(len(top200[x])):
                appo.append((100 * top200[x][y]) / listLength200[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    realTop = []
    for x in range(len(top50b)):
        appo = []
        try:
            for y in range(len(top50b[x])):
                appo.append((100 * top50b[x][y]) / listLength50b[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    realTop = []
    for x in range(len(top100)):
        appo = []
        try:
            for y in range(len(top100b[x])):
                appo.append((100 * top100b[x][y]) / listLength100b[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    realTop = []
    for x in range(len(top200)):
        appo = []
        try:
            for y in range(len(top200b[x])):
                appo.append((100 * top200b[x][y]) / listLength200b[x][y])
        except:
            pass
        realTop.append(appo)
    for el in realTop:
        median.append(np.median(el))

    different = []
    totalPOIs = []
    for el in numberPoi50:
        different.append("IDSA")
        totalPOIs.append(np.median(el))
    for el in numberPoi100:
        different.append("IDSA")
        totalPOIs.append(99)
    for el in numberPoi200:
        different.append("IDSA")
        totalPOIs.append(262)
    for el in numberPoi50b:
        different.append("Geolife")
        totalPOIs.append(np.median(el))
    for el in numberPoi100b:
        different.append("Geolife")
        totalPOIs.append(75)
    for el in numberPoi200b:
        different.append("Geolife")
        totalPOIs.append(210)


    zz = {"data": median, "pois": totalPOIs, "dataset": different}
    dfs = DataFrame(data=zz)

    # sns.set(style="white", color_codes=True)

    # plt.figure(1)
    sns.set(font_scale=1.3)
    g = sns.lmplot(x="pois", y="data", data=dfs, x_jitter=.05, hue="dataset")
    # plt.figure(2)
    # sns.regplot(x="pois", y="data", hue="different", data=dfs)
    plt.xlabel("Number of POIs")
    plt.ylabel("Performance (%)")
    plt.xlim(0, 310)

    plt.show()

    # logging.debug("End Program")
