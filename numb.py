import filecmp
import json
import os
import matplotlib.pyplot as plt
import numpy as np

import inspect
import seaborn as sns
import numpy

def compute():
    filename = 'numb.py'
    try:
        (name, suffix, mode, mtype) = inspect.getmoduleinfo(filename)
    except TypeError:
        print 'Could not determine module type of %s' % filename
    pass

# main
if __name__ == "__main__":
    # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None
    compute()
    # logging.debug("End Program")