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

cols = [i for i in data.columns if i not in 'Compressive Strength']
length = len(cols)

plt.figure(figsize=(13, 27))
for i, j in itertools.zip_longest(cols, range(length)):
    plt.subplot(4, 2, j + 1)
    sns.kdeplot(data[i],
                data["Compressive Strength"],
                cmap="hot",
                shade=True)
    plt.title(i + "  &  Compressive Strength", color="navy")
plt.show()
