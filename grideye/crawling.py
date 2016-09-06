# -*- coding:utf-8 -*-
import db
from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import time
url = 'http://fnetpublic.utk.edu/tabledisp.php'

while True:
    try:
        dt = datetime.utcnow()
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')
        arr = soup.find_all('tr')
        for n, item in enumerate(arr):
            if n>149:
                break
            if n in (0, 112, 140):
                group = item.text.strip()
            elif n in (1, 113, 141):
                a = item.text.split()
                times = a[2:]
            else:
                b = item.find_all('td')
                uid = int(b[0].text.split()[1][1:])
                cnt = 0
                for i in range(len(b[1:])):
                    t = times[i].split(':')
                    cur_dt = datetime(
                        dt.year,
                        dt.month,
                        dt.day,
                        int(t[0]),
                        int(t[1]),
                        int(t[2])
                    )
                    if not db.is_exist(db.Data, uid=uid, datetime = cur_dt):
                        value = b[1:][i].text
                        #print uid, cur_dt, value
                        db.session.add(db.Data(uid=uid,
                                               value= float(value) if value != 'No Data' else 0,
                                               datetime=cur_dt))
                        cnt=cnt+1
                print uid, cnt, 'added'
                        #print uid, cur_dt, 'added'
                #for i in b[1:]:
                #    print i.text
        db.session.commit()
        #print datetime.utcnow()
        print dt.year, dt.month, dt.day, dt.hour, dt.minute
        time.sleep(25)
    except Exception:
        pass
