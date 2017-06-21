# -*- coding: utf-8 -*-

import time

def date_to_second(time_string):
    """
    time_string format as '2011-02-28 17:44:30' or |
    |'2011-02-28-17-44-30' or '20130827122619'

    """
    if len(time_string) == 19:
        time_string = time_string.replace(' ','-').replace(':','-')
    elif len(time_string) == 14:
        i = 1
        b = []
        for p in time_string:
            if i % 2 == 1:
                b.append('-')
            b.append(p)
            i = i + 1
        time_string = ''.join(b).replace('-', '', 2)
    else:
        raise Exception('the format of time you given is not right, please check and input again')
    return time.mktime(time.strptime(time_string,'%Y-%m-%d-%H-%M-%S'))

def second_to_date(second,time_type=1):
    if time_type == 1:
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(second))
    elif time_type == 2:
        return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(second))


def get_timestamp(time_format='%Y%m%d%H%M%S'):
    return time.strftime(time_format,time.localtime())


print date_to_second('20110228174430')
print second_to_date(2342334544,2)
print get_timestamp()
