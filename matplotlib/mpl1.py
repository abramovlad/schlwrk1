import matplotlib.pyplot as plt
import numpy as np

x = np.array([-20, 20])


def lines(y1, y2):
    plt.title('Линейные функции:')
    plt.xlabel('x')
    plt.ylabel('y1, y2')
    plt.grid()
    plt.plot(x, eval(y1))
    plt.plot(x, eval(y2))
    plt.legend()
    plt.show()


lines(input('Формула графика 1: y1 = '), input('Формула графика 2: y2 = '))
