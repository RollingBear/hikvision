# -*- coding: utf-8 -*-

#   2019/9/3 0003 下午 5:06     

__author__ = 'RollingBear'


import platform

from ctypes import *

fileAddr = ''

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary(fileAddr)
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary(fileAddr)


def NET_DVR_GetLastError():

    result = libc.NET_DVR_GetLastError()

    return result


def NET_DVR_Init():

    result = libc.NET_DVR_Init()

    return result


def NET_DVR_Cleanup():

    result = libc.NET_DVR_Cleanup()

    return result


def NET_DVR_GetSDKBuildVersion():

    result = libc.NET_DVR_GetSDKBuildVersion()

    return result


def NET_DVR_GetSDKState():

    result = libc.NET_DVR_GetSDKState()
