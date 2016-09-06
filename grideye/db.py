from db_schema import Data, engine, Base, Unit
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
def is_exist(Table, id=None, uid=None, datetime=None):
    q = session.query(Table)
    if id is not None:
        q = q.filter(Table.id==id)
    if uid is not None:
        q = q.filter(Table.uid==uid)
    if datetime is not None:
        q = q.filter(Table.datetime==datetime)
    if q.count():
        return True
    else:
        return False
