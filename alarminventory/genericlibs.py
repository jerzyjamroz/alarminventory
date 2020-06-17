#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys
import os
#import socket
#import math
#import epics


def assure_py3():
    # System test
    print(os.getcwd())
    print("INFO Python Environment", sys.version)

    if sys.version_info[0] < 3:
        raise Exception("ERROR Python 3 required")


def pfx_put_sep(prefix=""):
    if prefix[-1].isalpha() or prefix[-1].isdigit():
        prefix += ':'
    return prefix


def pfx_put_nosep(prefix=""):
    if prefix[-1].isalpha() or prefix[-1].isdigit():
        return prefix
    return prefix[:-1]


def time2iso():
    return datetime.datetime.now().replace(microsecond=0).isoformat().replace('-', '').replace(':', '')


def time_span2sec(time_span_str):
    time_span_int = int(time_span_str[:-1])
    if time_span_str.endswith('d'):
        return time_span_int * 60 * 60 * 24
    elif time_span_str.endswith('h'):
        return time_span_int * 60 * 60
    elif time_span_str.endswith('m'):
        return time_span_int * 60
    elif time_span_str.endswith('s'):
        return time_span_int
    raise ValueError("ERROR Wrong Time, use num[d h m s]")


# def list_1dim_get(plist, dim):
#     try:
#         list_tmp = [i[dim] for i in plist]
#     except:
#         print("WARNING list_1dim_get ", sys.exc_info()[0])
#         return []
#     return list_tmp

def msg2meta(msg, msg_list=[], file=None):
    msg = str(msg)
    msg_list.append(msg)
    print(msg, file=file)
    return msg

# def my_ip_get():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(("8.8.8.8", 80))
#     tmp_str = s.getsockname()[0]
#     s.close()
#     return str(tmp_str)
