import matplotlib.pyplot as plt
import numpy as np


def circ_diag(n):
    labels = ['Part' + str(i) for i in range(1, n + 1)]
    values = np.random.randint(1, 100, n)
    plt.pie(values, labels=labels)
    plt.show()


circ_diag(int(input()))
