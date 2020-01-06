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

        f = open('DataSemple.csv', 'a', encoding='utf-8-sig')
        wr = csv.writer(f, delimiter='\t')
        wr.writerow('userID = ' + str(i))

    #   wr.writerow([soup.find_all(class_='race_테란')])
    #  wr.writerow([soup.find_acll(class_='race_토스')])
    #  wr.writerow([soup.find_all(class_='race_저그')])
        raceAll = str(soup.find_all(class_='race_전체'))

        raceAll = re.sub('<.+?>', '', raceAll, 0).strip()
        raceAll = raceAll.replace("[", '')
        raceAll = raceAll.replace("]", '')
        raceAll = raceAll.replace("전체", '')

        wr.writerow(raceAll)
        time.sleep(1)

        raceTerran = str(soup.find_all(class_='race_테란'))
        raceTerran = re.sub('<.+?>', '', raceTerran, 0).strip()
        raceTerran = raceTerran.replace("[", '')
        raceTerran = raceTerran.replace("]", '')
        raceTerran = raceTerran.replace("테란", '')

        wr.writerow(raceTerran)
        time.sleep(1)

        raceToss = str(soup.find_all(class_='race_토스'))
        raceToss = re.sub('<.+?>', '', raceToss, 0).strip()
        raceToss = raceToss.replace("[", '')
        raceToss = raceToss.replace("]", '')
        raceToss = raceToss.replace("토스", '')

        wr.writerow(raceToss)
        time.sleep(1)

        raceZerg = str(soup.find_all(class_='race_저그'))
        raceZerg = re.sub('<.+?>', '', raceZerg, 0).strip()
        raceZerg = raceZerg.replace("[", '')
        raceZerg = raceZerg.replace("]", '')
        raceZerg = raceZerg.replace("저그", '')
        wr.writerow(raceZerg)


req = requests.get(
    'https://xn--oy3bn0ftst.com/profile/?month1=2017-05&month2=2020-01&map_id=0&bj_id=1')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

vsID = str(soup.find_all(class_='opposite_score'))
soup2 = BeautifulSoup(vsID, 'html.parser')
vsID2 = str(soup2.find_all('a'))
vsID2 = re.sub('[<a href="/profile/?month=&amp;bj_', '', vsID2, 0).strip()
print(vsID2)

# print(vsID)

# vsID = re.sub('<.+?>', '', vsID, 0).strip()
# print(vsID)
# time.sleep(1)  # time 3을 하는이유 html 파싱할때 렉이 걸려서 " " or , 밀림 현상 때문에
# print(html)
