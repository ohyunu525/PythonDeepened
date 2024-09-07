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

corrMatt = train[["temp", "atemp", "casual", "registered", "humidity", "windspeed", "count"]]
corrMatt = corrMatt.corr()
print(corrMatt)

mask = np.array(corrMatt)
mask[np.tril_indices_from(mask)] = False
fig, ax = plt.subplots()
fig.set_size_inches(20, 10)
sns.heatmap(corrMatt, mask=mask, vmax=8, square=True, annot=True)

plt.savefig("BicycleRentalAmountCorrelationByHeatMap.png")
