import json
import logging
import os
import shutil
import zipfile


def elab():
    path = '/Volumes/TheMaze/idsa/lisa/OutputPacmanDistancePath'
    directories = os.listdir(path)
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
        # subdirectories = os.listdir(path + "/" + str(direct))
        # if ".DS_Store" in subdirectories:
        #     subdirectories.remove(".DS_Store")
        # for el in subdirectories:
        #         subsubdirectories = os.listdir(path + "/" + str(direct) + "/" + str(el))
        #         if ".DS_Store" in subsubdirectories:
        #             subsubdirectories.remove(".DS_Store")
                # for subel in subsubdirectories:
                #     source = path + "/" + str(direct) + "/" + str(el) + "/" + str(subel)
                #     dest = path + "/" + str(direct) + "/" + str(subel)
                #
                #     shutil.move(source, dest)
        # subdirectories = os.listdir(path + "/" + str(direct))
        # if ".DS_Store" in subdirectories:
        #     subdirectories.remove(".DS_Store")
        # logging.debug("Moving the folder {} to idsa".format(path + "/" + str(direct)))
        # for el in subdirectories:
        #     if el != "NotChina":
        #         source = path + "/" + str(direct) + "/" + str(el)
        #         dest = "/Volumes/TheMaze/idsa/lisa/OutputPacmanDistancePath/" + str(direct) + "/" + str(el)
        #         shutil.move(source, dest)

        try:
            subdirectories = os.listdir(path + "/" + str(direct))
            if ".DS_Store" in subdirectories:
                subdirectories.remove(".DS_Store")
            # if len(subdirectories) == 0:
            #     logging.warning(path + "/" + str(direct) + " File non present -> remove folder")
            #     shutil.rmtree(path + "/" + str(direct))
            folderAndSub.append({"number": str(direct), "list": subdirectories})
        except:
            pass

    for y in range(0, len(folderAndSub)):
        count = 0
        total = 0
        for z in range(0, len(folderAndSub[y]["list"])):
            # logging.debug("loading people n {} rules {}".format(z, y))
            namePerson = folderAndSub[y]["list"][z]
            if namePerson != ".DS_Store":
                number = folderAndSub[y]["number"]
    #
    #             # Second file ------------------------------------------------------------------------------------------
    #             # fileName = "/Performance.zip"
    #             # pathLocalSecond = path + "/" + number + "/" + namePerson + fileName
    #             # try:
    #             #     zf = zipfile.ZipFile(pathLocalSecond)
    #             #     filename = "/Performance.JSON"
    #             #     json_data = zf.read(filename)
    #             #     data = json.loads(json_data)
    #             # except:
    #             #     logging.warning(pathLocalSecond + " File non present -> remove folder")
    #             #     shutil.rmtree(path + "/" + number + "/" + namePerson)
    #
                # Third file ------------------------------------------------------------------------------------------
                fileName = "/path.zip"
                pathLocalSecond = path + "/" + number + "/" + namePerson + fileName
                try:
                    zf = zipfile.ZipFile(pathLocalSecond)
                    filename = "/path.JSON"
                    json_data = zf.read(filename)
                    data = json.loads(json_data)
                    coordinates = data["Path"][1].split(",")
                    if 15.125101584012096 < float(coordinates[0]) < 73.24670735552998 and 53.94998853541885 < \
                            float(coordinates[1]) < 135.05707033106097:
                        # logging.warning(pathLocalSecond + "China")
                        count += 1
                        source = path + "/" + number + "/" + namePerson
                        destination = "/Volumes/TheMaze/china/OutputPacmanDistancePath" + "/" + number + "/" + namePerson
                        shutil.move(source, destination)

                        # logging.warning(pathLocalSecond + "Not China")
                    total += 1
                    # logging.warning(pathLocalSecond + " File non correct -> move folder")
                    # shutil.move(path + "/" + number + "/" + namePerson,
                    #             path + "/" + number + "/NotChina/" + namePerson)

                    # bound china -> 73.24670735552998,135.05707033106097,15.125101584012096,53.94998853541885
                except:
                    # logging.warning(pathLocalSecond + " File non present -> remove folder")
                    # shutil.rmtree(path + "/" + number + "/" + namePerson)
                    logging.warning(pathLocalSecond + " Error")
        logging.debug("{} from china on {}".format(count, total))


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    elab()

    logging.debug("End Program")