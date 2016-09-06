# -*- coding:utf-8 -*-
import db
from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import time
url = 'http://fnetpublic.utk.edu/tabledisp.php'

while True:
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
            if not db.is_exist(db.Unit, id=uid):
                db.session.add(db.Unit(id = uid, group=group))
                print uid, 'is added'
    break
db.session.commit()
