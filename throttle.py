# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 11:42:27 2014

@author: Nathan
"""

def throttle (RPM):
    if RPM < 2000:
        return 240
    elif RPM < 2500:
        return -0.08*RPM + 400
    else:
        return -0.2*RPM + 700 

x = arange(0,3500)
y = zeros(3500)

for i in x:
    y[i] = throttle(x[i])

plot(x, y)
figure();
plot(x, x*y)
