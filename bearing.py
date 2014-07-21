# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 15:50:48 2014

@author: Nathan
"""
bearing = range(size(lat)-1)

for i in range(size(lat)-1):
    startLat = math.radians(lat[i])
    startLong = math.radians(longgps[i])
    endLat = math.radians(lat[i+1])
    endLong = math.radians(longgps[i+1])
    
    dLong = endLong - startLong
    
    dPhi = math.log(math.tan(endLat/2.0+math.pi/4.0)/math.tan(startLat/2.0+math.pi/4.0))
    if abs(dLong) > math.pi:
         if dLong > 0.0:
             dLong = -(2.0 * math.pi - dLong)
         else:
             dLong = (2.0 * math.pi + dLong)
    
    bearing[i] = math.atan2(dLong, dPhi)

