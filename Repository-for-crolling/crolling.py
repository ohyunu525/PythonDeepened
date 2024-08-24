import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Matplotlib 백엔드 설정
matplotlib.use('agg')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

fpath = 'pokemon.csv'
poke_data = pd.read_csv(fpath, index_col='#')
plt.figure(figsize=(16, 9))
sns.swarmplot(x = "Generation", y = "HP", hue = "Total", data= poke_data, dodge=True)
#저장:plt.savefig('FileName.png')
plt.savefig('RealFile.png')
#\[T]/