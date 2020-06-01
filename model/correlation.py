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

cor = data.corr()

mask = np.zeros_like(cor)
mask[np.triu_indices_from(mask)] = True

plt.figure(figsize=(12, 10))

with sns.axes_style("white"):
    sns.heatmap(cor, annot=True, linewidth=2,
                mask=mask, cmap="magma")
plt.title("Correlation between variables")
plt.show()
