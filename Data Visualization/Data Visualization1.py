import matplotlib.pyplot as plt
import numpy as np
import csv


def analyzeBirths():
    years = range(1880, 2012)
    pieces = []
    datafile = 'DataSemple.csv'
    with open(datafile, 'rt', encoding='utf-8-sig') as f:
        data = csv.reader(f, delimiter='\t')
        for d in data:
            pieces.append(d)

    p1 = plt.plot(x, y1, "r^--", label='female')
    p2 = plt.plot(x, y2, 'bs^--', label='male ')
    plt.show()


if __name__ == "__main__":
    analyzeBirths()
