import math
import datetime


def areaOfCircle(radius):
    area = math.pi * math.pow(radius, 2)
    return area


def GetDateTime():
    currentDateTime = datetime.datetime.now()
    return currentDateTime