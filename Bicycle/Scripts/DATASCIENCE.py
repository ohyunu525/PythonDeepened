import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

mpl.rcParams['axes.unicode_minus'] = False

train = pd.read_csv("../Sources/train.csv", parse_dates=["datetime"])

test = pd.read_csv("../Sources/test.csv", parse_dates=["datetime"])

print(train.shape)

print(test.shape)

#\[T]/