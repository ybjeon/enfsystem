import db
from datetime import datetime
under_dt = datetime(2016, 5, 13, 21, 54, 24)
above_dt = datetime(2016, 5, 14, 21, 54, 24)
arr = db.session.query(db.Data).count()
#        .filter(db.Data.datetime>above_dt)\
#        .filter(db.Data.datetime>under_dt)\
#        .filter(db.Data.datetime<above_dt).all()
print arr
for item in arr:
    print item.id
