#importing libraries
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

plt.figure(figsize=(13,6))
sns.distplot(data["Compressive Strength"],color="b",rug=True)
plt.axvline(data["Compressive Strength"].mean(),
            linestyle="dashed",color="k",
            label='mean',linewidth=2)
plt.legend(loc="best",prop={"size":14})
plt.title("Compressive strength distribution")
plt.show()