import filecmp
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import logging
import scipy.interpolate

import math

import seaborn as sns
import numpy
from matplotlib import cm


def compute():
    # fake data:
    # i = 5.0
    # q = 5.0
    #
    # print "Cartesian: (%.1f,%.1f)" % (i, q)
    # print "Polar: r = %.1f" % math.sqrt(math.pow(i, 2) + math.pow(q, 2)) + ", Theta = %.1f" % math.degrees(
    #     math.atan(q / i)) + " degrees"
    aa = np.linspace(1, 6, 10)

    x = [6, 8, 6, 3, -2, -3, -5, -3, -1, 1, 3, 2, 3, 4, 5, 6, 1, 1, 1, 1, 0, 0.99, -2, -1, -3, 6, 5, 4, -4, -2, -3, -3, -1, 3, 2, 0, 7, 8, 1.5, 2.5, 3.5, 4.5, 1, 1, 1, 1, 1, 1]
    y = [3, 1, -2, -5, -5, -3, -1, 2, 4, 6, 5, 1, 1, 1, 1, 1, 5, 4, 3, 2, 0, 0.99, -2, -1, -3, -4, -3, -2, 6, 4, 5, 3, 2, -2, -1, -4, 7, 8, 1, 1, 1, 1, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    c = [21.80, 0, -30.96, -71.56, -116.67, -135, -108.43, -75.96, -33.69, 0, 26.56, 0, 0, 0, 0, 0, 0, 0, 0, 0, -135, -135, -135, -135, -135, -45, -45, -45, -45, -45, -45, -63.44, -63.44, -56.30, -63.44, -101.3, 45, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    cc = []
    for ppp in range(len(aa)):
        cc.append(45)

    x = np.concatenate((aa, x))
    y = np.concatenate((aa, y))
    c = np.concatenate((cc, c))

    # z = []
    # for q in range(len(x)):
    #     z.append(math.sqrt(math.pow(x[q], 2) + math.pow(y[q], 2)))


    # A, B = np.meshgrid(x, y)
    # d = np.random.random(A.shape)


    ccccccccc = []
    for el in c:
        # if el < 0:
            ccccccccc.append(el)
        # else:
        #     ccccccccc.append((((el - 0) * (135 - 0)) / (45 - 0)) + 0)


    s = 1.0
    w = 0.01
    cdcd = []
    for el in c:
        cdcd.append(s * math.exp(math.fabs(el) * w))

    cdcdcdcd = []
    for x1 in range(len(cdcd)):
        if c[x1] > 0:
            cdcdcdcd.append(cdcd[x1])
        else:
            cdcdcdcd.append(-cdcd[x1])


    xi, yi = np.linspace(np.min(x), np.max(x), 1000), np.linspace(np.min(y), np.max(y), 1000)
    xi, yi = np.meshgrid(xi, yi)
    rbf = scipy.interpolate.Rbf(x, y, cdcdcdcd, function='linear')
    zi = rbf(xi, yi)

    fig = plt.figure(0)
    figr = fig.add_subplot(111)
    # plt.imshow(zi, vmin=np.min(c), vmax=np.max(c), origin='lower',
    #            extent=[np.min(x), np.max(x), np.min(y), np.max(y)], cmap=cm.Greys)
    plt.imshow(zi, vmin=np.min(cdcdcdcd), vmax=np.max(cdcdcdcd), origin='lower',
               extent=[np.min(x), np.max(x), np.min(y), np.max(y)], cmap=cm.RdYlBu)
    plt.colorbar()
    plt.clim(-4, 4)
    figr.set_yticklabels([])
    figr.set_xticklabels([])

    # a = np.linspace(0, 2 * np.pi, 50)
    # logging.debug(a)
    # b = np.linspace(0, 1, 50)
    # logging.debug(b)
    # A, B = np.meshgrid(a, b)
    # c = np.random.random(A.shape)
    # logging.debug(c)
    #
    # # actual plotting
    # import matplotlib.cm as cm
    # ax = plt.subplot(111, polar=True)
    # ax.set_yticklabels([])
    # ctf = ax.contourf(x, y, d, cmap=cm.jet)
    # plt.colorbar(ctf)
    plt.show()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    # result = None
    compute()
    logging.debug("End Program")
