# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 14:21:26 2014

@author: Nathan
"""
mesid =825 
x = 15

while x < 40: 
    print('BO_ {0} PackTemperatures{1}Thru{2}: 8 Vector__XXX\n SG_ Temp{3} : 0|16@1- (1,0) [-32768|32767] "(c°C)"  Vector__XXX\n SG_ Temp{4} : 16|16@1- (1,0) [-32768|32767] "(c°C)" Vector__XXX\n SG_ Temp{5} : 32|16@1- (1,0) [-32768|32767] "(c°C)" Vector__XXX\n SG_ Temo{6} : 48|16@1- (1,0) [-32768|32767] "(c°C)" Vector__XXX\n'
        .format(mesid, x, x+3, x, x+1 , x+2, x+3))
    x = x+4
    mesid = mesid+1
    print '\n'
    
