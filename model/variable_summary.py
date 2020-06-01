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

data1 = data1.sort_values(by=['Clay'], ascending=True).reset_index()

data1 = data1[['Clay', 'Wood Ash', 'Charcoal', 'Iron Powder', 'Compressive Strength']]


plt.figure(figsize=(12, 8))
sns.heatmap(round(data.describe()[1:].transpose(),2),linewidth=2,annot=True,fmt="f")
plt.xticks(fontsize=20)
plt.yticks(fontsize=12)
plt.title("Variables summary")
plt.show()