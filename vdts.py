# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 16:18:42 2014

@author: Nathan
"""

# vdts generator pikes peak

max_lat = 9.0
max_decell = 9.0

keys, dict = file_to_variables('C:/Users/Nathan/Desktop/random python scripts/pikespeakradius.csv')

dist = dict['dist']
radius = dict['radius']

cdts = ones(size(dist)) * float('inf')
d_lookahead = zeros(size(dist))

rdts = sqrt(max_lat*radius)

size_rdts = size(rdts)
#size_rdts = 1000
range_rdts = range(size_rdts)

# k = current spot
# i  skip inf
# j iterate look ahead

for k in range_rdts:
    i = k
    while rdts[i] == float('inf'):
        i = i+1
    d_lookahead[k] = (rdts[i]**2)/(2*max_decell)
    j = i
    while dist[j] < (dist[k] + d_lookahead[k]) and j < size_rdts:
        bdts = sqrt(max_decell*2*(dist[j]-dist[k])+rdts[j]**2)
        if cdts[k] > bdts:
            cdts[k] = bdts
        j = j+1

    