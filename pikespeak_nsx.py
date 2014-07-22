# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 20:11:58 2014

@author: Nathan
"""

#keys,nsx = file_to_variables('C:/Users/Nathan/Desktop/random python scripts/jamesNSX_dataPPIHC_edit.csv')

lateral = nsx['G_Lat'] * 9.80665
speed = nsx['Ground_Speed'] * 0.277778
lat = nsx['GPS_Latitude']
longgps = nsx['GPS_Longitude']
time = nsx['Time']
#dist = nsx['Distance']
dist = zeros(size(speed))

for i in range(size(speed)-1): 
    dist[i+1] = dist[i] + speed[i]*(diff(time))[i]
    

radius = (speed**2.0)/lateral


figure('radius')
scatter(lat,longgps, c = abs(radius), edgecolors = 'none', vmin = 0, vmax = 200)
colorbar()

out = np.column_stack((dist,abs(radius)))
np.savetxt('disttoradius.csv', out, delimiter=",", fmt = '%.7f')