# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 15:01:58 2014

@author: Nathan
"""

keys, dict = file_to_variables('C:/Users/Nathan/Desktop/Zach_FullRace_062914_edited_seanscript.csv')

heading = dict['GPS_Heading']
velocity = dict['GPS_Speed']
time = dict['Time']
yawrate = diff(heading)/diff(time)
radius = velocity[1:]*0.44704/yawrate

