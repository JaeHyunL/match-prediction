import requests
from bs4 import BeautifulSoup
import csv
import re
import time
for i in range(100):
    req = requests.get(
        'https://xn--oy3bn0ftst.com/profile/?month1=2017-05&month2=2020-01&map_id=0&bj_id='+str(i))

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')

    f = open('DataSemple.csv', 'a', encoding='utf-8-sig')
    wr = csv.writer(f, delimiter=' ')
    # wr.writerow([soup.find_all(class_='race_테란')])
    # wr.writerow([soup.find_all(class_='race_토스')])
    # wr.writerow([soup.find_all(class_='race_저그')])
    # f.close()

    raceAll = str(soup.find_all(class_='race_전체'))

    raceAll = re.sub('<.+?>', '', raceAll, 0).strip()
    raceAll = raceAll.replace("[", '')
    raceAll = raceAll.replace("]", '')
    raceAll = raceAll.replace("전체", '')

    raceTerran = soup.find_all(class_='race_테란')
    raceTerran = re.sub('<.+?>', '', raceAll, 0).strip()
    raceTerran = raceTerran.replace("[", '')
    raceTerran = raceTerran.replace("]", '')

    raceToss = soup.find_all(class_='race_토스')
    raceToss = re.sub('<.+?>', '', raceAll, 0).strip()
    raceToss = raceToss.replace("[", '')
    raceToss = raceToss.replace("]", '')

    raceZerg = soup.find_all(class_='race_저그')
    raceZerg = re.sub('<.+?>', '', raceAll, 0).strip()
    raceZerg = raceZerg.replace("[", '')
    raceZerg = raceZerg.replace("]", '')
    time.sleep(3)  # time 3을 하는이유 html 파싱할때 렉이 걸려서 " " or , 밀림 현상 때문에

    wr.writerow(raceAll.rstrip('""') +
                raceTerran.rstrip('""') + raceZerg.rstrip('""'))
    wr.writerows("-----------------")
    wr.writerows(raceAll)
    wr.writerows(',')
    wr.writerows(raceTerran)
    wr.writerows(raceZerg)
    wr.writerows(',')
    wr.writerows('---------------------')
    f.close()
    # print(html)
