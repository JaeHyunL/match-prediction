import requests
from bs4 import BeautifulSoup
import csv
import re
import time


def race():
    for i in range(1, 200):
        req = requests.get(
            'https://xn--oy3bn0ftst.com/profile/?month1=2017-05&month2=2020-01&map_id=0&bj_id='+str(i))

        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        soup2 = BeautifulSoup(html, 'html.parser')
        f = open('DataSemple.csv', 'a', encoding='utf-8-sig', newline='')
        wr = csv.writer(f, delimiter=',')
        # wr.writerow(['userID = ' + str(i)])
        bjName = str(soup2.find_all("h2", id="container_title"))
        bjName = re.sub('<.+?>', '', bjName, 0).strip()
        bjName = bjName.replace('스폰빵닷컴 - BJ ', '')
        bjName = bjName.replace(' 2017년 5월 ~ 2020년 1월 전적', '')
    #   wr.writerow([soup.find_all(class_='race_테란')])
    #  wr.writerow([soup.find_acll(class_='race_토스')])
    #  wr.writerow([soup.find_all(class_='race_저그')])
        raceAll = str(soup.find_all(class_='race_전체'))

        raceAll = re.sub('<.+?>', '', raceAll, 0).strip()
        raceAll = raceAll.replace("[", '')
        raceAll = raceAll.replace("]", '')
        raceAll = raceAll.replace("전체", '')
        raceAll = raceAll.rstrip('\n')
        raceAll = raceAll.strip('\n')
        raceAll = raceAll.replace('\n', ',')
        raceAll = raceAll.split(',')
        # wr.writerow(raceAll)
        # time.sleep(1)

        raceTerran = str(soup.find_all(class_='race_테란'))
        raceTerran = re.sub('<.+?>', '', raceTerran, 0).strip()
        raceTerran = raceTerran.replace("[", '')
        raceTerran = raceTerran.replace("]", '')
        raceTerran = raceTerran.replace("테란", '')
        raceTerran = raceTerran.rstrip('\n')
        raceTerran = raceTerran.strip('\n')
        raceTerran = raceTerran.replace('\n', ',')
        raceTerran = raceTerran.split(',')
        # wr.writerow(raceTerran)
        # time.sleep(1)

        raceToss = str(soup.find_all(class_='race_토스'))
        raceToss = re.sub('<.+?>', '', raceToss, 0).strip()
        raceToss = raceToss.replace("[", '')
        raceToss = raceToss.replace("]", '')
        raceToss = raceToss.replace("토스", '')
        raceToss = raceToss.strip('\n')
        raceToss = raceToss.replace('\n', ',')
        raceToss = raceToss.split(',')
        # wr.writerow(raceToss)
        # time.sleep(1)

        raceZerg = str(soup.find_all(class_='race_저그'))
        raceZerg = re.sub('<.+?>', '', raceZerg, 0).strip()
        raceZerg = raceZerg.replace("[", '')
        raceZerg = raceZerg.replace("]", '')
        raceZerg = raceZerg.replace("저그", '')
        raceZerg = raceZerg.rstrip('\n')
        raceZerg = raceZerg.strip('\n')

        raceZerg = raceZerg.replace('\n', ',')
        raceZerg = raceZerg.split(',')
        # wr.writerow(raceZerg)

        wr.writerow([bjName, 'userID = ' + str(i), raceAll[0],raceAll[1],
                     raceTerran[0],raceTerran[1], raceToss[0],raceToss[1], raceZerg[0],raceZerg[1]])
        print(str(i) + '번째까지 정상실행 . ')


# req = requests.get(
#    'https://xn--oy3bn0ftst.com/profile/?month1=2017-05&month2=2020-01&map_id=0&bj_id=2')
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
# asdf = soup2.find_all("h2", id="container_title")
# print(asdf)
# vsID = str(soup.find_all(class_='opposite_score'))
# vsID = re.sub('<.+?>', '', vsID, 0).strip()


# print(vsID)
if __name__ == '__main__':
    race()
# vsID = re.sub('<.+?>', '', vsID, 0).strip()
# print(vsID)
# time.sleep(1)  # time 3을 하는이유 html 파싱할때 렉이 걸려서 " " or , 밀림 현상 때문에
# print(html)
