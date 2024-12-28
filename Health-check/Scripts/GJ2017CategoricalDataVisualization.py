import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings

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
warnings.simplefilter(action='ignore', category=FutureWarning)

#Palettes
SexPalette = ['#99d8ea', '#ffaec9']
BoolPalette = ['#ff0000', '#0000ff']

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = 'white'
plt.rcParams['savefig.edgecolor'] = 'white'

df = pd.read_csv("../Sources/NHIS_OPEN_GJ_2017_v1.1.csv", encoding="CP949")

createDirectory("../Outputs/CategoricalData")

df_sample = df.sample(1000, random_state=1)
"""
df["음주여부"].value_counts().plot.bar()
plt.savefig("../Outputs/CategoricalData/CategoricalData_1")
clearPlt()

sns.countplot(x="음주여부", data=df, palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_2")
clearPlt()

sns.countplot(x="음주여부", data=df, hue="성별코드", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_3")
clearPlt()

sns.set(font_scale=1.5, font="Malgun Gothic")
sns.countplot(x="음주여부", data=df, hue="성별코드", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_4")
clearPlt()

sns.countplot(data=df, x="연령대코드(5세단위)")
plt.savefig("../Outputs/CategoricalData/CategoricalData_5")
clearPlt()

sns.countplot(data=df, x="연령대코드(5세단위)", hue="음주여부", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_6")
clearPlt()


plt.figure(figsize=(15, 6))
sns.countplot(data=df, x="신장(5Cm단위)", palette="rainbow")
plt.savefig("../Outputs/CategoricalData/CategoricalData_7")
clearPlt()

plt.figure(figsize=(15, 6))
sns.countplot(data=df, x="체중(5Kg단위)", palette="rainbow")
plt.savefig("../Outputs/CategoricalData/CategoricalData_8")
clearPlt()

plt.figure(figsize=(15, 6))
sns.countplot(data=df, x="신장(5Cm단위)", hue="성별코드", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_9")
clearPlt()

plt.figure(figsize=(15, 6))
sns.countplot(data=df, x="체중(5Kg단위)", hue="성별코드", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_10")
clearPlt()

sns.barplot(data=df, x="연령대코드(5세단위)", y="총콜레스테롤", palette="rainbow")
plt.savefig("../Outputs/CategoricalData/CategoricalData_11")
clearPlt()

sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="총콜레스테롤", palette="rainbow")
plt.savefig("../Outputs/CategoricalData/CategoricalData_12")
clearPlt()

sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="총콜레스테롤", hue="음주여부", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_13")
clearPlt()

plt.figure(figsize=(12, 6))
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="총콜레스테롤", hue="흡연상태", palette="Set1")
plt.savefig("../Outputs/CategoricalData/CategoricalData_14")
clearPlt()

plt.figure(figsize=(12, 6))
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_15")
clearPlt()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", ci=95, palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_16")
clearPlt()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", errorbar="sd", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_17")
clearPlt()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="연령대코드(5세단위)", y="체중(5Kg단위)", hue="성별코드", errorbar=None, palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_18")
clearPlt()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="연령대코드(5세단위)", y="체중(5Kg단위)", hue="음주여부", errorbar=None, palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_19")
clearPlt()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="연령대코드(5세단위)", y="체중(5Kg단위)", hue="음주여부", ci="sd", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_20")
clearPlt()

plt.figure(figsize=(15, 6))
sns.lineplot(data=df, x="연령대코드(5세단위)", y="체중(5Kg단위)", hue="성별코드", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_21")
clearPlt()

plt.figure(figsize=(15, 6))
sns.lineplot(data=df_sample, x="연령대코드(5세단위)", y="체중(5Kg단위)", hue="성별코드", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_22")
clearPlt()

plt.figure(figsize=(15, 6))
sns.lineplot(data=df_sample, x="연령대코드(5세단위)", y="체중(5Kg단위)", hue="성별코드", ci="sd", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_23")
clearPlt()

plt.figure(figsize=(15, 6))
sns.lineplot(data=df_sample, x="연령대코드(5세단위)", y="신장(5Cm단위)", hue="성별코드", ci="sd", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_24")
clearPlt()

plt.figure(figsize=(15, 6))
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="신장(5Cm단위)", hue="음주여부", ci="sd", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_25")
clearPlt()

plt.figure(figsize=(15, 6))
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="신장(5Cm단위)", hue="음주여부", ci="sd", palette=sns.color_palette(BoolPalette))
sns.pointplot(data=df_sample, x="연령대코드(5세단위)", y="신장(5Cm단위)", hue="음주여부", ci="sd", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_26")
clearPlt()

plt.figure(figsize=(15, 6))
sns.pointplot(data=df_sample, x="연령대코드(5세단위)", y="신장(5Cm단위)", hue="성별코드", ci="sd", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_27")
clearPlt()
#여기부터계속
plt.figure(figsize=(15, 6))
sns.lineplot(data=df, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", ci=None, palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_28")
clearPlt()

plt.figure(figsize=(15, 6))
sns.boxplot(data=df, x="신장(5Cm단위)", y="체중(5Kg단위)", hue="성별코드", palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_29")
clearPlt()

plt.figure(figsize=(15, 6))
sns.violinplot(data=df, x="신장(5Cm단위)", y="체중(5Kg단위)", hue="음주여부", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_30")
clearPlt()

plt.figure(figsize=(15, 6))
sns.violinplot(data=df, x="신장(5Cm단위)", y="체중(5Kg단위)", hue="음주여부", split=True, palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_31")
clearPlt()

plt.figure(figsize=(15, 6))
sns.violinplot(data=df, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_32")
clearPlt()

plt.figure(figsize=(15, 6))
sns.violinplot(data=df, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", split=True, palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_33")
clearPlt()

plt.figure(figsize=(12, 4))
sns.swarmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg단위)", hue="음주여부", size=2, palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_34")
clearPlt()

plt.figure(figsize=(12, 4))
sns.swarmplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", size=2, palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_35")
clearPlt()
"""
plt.figure(figsize=(8, 7))
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_36")
clearPlt()


plt.figure(figsize=(8, 7))
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부", size="체중(5Kg단위)", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_37")
clearPlt()

plt.figure(figsize=(8, 7))
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="허리둘레")
plt.savefig("../Outputs/CategoricalData/CategoricalData_38")
clearPlt()

plt.figure(figsize=(8, 7))
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg단위)", hue="음주여부", palette=sns.color_palette(BoolPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_39")
clearPlt()

plt.figure(figsize=(8, 7))
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg단위)", hue="성별코드", col='음주여부', palette=sns.color_palette(SexPalette))
plt.savefig("../Outputs/CategoricalData/CategoricalData_40")
clearPlt()
#\[T]/