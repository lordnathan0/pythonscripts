# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 13:41:43 2014

@author: Nathan
"""

import scipy.signal
from scipy.interpolate import griddata,interp1d

keys, dict = file_to_variables('C:/Users/Nathan/Desktop/random python scripts/PPIHC radius - 20pt least-square radius estimate - GPS dist.csv')
keys, zach = file_to_variables('C:/Users/Nathan/Desktop/Zach_FullRace_062914_edited_seanscript.csv')

zlat = zach['GPS_Latitude']
zlong = zach['GPS_Longitude']
dist = dict['dist']
zdist = zach['Distance']
radius = dict['radius']

velocity = zach['GPS_Speed'] * .44704

time = zach['Time']

#zdist = zeros(size(time))
#
#for i in range(size(velocity)-1): 
# zdist[i+1] = zdist[i] + velocity[i]*(diff(time))[i]
 
zradius = radius
zradius = zradius[:size(zlong)]

#for i in range(size(zradius)):
#    if zradius[i] < 15:
#        zradius[i] = zradius[i-1]

zradius = scipy.signal.medfilt(zradius)

tdist = dist
tdist = tdist[:size(zlong)] 


zradius[zradius == float('inf')] = 10000

#d_r = interp1d(dist,radius)
#
#gpsradius = d_r(zdist)
#
lat_acc = velocity**2/zradius

figure('dist v zdist')
plot(tdist)
plot(zdist,'r')
 
figure('gps radius')
scatter(zlat,zlong, c = zradius, edgecolors = 'none', vmin = 0, vmax = 30)
colorbar()

figure('lat_acc')
plot(lat_acc)

figure('gps lat')
scatter(zlat,zlong, c = lat_acc, edgecolors = 'none', vmin = 0, vmax = 15)
colorbar()

out = np.column_stack(((tdist-tdist[0])*1000,zradius))
np.savetxt('disttoradius.csv', out, delimiter=",", fmt = '%.7f')