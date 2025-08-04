import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,6])
# plt.show()

# years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
# runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

# plt.plot(years, runs)
# plt.xlabel("Year")
# plt.ylabel("Runs Scored")
# plt.title("Sachin Tendulkar's Yearly Runs")
# plt.show()

import numpy as np
for i in range(3):
    plt.plot(np.random.rand(50),linewidth = 1)

plt.title("Too Much Data can Be Confusing!")
plt.grid(True)
plt.tight_layout()
plt.show()