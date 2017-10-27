import json
import logging
import os
import zipfile


def elab():
    name_folder = 'OutputPacmanDistance'
    selected_track = 145
    first_folder = '140'
    second_folder = '220'
    third_folder = '300'
    base_folder = '60'

    logging.debug("folder {} number {}".format(base_folder, selected_track))
    path = '/Users/alessandrozonta/Documents/Results Exp/folderfix/'

    base_path = path + name_folder + "/" + base_folder
    directories = os.listdir(base_path)

    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    selected_folder = directories[selected_track]
    file_name = "/path.zip"
    path_local = base_path + "/" + selected_folder + "/" + file_name
    zf = zipfile.ZipFile(path_local)
    filename = "/path.JSON"
    zipdata = zf.read(filename)
    json_data = zipdata.replace("(", '"').replace(")", '"')
    base_data = json.loads(json_data)
    base_data = base_data["Path"]

    base_path = path + name_folder + "/" + first_folder
    logging.debug("folder {} number {}".format(first_folder, ret_position(base_path, base_data)))
    base_path = path + name_folder + "/" + second_folder
    logging.debug("folder {} number {}".format(second_folder, ret_position(base_path, base_data)))
    base_path = path + name_folder + "/" + third_folder
    logging.debug("folder {} number {}".format(third_folder, ret_position(base_path, base_data)))


def ret_position(base_path, base_data):
    directories = os.listdir(base_path)
    if ".DS_Store" in directories:
        directories.remove(".DS_Store")
    count = 0
    for el in directories:
        file_name = "/path.zip"
        path_local = base_path + "/" + el + "/" + file_name
        zf = zipfile.ZipFile(path_local)
        filename = "/path.JSON"
        zipdata = zf.read(filename)
        json_data = zipdata.replace("(", '"').replace(")", '"')
        second_data = json.loads(json_data)
        second_data = second_data["Path"]
        if base_data == second_data:
            return count
        count += 1
    return None

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    elab()

    logging.debug("End Program")