from datetime import datetime
from dateutil import tz
import pytz

def convertToUtcDatetime(utcDatetimeString):
    return datetime.strptime(utcDatetimeString, '%Y-%m-%dT%H:%M:%SZ')

def convertUtcDateTimeToLocal(utcTime):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utcTime = utcTime.replace(tzinfo=from_zone)
    localTime = utcTime.astimezone(to_zone)

    return localTime

def isBeforeCurrentTime(time):
    return time < datetime.utcnow()