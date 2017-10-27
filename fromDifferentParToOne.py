import json
import logging

import sys


def elab(path):
    for x in range(1, 244):
        localPath = path + '/par' + str(x)
        json_data = open(localPath).read()
        data = json.loads(json_data)
        f = open(path + "/param", 'a')
        f.write(str(data["Alpha"]) + " " + str(data["s1"]) + " " + str(data["w1"]) + " " + str(data["s2"]) + " " + str(
            data["w2"]) + " " + str(data["Name"]) + " " + str(data["Exp"]) + " " + str(data["Number"]) + " " + str(
            data["UR"]) + "\n")
        f.close()
        logging.debug("Wrote number {}".format(x))

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    print(sys.argv)
    deb = sys.argv[1]


    elab(deb)

    logging.debug("End Program")