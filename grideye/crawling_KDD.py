# -*- coding:utf-8 -*-
from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import time
import pdb
url = 'http://fnetpublic.utk.edu/tabledisp.php'

def getValue(tidx, vidx):
    time = arr[tidx].text.split()[2:]
    values = arr[vidx].text.split()[2:]
    return (time, values)

while True:
    try:
        dt = datetime.utcnow()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(url, headers)
        soup = bs(r.text, 'html.parser')
        arr = soup.find_all('tr')
        time_idx = [133,145,166,166,186]
        value_idx = [134,146,167,168,187]


        for i in range(4):
            filename = 'enf'+str(i)+'.txt'
            try:
                fin = open(filename,'r')
            except IOError:
                f = open(filename,'w')
                f.close()
                fin = open(filename,'r')
            lines = fin.readlines()
            fin.close()
            if len(lines)==0:
                last_time = '00:00:00'
            else:
                last = lines[-1].split()
                last_time = last[0]
                if last_time in ['24:00:00','23:59:59','23:59:58','23:59:57','23:59:56']:
                    last_time = '00:00:00'
            #pdb.set_trace()
            t,vs = getValue(time_idx[i], value_idx[i])
            for idx, titem in enumerate(reversed(t)):
                print titem
                print last_time
                if titem<=last_time:
                    continue
                else:
                    f=open(filename,'a')
                    f.write(titem+'\t'+vs[idx]+'\n')
                    print vs[idx]+ ' added in enf'+str(i)
                    f.close()
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
        #print datetime.utcnow()
        print dt.year, dt.month, dt.day, dt.hour, dt.minute
        time.sleep(25)
    except IOError:
        pass
