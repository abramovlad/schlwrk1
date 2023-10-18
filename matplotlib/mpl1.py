import matplotlib.pyplot as plt
import numpy as np


def lines():
    x = np.array([-20, 20])
    plt.title('Линейные функции:')
    plt.xlabel('x')
    plt.ylabel('y1, y2')
    plt.grid()
    plt.plot(x, eval(input('Формула графика 1: y1 = ')))
    plt.plot(x, eval(input('Формула графика 2: y2 = ')))
    plt.legend()
    plt.show()


lines()



