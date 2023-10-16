import matplotlib.pyplot as plt
import numpy as np

labels = ['Народ' + str(i) for i in range(1, 8)]
counts = np.random.randint(10, 100, 7)
plt.bar(labels, counts)
plt.title("Население")
plt.xlabel("народы")
plt.ylabel("кол-во")
plt.show()
