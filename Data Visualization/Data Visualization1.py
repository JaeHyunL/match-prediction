import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
x = []
y = []

with open('DataSemple.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',' )
    for row in plots:
        x.append(int(row[2]))
        y.append(int(row[3]))

#styles = ['-', '--', ':']
#colors = ['deepskyblue', 'mediumseagreen', 'hotpink']
#widths = [10, 5, 2]

#s = pd.Series(x, y , dtype='float64')
plt.title("Plot")
for i in range(45):
    plt.hist(x[i], bins=15)
plt.xlim([0,5000]) 
plt.ylim([0,5000])
plt.legend()
plt.show()




#plt.title("Line examples")    # 그래프 제목
#plt.xlabel("X")               # x축 이름
##plt.ylabel("Y")               # y축 이름
#plt.xlim([0,10])              # x축 최소최대값
#plt.ylim([0,100])             # y축 최소최대값

### 5. 그래프 그림 저장하기
#plt.savefig("lineexamples.png", dpi=350)

### 6. 그래프 화면에 출력하기
#plt.show()
#plt.figure()
#plt.plot(x,y, label='int load file')
#plt.xlabel('판수')
#plt.ylabel('승수 ')
#plt.title('그래프')
#plt.grid()
#plt.legend()
#plt.savefig('txt.png')
#plt.close()