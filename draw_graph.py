import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"x": np.array([1, 2, 3]), "y": np.array([   2, 3, 5])})









print(df)
plt.plot(df[  "x"], df["y"])
plt.show()
