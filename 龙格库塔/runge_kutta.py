#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:15:23 2019

@author: fenglei
"""

import math
import numpy as np
import matplotlib.pyplot as plt

## 4 forder runge kutta
def runge_kutta(y0, x, dx,f):
    k1 = f(y0, x)*dx
    k2 = f(y0 + 0.5*k1, x + 0.5*dx)*dx
    k3 = f(y0 + 0.5*k2, x + 0.5*dx)*dx
    k4 = f(y0 + k3, x + dx)*dx
    y = y0 + 1./6*(k1 +2*k2 + 2*k3 + k4)
    return y
    
## diffrential func
def func(y, t):
    result = t*np.sqrt(y)
    return result

def analytic_y(t):
    result = (t**2 + 4)**2/16.
    return result

def runge_kutta_2_order(y0, x, dx,f):
    k1 = f(y0, x)*dx
    k2 = f(y0 + k1/2., x + 0.5*dx)*dx
    y = y0 + k2
    return y

t = 0
dt = 0.1
y_ini = 1.
n_step = 100

y_oder_2 = 1.
t_list = np.array([t +dt*i for i in range(n_step)])
#print(t_list)
y_update = y_ini
numeric_y = []
numeric_t = []
numeric_y_order_2 = []
for i in range(n_step):
    '''
    update y and t simutaneosly and save them
    '''
    ## 4 orer
    y_ = runge_kutta(y_update, t , dt, func) 
    t += dt
    y_update = np.copy(y_)
    ## 2 order
    y_oder_2 = runge_kutta_2_order(y_oder_2, t , dt, func)
#    print(y_update)
    numeric_y.append(y_update)
    numeric_t.append(t)
    numeric_y_order_2.append(y_oder_2)
#numeric_y = np.array([runge_kutta(y_ini, t +dt*i, dt, f) for i in range(10)])
exact_y = [analytic_y(t) for t in t_list]

plt.plot(numeric_t, numeric_y,lw=2, label='order-4-runge-kutta ')
plt.plot(t_list, exact_y, lw=2,label='analytic')
plt.plot(numeric_t, numeric_y_order_2, lw=2, label='order-2-runge-kutta ')
plt.xlabel('t', fontsize=15)
plt.ylabel('y(t)', fontsize=15)
plt.legend()










