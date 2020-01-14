import matplotlib.pyplot as plt
from pandas import DataFrame as df
import csv
import seaborn as sb
import matplotlib as mpl
alldata = []
windata = []
name = []
winrating = []
raceZergRating = []
raceZergWin = []
raceTossRating = []
raceTossWin = []
raceTerranRating = []
raceTerranWin = []
with open('DataSemple.csv', encoding='utf-8-sig') as f:
    plots = csv.reader(f, delimiter=',')
    for row in plots:
        alldata.append(int(row[2]))
        windata.append(int(row[3]))
        winrating.append((int(row[3]) / int(row[2]) * 100))
        name.append(str(row[1]))
        raceTerranRating.append((int(row[5]) / int(row[4]) * 100))
        raceTerranWin.append(int(row[5]))
        raceTossRating.append((int(row[7]) / int(row[6]) * 100))
        raceTossWin.append(int(row[6]))
        raceZergRating.append((int(row[9]) / int(row[8]) * 100))
        raceZergWin.append(int(row[8]))

df1 = df(data={'name:': name, 'win rating': winrating, 'win Data ': windata})
print(df1)
sb.lmplot('name:', 'win rating',  data=df1,
          fit_reg=False, scatter_kws={"s": 100})
df2 = df(data={'name:': name, 'win rating': raceTerranRating,
               'win Data ': raceTerranWin})
sb.lmplot('name:', 'win rating',  data=df2,
          fit_reg=False, scatter_kws={"s": 100})

df3 = df(data={'name:': name, 'win rating': raceTossRating,
               'win Data ': raceTossWin})
sb.lmplot('name:', 'win rating',  data=df3,
          fit_reg=False, scatter_kws={"s": 100})

df4 = df(data={'name:': name, 'win rating': raceZergRating,
               'win Data ': raceZergWin})
sb.lmplot('name:', 'win rating',  data=df4,
          fit_reg=False, scatter_kws={"s": 100})

# plt.plot(df1)
# plt.xscale('log')
plt.show()
