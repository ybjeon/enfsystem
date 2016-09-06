import datetime
def mil_to_date(mil):
    """date items from REST services are reported in milliseconds,
    this function will convert milliseconds to datetime objects

    Required:
        mil -- time in milliseconds
    """
    if mil == None:
        return None
    elif mil < 0:
        return datetime.datetime.utcfromtimestamp(0) + datetime.timedelta(seconds=(mil/1000))
    else:
        return datetime.datetime.fromtimestamp(mil / 1000)

def date_to_mil(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0
