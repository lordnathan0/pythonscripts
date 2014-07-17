# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 21:43:56 2014

@author: Nathan
"""

from mpl_toolkits.mplot3d import Axes3D
#
#fig = figure()
#Axes3D(fig)
#plot(xs = lat[2000:],ys= long[2000:], zs = time[2000:])

start = 10

fig = figure()
ax = Axes3D(fig)
sc = ax.scatter(xs = lat[start:],ys= long[start:], zs = time[start:], c = tilt[start:], s =60 )
colorbar(sc)