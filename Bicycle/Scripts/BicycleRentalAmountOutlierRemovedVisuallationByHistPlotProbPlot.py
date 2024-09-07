import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import seaborn as sns
from scipy import stats


def concatenate_year_month(datetime):
    return "{0}-{1}".format(datetime.year, datetime.month)


plt.style.use('ggplot')
mpl.rcParams['axes.unicode_minus'] = False
train = pd.read_csv("./train.csv", parse_dates=["datetime"])

train["year"] = train["datetime"].dt.year
train["month"] = train["datetime"].dt.month
train["hour"] = train["datetime"].dt.hour
train["day"] = train["datetime"].dt.day
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second
train["dayofweek"] = train["datetime"].dt.dayofweek

train["year_month"] = train["datetime"].apply(concatenate_year_month)

trainWithoutOutliers = train[np.abs(train["count"]-train["count"].mean()) <= (3*train["count"].std())]

figure, axes = plt.subplots(ncols=2, nrows=2)
figure.set_size_inches(12, 10)

sns.histplot(train["count"], kde=True, ax=axes[0][0])
stats.probplot(train["count"], dist='norm', fit=True, plot=axes[0][1])
sns.histplot(np.log(trainWithoutOutliers["count"]), kde=True, ax=axes[1][0])
stats.probplot(np.log1p(trainWithoutOutliers["count"]), dist='norm', fit=True, plot=axes[1][1])

plt.savefig("BicycleRentalAmountOutlierRemovedByHistPlotProbPlot.png")