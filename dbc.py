# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:29:45 2014

@author: Nathan
"""
mesid = 798 
x = 55

while x < 110: 
    print('BO_ {0} Cells_{1}_{2}: 8 Vector__XXX\n SG_ Cell{3} : 0|15@1- (1,0) [0|5500] "mV" Vector__XXX\n SG_ Cell{4} : 16|15@1- (1,0) [0|5500] "mV" Vector__XXX\n SG_ Cell{5} : 32|15@1- (1,0) [0|5500] "mV" Vector__XXX\n SG_ Cell{6} : 48|15@1- (1,0) [0|5500] "mV" Vector__XXX\n SG_ Cell{7}_bal : 15|1@1+ (1,0) [0|1] "" Vector__XXX\n SG_ Cell{8}_bal : 31|1@1+ (1,0) [0|1] "" Vector__XXX\n SG_ Cell{9}_bal : 47|1@1+ (1,0) [0|1] "" Vector__XXX\n SG_ Cell{10}_bal : 63|1@1+ (1,0) [0|1] "" Vector__XXX'
        .format(mesid, x, x+3, x, x+1 , x+2, x+3, x, x+1, x+2, x+3))
    x = x+4
    mesid = mesid+1
    print '\n'