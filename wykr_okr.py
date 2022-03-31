import matplotlib.pyplot as plt
import numpy as np

y = np.array([1, 39, 83, 92, 118, 196, 206])
mylabels = ["Others", "Left Party", "AFD", "FDP", "Greens", "CDU/CSU", "SPD"]

plt.pie(y, labels = mylabels, autopct='%1.1f%%')
plt.show() 