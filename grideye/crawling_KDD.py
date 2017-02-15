# -*- coding:utf-8 -*-
from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import time
from fake_useragent import UserAgent
#import pdb
url = 'http://fnetpublic.utk.edu/tabledisp.php'

def getValue(tidx, vidxs):
    time = arr[tidx].text.split()[2:]
    values = []
    for vidx in vidxs:
        values.append(arr[vidx].text.split()[2:])
    return (time, values)

while True:
    try:
        dt = datetime.utcnow()
        ua = UserAgent()
        headers = {'User-Agent': ua.chrome}
        r = requests.get(url, headers)
        soup = bs(r.text, 'html.parser')
        arr = soup.find_all('tr')
        time_idx = [133,145,166,186]
        value_idx = [[134],[146],[167,168],[187]]

        for i in range(4):
            fin = open('rw', 'enf'+str(i)+'.txt')
            lines = fin.readlines()
            last = lines[-1].split()
            last_time = last[0]
            t,vs = getValue(time_idx[i], value_idx[i])
            pdb.set_trace()
            print t
            print vs
        # Big Island, Hawaii
        # time: 133 , value: 134

        # Japan West
        # time: 145, value: 146

        # Continental Europe
        # time: 166, value: 167, 168

        # Japan East
        # time: 186, value: 187

#        for n, item in enumerate(arr):
#            if n>149:
#                break
#            if n in (0, 112, 140):
#                group = item.text.strip()
#            elif n in (1, 113, 141):
#                a = item.text.split()
#                times = a[2:]
#            else:
#                b = item.find_all('td')
#                uid = int(b[0].text.split()[1][1:])
#                cnt = 0
#                for i in range(len(b[1:])):
#                    t = times[i].split(':')
#                    cur_dt = datetime(
#                        dt.year,
#                        dt.month,
#                        dt.day,
#                        int(t[0]),
#                        int(t[1]),
#                        int(t[2])
#                    )
#                    if not db.is_exist(db.Data, uid=uid, datetime = cur_dt):
#                        value = b[1:][i].text
#                        #print uid, cur_dt, value
#                        db.session.add(db.Data(uid=uid,
#                                               value= float(value) if value != 'No Data' else 0,
#                                               datetime=cur_dt))
#                        cnt=cnt+1
#                print uid, cnt, 'added'
#                        #print uid, cur_dt, 'added'
#                #for i in b[1:]:
#                #    print i.text
        db.session.commit()
        #print datetime.utcnow()
        print dt.year, dt.month, dt.day, dt.hour, dt.minute
        time.sleep(25)
    except Exception:
        pass
