import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import seaborn as sns
from scipy import stats

plt.style.use('ggplot')
mpl.rcParams['axes.unicode_minus'] = False
train = pd.read_csv("../Sources/train.csv", parse_dates=["datetime"])

train["year"] = train["datetime"].dt.year
train["month"] = train["datetime"].dt.month
train["hour"] = train["datetime"].dt.hour
train["day"] = train["datetime"].dt.day
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(12, 10)

sns.boxplot(data=train, y="count", orient="v", ax=axes[0][0])
sns.boxplot(data=train, y="count", x="season", orient="v", ax=axes[0][1])
sns.boxplot(data=train, y="count", x="hour", orient="v", ax=axes[1][0])
sns.boxplot(data=train, y="count", x="workingday", orient="v", ax=axes[1][1])

axes[0][0].set(ylabel='Count', title="Rental Amount")
axes[0][1].set(xlabel='Season', ylabel='Count', title="Rental Amount by Seasons")
axes[1][0].set(xlabel='Hour Of The Day', ylabel='Count', title="Rental Amount by Hour")
axes[1][1].set(xlabel='Working Day', ylabel='Count', title="Rental Amount d_on working days")

plt.savefig("../OutPuts/BicycleRentalAmountBySeasonsHourD_onWorkingDaysBoxPlot.png")
