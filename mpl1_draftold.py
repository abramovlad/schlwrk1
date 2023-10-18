import matplotlib.pyplot as plt
import numpy as np
# в разработке

def lines():
    x = np.array([-20, 20])
    print('Формула графика y1:')
    exec(input())
    print('Формула графика y2:')
    exec(input())
    plt.title('Линейные функции:')
    plt.xlabel('x')
    plt.ylabel('y1, y2')
    plt.grid()
    plt.plot([x, x], [y1, y2])
    plt.legend()
    plt.show()


lines()



