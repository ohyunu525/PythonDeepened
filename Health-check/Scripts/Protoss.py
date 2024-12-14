import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

def clearPlt():
    plt.clf()
    plt.cla()
def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print("Error: \"", directory, "\" already exists.", sep="")
    except OSError:
        print("Error: Can't make \"", directory, "\".", sep="")

#ProjectSetting
if os.name == "posix":
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="Malgun Gothic")

plt.rc("axes", unicode_minus=False)

SAVEPATH = "../Outputs/WeightByHeight"

#Palettes
SexPalette = ['#99d8ea', '#ffaec9']
BoolPalette = ['#ff9723', '#5599aa']

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = 'white'
plt.rcParams['savefig.edgecolor'] = 'white'

df = pd.read_csv("../Sources/NHIS_OPEN_GJ_2017_v1.1.csv", encoding="CP949")

createDirectory(SAVEPATH)

df_sample = df.sample(1000, random_state=1)

plt.figure(15, 4)


#\[T]/