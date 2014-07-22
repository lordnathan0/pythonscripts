# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 16:18:42 2014

@author: Nathan
"""

# vdts generator pikes peak

import math
from scipy.interpolate import UnivariateSpline

max_lat = 9.0
max_decell = 9.0

keys, dict = file_to_variables('C:/Users/Nathan/Desktop/random python scripts/disttoradius.csv')
#keys, zach = file_to_variables('C:/Users/Nathan/Desktop/Zach_FullRace_062914_edited_seanscript.csv')

zspeed = zach['GPS_Speed']
zdist = zach['Distance'] * 1000
zlat = zach['GPS_Latitude']
zlong = zach['GPS_Longitude']
dist = dict['dist']
radius = dict['radius']

cdts = ones(size(dist)) * float('inf')
lat = ones(size(dist)) * float('inf')
a = ones(size(dist)) * float('inf')


rdts = sqrt(max_lat*radius)

#smoothcurve = UnivariateSpline(range(size(rdts)),1/rdts, s = .5)

#curve = smoothcurve(range(size(rdts)))
curve = 1/rdts
curve[curve < 0] = 0
rdts = 1/curve

size_rdts = size(rdts)
#size_rdts = 1000
range_rdts = range(size_rdts-1,-1,-1)

# k = current spot
# i  skip to inf
# j iterate look ahead
i = size_rdts-1
while rdts[i] == float('inf') or rdts[i] == 0:
    i = i-1

cdts[i] = rdts[i]

for k in range(i,0,-1):
    lat[k] = cdts[k]**2/radius[k]
    
    if lat[k] == float('nan'):
        a[k] = max_decell
    elif lat[k] > max_lat:
        a[k] = 0
    else:
        a[k] = math.sin(math.acos(lat[k]/max_lat))*max_decell
    
    d = dist[k] - dist[k-1]
    cdts[k-1] = math.sqrt(a[k]*2*d+cdts[k]**2)
    
    if rdts[k-1] < cdts[k-1]:
        cdts[k-1] = rdts[k-1]


figure('cdts')
plot(dist,cdts/.44704, 'b')
plot(zdist,zspeed, 'r')

figure('gps cdts')
scatter(zlat[:1],zlong[:1], c = (cdts[:1]/.44704), edgecolors = 'none', vmin = 0, vmax = 100)
colorbar()

figure('gps zach')
scatter(zlat,zlong, c = zspeed, edgecolors = 'none', vmin = 0, vmax = 100)
colorbar()

    