import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

if os.name == "posix":
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="Malgun Gothic")

plt.rc("axes", unicode_minus=False)

df = pd.read_csv("../Sources/NHIS_OPEN_GJ_2017_v1.1.csv", encoding="CP949")

plt.savefig("")


#\[T]/