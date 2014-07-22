# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 15:01:58 2014

@author: Nathan

Use the idea that corner radius = velocity/yaw rate to calculate a corner radius of 
pikes peak using gps data
"""
import scipy.signal
from scipy.interpolate import UnivariateSpline
from scipy import interpolate

from mpl_toolkits.mplot3d import Axes3D

keys, dict = file_to_variables('C:/Users/Nathan/Desktop/Zach_FullRace_062914_edited_seanscript.csv')

heading = dict['GPS_Heading']
velocity = dict['GPS_Speed'] * .44704
time = dict['Time']
lat = dict['GPS_Latitude']
longgps = dict['GPS_Longitude']
dist = dict['Distance']


bearing = range(size(lat)-1)

gpssmooth = .000001

slat = UnivariateSpline(range(size(lat)),lat, s = gpssmooth)
lats  = slat(range(size(lat)))

slong = UnivariateSpline(range(size(longgps)),longgps, s = gpssmooth)
longgpss = slong(range(size(longgps)))

for i in range(size(lat)-1):
    startLat = math.radians(lats[i])
    startLong = math.radians(longgpss[i])
    endLat = math.radians(lats[i+1])
    endLong = math.radians(longgpss[i+1])
    
    dLong = endLong - startLong
    
    dPhi = math.log(math.tan(endLat/2.0+math.pi/4.0)/math.tan(startLat/2.0+math.pi/4.0))
    if abs(dLong) > math.pi:
         if dLong > 0.0:
             dLong = -(2.0 * math.pi - dLong)
         else:
             dLong = (2.0 * math.pi + dLong)
    
    bearing[i] = math.atan2(dLong, dPhi)

#annoying data...

for i in range(size(bearing)):
    if bearing[i] == 0:
        bearing[i] = (bearing[i-1] + bearing[i+1])/2

#sbearing = UnivariateSpline(range(size(bearing)),bearing, s = 1000)
#bearing  = sbearing(range(size(bearing)))

arclength = velocity[:-1]*diff(time)

center_angle = diff(bearing)

radius = arclength[:-1]/center_angle
 
lat_acc = (velocity[:-2]**2)/abs(radius)

curve = 1/radius


#figure('curve gps')
#scatter(lat[1:],longgps[1:], c = curve, edgecolors = 'none', vmin = min(curve), vmax = max(curve)/5)
#colorbar()
#
#figure('yaw gps')
#scatter(lat[1:],longgps[1:], c = yawrate, edgecolors = 'none', vmin = min(yawrate), vmax = max(yawrate)/5)
#colorbar()


figure('bearing')
scatter(lat[:-1],longgps[:-1], c = bearing, edgecolors = 'none', vmin = min(bearing), vmax = max(bearing))
colorbar()

figure('radius')
scatter(lat[:-2],longgps[:-2], c = abs(radius), edgecolors = 'none', vmin = 0, vmax = 50)
colorbar()

figure('gps lat acc')
scatter(lat[:-2],longgps[:-2], c = lat_acc, edgecolors = 'none', vmin = 0, vmax = 40)
colorbar()

figure('smooth gps')
scatter(lats,longgpss)

#figure('radius')
#plot(radius)
#
#figure('absradius')
#plot(absradius)
#
#figure('yaw')
#plot(yawrate)
#
figure('lat acc')
plot(lat_acc)
#
#
#figure('gps')
#scatter(lat,longgps)
#
#figure('curve')
#scatter(lat[1:], curve)
#
#out = np.column_stack((dist[:-2]*1000,abs(radius)))
#np.savetxt('disttoradius.csv', out, delimiter=",", fmt = '%.7f')