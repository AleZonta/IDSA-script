# main
import logging
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from math import fabs, exp


# angle function increment/decrement
def define_charnge_in_charge(current_angle, h, z1, z2):
    return 10 * exp(-z1 * fabs(current_angle)) - 10 * h * exp(-z2 * (180 - fabs(current_angle)))


def old_alpha(current_angle, z1, z2):
    return z1 * exp(current_angle * z2)



def compute():
    results = []
    sns.set(font_scale=1.5)
    h = [0.5, 1.0, 2.0, 5.0, 10.0]
    z2 = [0.01, 0.1, 0.2, 0.5]
    z1 = [0.01, 0.1, 0.2, 0.5]

    for el in h:
        for eel in z2:
            for eeel in z1:
                results_v0 = []
                for x in range(181):
                    results_v0.append(define_charnge_in_charge(x, el, eeel, eel))
                results.append(results_v0)

    cmap = plt.get_cmap('gnuplot')
    colors = [cmap(i) for i in np.linspace(0, 1, len(results))]
    elem = []

    i = 0
    for el in results:
        x = np.arange(181)
        elem.append(plt.scatter(x, el, c=colors[i]))
        i+=1

    plt.xlim(-10, 190)
    plt.ylim(-20, 20)
    plt.xlabel("degree")
    plt.ylabel("change in charge")
    plt.show()


def best():
    results = []
    sns.set(font_scale=1.5)
    h = [1.0]
    z2 = [0.03]
    z1 = [0.003]

    for el in h:
        for eel in z2:
            for eeel in z1:
                results_v0 = []
                xx = np.arange(0,181,0.25)
                for x in xx:
                    results_v0.append(define_charnge_in_charge(x, el, eeel, eel))
                results.append(results_v0)

    z2 = [0.04]
    z1 = [0.004]

    for el in h:
        for eel in z2:
            for eeel in z1:
                results_v0 = []
                xx = np.arange(0, 181, 0.25)
                for x in xx:
                    results_v0.append(define_charnge_in_charge(x, el, eeel, eel))
                results.append(results_v0)

    z2 = [0.02]
    z1 = [0.002]

    for el in h:
        for eel in z2:
            for eeel in z1:
                results_v0 = []
                xx = np.arange(0, 181, 0.25)
                for x in xx:
                    results_v0.append(define_charnge_in_charge(x, el, eeel, eel))
                results.append(results_v0)

    z2 = [0.01]
    z1 = [0.001]

    for el in h:
        for eel in z2:
            for eeel in z1:
                results_v0 = []
                xx = np.arange(0, 181, 0.25)
                for x in xx:
                    results_v0.append(define_charnge_in_charge(x, el, eeel, eel))
                results.append(results_v0)

    z2 = [0.05]
    z1 = [0.005]

    for el in h:
        for eel in z2:
            for eeel in z1:
                results_v0 = []
                xx = np.arange(0, 181, 0.25)
                for x in xx:
                    results_v0.append(define_charnge_in_charge(x, el, eeel, eel))
                results.append(results_v0)




    cmap = plt.get_cmap('gnuplot')
    colors = [cmap(i) for i in np.linspace(0, 1, len(results))]
    elem = []

    i = 0
    for el in results:
        x = np.arange(0,181,0.25)
        elem.append(plt.scatter(x, el, c=colors[i]))
        i += 1

    plt.legend(("0.003/0.03 [I=13.16% G=32.65%]", "0.004/0.04 [I=12.84% G=32.10%]", "0.002/0.02 [I=12.52%; G=32.9%]", "0.001/0.01 [I=12.49% G=32.30%]", "0.005/0.05 [I=11.29% G=30.85%]"))
    plt.xlim(-10, 190)
    plt.ylim(-10, 15)
    plt.xlabel("degree")
    plt.ylabel("change in charge")
    plt.show()


def oldFunction(total):

    sns.set(font_scale=1.5)
    z2 = [0.01, 0.1, 0.2, 0.5]
    z1 = [0.01, 0.1, 0.2, 0.5]
    angle = [30, 60, 90, 120, 180, 240]
    if total:
        results = []

    for pos_angle in range(len(angle)):
        if not total:
            results = []
        for eel in z2:
            for eeel in z1:
                results_v0 = []
                value_positive = angle[pos_angle] / 2
                value_negative = (360 - angle[pos_angle]) / 2
                for x in range(value_positive):
                    results_v0.append(old_alpha(x, eeel, eel))
                for x in reversed(range(value_positive)):
                    results_v0.append(old_alpha(x, eeel, eel))
                for x in range(value_negative):
                    results_v0.append(-old_alpha(x, eeel, eel))
                for x in reversed(range(value_negative)):
                    results_v0.append(-old_alpha(x, eeel, eel))
                results.append(results_v0)

        cmap = plt.get_cmap('gnuplot')
        colors = [cmap(i) for i in np.linspace(0, 1, len(results))]

        if not total:
            plt.figure(pos_angle)
        i = 0
        for el in results:
            x = np.arange(len(el))
            plt.scatter(x, el, c=colors[i])
            i += 1

        plt.xlabel("degree")
        plt.ylabel("change in charge")
        plt.yscale("symlog")
    plt.show()

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


    #compute()

    best()

    # oldFunction(total=True)

    logging.debug("End Program")
