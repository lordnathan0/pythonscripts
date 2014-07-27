# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 16:44:20 2014

@author: Nathan
"""

keys,radius = file_to_variables('')

keys, dict = file_to_variables('C:/Users/Nathan/Desktop/random python scripts/PPIHC radius - 20pt circumradius - GPS dist.csv')

dist = dict['dist']
rad = dict['radius']

d1 = radius['d1']
d2 = radius['d2']
r = radius['r']

percent-rad_error = list()
dist_error = list()
radius_error = list()
r_error = list()

for i in range(size(d1)):
    for d in range(size(dist)):
        if dist[d] > d1[i] and dist[d] < d2[i]:
            percent_rad_error.append((r[i] - rad[d]/r[i]))
            dist_error.append(dist[d])
            radius_error.append(rad[d])
            r_error.append(r[i])
            
            