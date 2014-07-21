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

GPSspline = UnivariateSpline(lat,longgps)

dGPS = diff(GPSspline(lat))/diff(lat)
ddGPS = abs(diff(dGPS))


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

#annoying data...

for i in range(size(bearing)):
    if bearing[i] == 0:
        bearing[i] = (bearing[i-1] + bearing[i+1])/2

dbearing = abs(diff(bearing)/diff(time[1:]))

mdbearing = scipy.signal.medfilt(dbearing)

mheading = scipy.signal.medfilt(heading,501)

normheading = range(size(mheading))

for i in range(size(mheading)):
    if mheading[i] < 0:
        normheading[i] = mheading[i] + 360
    else:
        normheading[i] = mheading[i]

dnorm = abs(diff(normheading))
dheading = abs(diff(heading))

dh = scipy.signal.medfilt(minimum(dnorm,dheading))


yawrate = ((dh)*(2*pi/360))/diff(time)
#arc = atan2(cos())
#yawrate = (arc)/diff(time)

radius = velocity[1:]/yawrate

gpsradius = velocity[2:]/dbearing

absradius = abs(radius)

absradiusreplace = absradius

 
lat_acc = (velocity[1:]**2)/absradius

curve = 1/radius


#figure('curve gps')
#scatter(lat[1:],longgps[1:], c = curve, edgecolors = 'none', vmin = min(curve), vmax = max(curve)/5)
#colorbar()
#
#figure('yaw gps')
#scatter(lat[1:],longgps[1:], c = yawrate, edgecolors = 'none', vmin = min(yawrate), vmax = max(yawrate)/5)
#colorbar()

figure('bearing')
scatter(lat[1:],longgps[1:], c = bearing, edgecolors = 'none', vmin = min(bearing), vmax = max(bearing))
colorbar()


figure('dbearing')
scatter(lat[2:],longgps[2:], c = dbearing, edgecolors = 'none', vmin = nanmin(dbearing), vmax = nanmax(dbearing)/2)
colorbar()

figure('gpscurve')
scatter(lat[2:],longgps[2:], c = 1/gpsradius, edgecolors = 'none', vmin = nanmin(1/gpsradius), vmax = .1)
colorbar()


#figure('radius')
#plot(radius)
#
#figure('absradius')
#plot(absradius)
#
#figure('yaw')
#plot(yawrate)
#
#figure('lat acc')
#plot(lat_acc)
#
#
#figure('gps')
#scatter(lat,longgps)
#
#figure('curve')
#scatter(lat[1:], curve)
#
#out = np.column_stack((dist[1:]*1000,radius))
#np.savetxt('disttoradius.csv', out, delimiter=",", fmt = '%.7f')