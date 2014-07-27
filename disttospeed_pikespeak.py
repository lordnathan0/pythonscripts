# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 14:42:09 2014

@author: Nathan
"""

keys, dict = file_to_variables('C:/Users/Nathan/Desktop/Zach_FullRace_062914_edited_seanscript.csv')


velocity = dict['GPS_Speed'] * .44704

time = dict['Time']

dist = zeros(size(time))

for i in range(size(velocity)-1): 
 dist[i+1] = dist[i] + velocity[i]*(diff(time))[i]
 
out = np.column_stack((dist,velocity))
np.savetxt('disttospeed.csv', out, delimiter=",", fmt = '%.7f')