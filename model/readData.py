# importing libraries
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv(r"model.csv")
data.head()
data.info()

data1 = data.copy()

data1 = data1.sort_values(by=['Clay'], ascending=True).reset_index()

data1 = data1[['Clay', 'Wood Ash', 'Compressive Strength']]

df = data1.unstack().reset_index()
df.columns = ["X", "Y", "Z"]

df["X"] = df["X"].map({'Clay': 1, 'Wood Ash': 2,
                       'Compressive Strength': 3})

fig = plt.figure(figsize=(14, 4))

ax = fig.gca(projection="3d")

surf = ax.plot_trisurf(df["X"], df["Y"], df["Z"], cmap="jet", linewidth=2)
lab = fig.colorbar(surf, shrink=.5, aspect=5)
lab.set_label("values", fontsize=15)

ax.set_xlabel("variable_encoded")
ax.set_ylabel("index")
ax.set_zlabel("values")

plt.title("Surface plot", color="navy")
plt.show()
