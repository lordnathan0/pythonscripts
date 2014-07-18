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

#keys, dict = file_to_variables('C:/Users/Nathan/Desktop/Zach_FullRace_062914_edited_seanscript.csv')

heading = dict['GPS_Heading']
velocity = dict['GPS_Speed'] * .44704
time = dict['Time']
lat = dict['GPS_Latitude']
longgps = dict['GPS_Longitude']
dlat = diff(lat)
dlong = diff(long)
dist = dict['Distance']

GPSspline = UnivariateSpline(lat,longgps)

dGPS = diff(GPSspline(lat))/diff(lat)

mheading = scipy.signal.medfilt(heading,601)

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
absradius = abs(radius)

absradiusreplace = absradius

 
lat_acc = (velocity[1:]**2)/absradius

curve = 1/radius






figure('radius')
plot(radius)

figure('absradius')
plot(absradius)

figure('yaw')
plot(yawrate)

figure('lat acc')
plot(lat_acc)


figure('gps')
scatter(lat,longgps)

figure('curve')
scatter(lat[1:], curve)
#
#out = np.column_stack((dist[1:]*1000,radius))
#np.savetxt('disttoradius.csv', out, delimiter=",", fmt = '%.7f')