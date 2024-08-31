import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import seaborn as sns
from scipy import stats

plt.style.use('ggplot')
mpl.rcParams['axes.unicode_minus'] = False
train = pd.read_csv("../train.csv", parse_dates=["datetime"])

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)
fig.set_size_inches(12, 5)

sns.regplot(x="temp", y="count", ax=ax1, data=train)
sns.regplot(x="windspeed", y="count", data=train, ax=ax2, color="blue")
sns.regplot(x="humidity", y="count", data=train, ax=ax3, color="purple")

plt.savefig("BicycleRentalAmountByRegPlot.png")
