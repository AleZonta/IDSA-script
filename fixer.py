import logging
import os

import datetime
import shutil


def compute():
    source = "/Volumes/TheMaze/china_160_800_fix/OutputPacmanDistancePath160000"
    dest = "/Volumes/TheMaze/china_160_800_fix/OutputPacmanDistancePath800000"

    # find directory on source (0 , 1 ,.....,323)
    directories = os.listdir(source)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")

    # save name and order normally
    list = []
    for el in directories:
        try:
            v = int(el)
            list.append(v)
        except:
            pass
    list.sort()

    # find sub folder (folder with the name of the tracked people)
    folderAndSub = []
    for direct in list:
        try:
            subdirectories = os.listdir(source + "/" + str(direct))
            if ".DS_Store" in subdirectories:
                subdirectories.remove(".DS_Store")
            totalDiffernece = []
            for el in subdirectories:
                time = os.stat(source + "/" + str(direct) + "/" + str(el)).st_birthtime
                ttime = str(time)[:7]
                if ttime not in totalDiffernece:
                    totalDiffernece.append(ttime)
            logging.debug("details folder {} -> {}".format(source + "/" + str(direct), totalDiffernece))
            if len(totalDiffernece) == 3:
                logging.debug("Len 2, moving the older folders")
                c = 0
                for el in subdirectories:
                    time = os.stat(source + "/" + str(direct) + "/" + str(el)).st_birthtime
                    ttime = str(time)[:7]
                    if ttime == totalDiffernece[2]:
                        shutil.move(source + "/" + str(direct) + "/" + str(el), dest + "/" + str(direct) + "/" + str(el))
                        c += 1
                logging.debug("Moved {} folder".format(c))
            # folderAndSub.append({"number": str(direct), "list": subdirectories})
        except:
            pass


# main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None
    # if general:
    # computeGeneral()
    # else:
    compute()
    # differentCompute()
    logging.debug("End Program")
