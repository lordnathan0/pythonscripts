# -*- coding: utf-8 -*-
"""
Created on Sat May 10 13:12:06 2014

@author: Nathan
"""

key,IOM = file_to_variables('C:/Users/Nathan/Desktop/CAR sync/Buckeye_Current/Battery Discussion/IOM profile.csv')

time = IOM['RaceTime']
speed = IOM['Speed']

dtime = diff(time)

dist = arange(len(dtime))*1.0

for i in arange(len(dtime)-1):
    dist[i+1] = (speed[i+1] * dtime[i]) + dist[i]


out = np.column_stack((time[1:],dist))
np.savetxt('timetodist.csv', out, delimiter=",", fmt = '%.7f')

