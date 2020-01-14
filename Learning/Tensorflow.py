import matplotlib.pyplot as plt
from pandas import DataFrame as df
import csv
import seaborn as sb
import matplotlib as mpl
import tensorflow as tf
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

df1 = df(data={'name:': name, 'win rating': winrating, 'win Data ': windata, 'terran rating': raceTerranRating, 'terran win ': raceTerranWin,
               'toss rating ': raceTossRating, 'toss win': raceTossWin, 'zerg rating ': raceZergRating, 'Zreg win': raceZergWin})
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


xData = winrating  # X 축 하루의 노동시간 데이터 대입
yData = windata  # Y축  하루 매출량
# 가설의 기울기값 W(가중치) 를 값을 넣어줌 변수로써 정의하고 랜덤
w = tf.Variable(tf.random_uniform([1], -100, 100))
# y절편 값 tf.기울기(tf.랜덤함수(랜덤갯수, 시작범위 , 끝 범위))
b = tf.Variable(tf.random_uniform([1], -100, 100))
X = tf.placeholder(tf.float32)  # 가장 대표적인형태 Placeholder 라는 틀을 정해줌
Y = tf.placeholder(tf.float32)  # 학습용 데이터를 담는 틀
H = w * X+b  # 하나의 가설을 정의함 가설식을 정의 일차함수 꼴로
# 비용함수 정의 square는 제곱 즉 예측값 에서 실제값을 뺀 녀석의 제곱
cost = tf.reduce_mean(tf.square(H-Y))
a = tf.Variable(0.001)  # 경사하강알고리즘 한번에 0.01 만큼 점프하게끔 변수를 a에다가 저장함
# 텐서플로에서 제공해주는 경사하강 라이브러리 누가봐도 학습과 관련된 라이브러리
optimizer = tf.train.GradientDescentOptimizer(a)

# 비용함수를 가장 적게 만드는 방향으로 학습을시켜줄수있도록 만들어줌
# oprtimizer 라는게 신경망 함수 같은건가봐? 거기서 minimize라는 함수를 사용해서 cost최소값을 구하나봐 어디서? cost중에서
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()  # tf 함수중에서 전역변수를 초기화 해줌

# 근데 초기화를 왜 해줄까? TODO 고민 한번해보자구~

sess = tf.Session()  # 응 세션
sess.run(init)  # 응 실행 응 초기화
# 실제 학습을 시켜줌
for i in range(100):
    sess.run(train, feed_dict={X: xData, Y: yData})
    if i % 5 == 0:
        print(i, sess.run(cost, feed_dict={
              X: xData, Y: yData}), sess.run(w), sess.run(b))
print(sess.run(H, feed_dict={X: [8]}))


plt.show()
