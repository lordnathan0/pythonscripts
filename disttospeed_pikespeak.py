# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 14:42:09 2014

@author: Nathan
"""

keys, dict = file_to_variables('C:/Users/Nathan/Desktop/Zach_FullRace_062914_edited_seanscript.csv')


velocity = dict['GPS_Speed'] * .44704

dist = dict['Distance']


out = np.column_stack((dist*1000,velocity))
np.savetxt('disttospeed.csv', out, delimiter=",", fmt = '%.7f')