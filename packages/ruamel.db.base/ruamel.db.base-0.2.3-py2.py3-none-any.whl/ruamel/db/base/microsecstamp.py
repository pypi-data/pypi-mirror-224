
import time
import math


def micro_sec_stamp(t=None):
    """return time as a non-space containing string that includes microseconds
    and where both date and time elements are separated by '-' (some use
    cases preclude using ':'
    """
    if t is None:
        t = time.time()
    msec = str(math.modf(t)[0])[1:8]
    ts = time.gmtime(t)
    return time.strftime('%Y-%m-%dT%H-%M-%S', ts) + msec


def micro_sec_stamp_to_time(s):
    """go from string to UTC time. mktime is timezone dependent"""
    from calendar import timegm
    dts, ms = s.split('.')
    ms = float('0.' + ms)
    # this could be off because of DST
    #  x = time.mktime(time.strptime(dts, '%Y-%m-%dT%H-%M-%S %Z')) - \
    #    time.timezone
    dts = timegm(list(map(int, dts.replace('T', '-', 1).split('-'))))
    return dts + ms
