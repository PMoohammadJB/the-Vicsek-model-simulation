# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 15:56:56 2025

@author: Pacific
"""

import numpy as np
import random as rd
import matplotlib.pyplot as plt

# =============================================================================
# simulation
# =============================================================================
time_step = 1
def initialize() :
    global N, L, x_positions, y_positions, directions, order_parameters
    x_positions = [ [rd.randint(0, L) for _ in range(N)] ]
    y_positions = [ [rd.randint(0, L) for _ in range(N)] ]
    directions = [ [rd.randint(0, 2*int(np.pi)) for _ in range(N)] ]
    #order parameter
    v_xs = np.cos(directions[0]) 
    v_ys = np.sin(directions[0]) 
    order_parameter = ( np.mean(v_xs)**2 + np.mean(v_ys)**2 )**0.5
    order_parameters = [order_parameter]
    
def update() :
    global R, v, etta
    xs = x_positions[-1]
    ys = y_positions[-1]
    v_xs = v*np.cos(directions[-1])
    v_ys = v*np.sin(directions[-1])
    #positions update
    new_xs = [ (xs[n] + time_step*v_xs[n])%L for n in range(N) ]
    new_ys = [ (ys[n] + time_step*v_ys[n])%L for n in range(N) ]
    x_positions.append(new_xs)
    y_positions.append(new_ys)
    #direction update
    new_dirs = []
    for n in range(N) :
        n_neighbors_dir = []
        for j in range(N) :
            dx = min( xs[n]-xs[j], 1-(xs[n]-xs[j]) )
            dy = min( ys[n]-ys[j], 1-(ys[n]-ys[j]) )
            if (dx**2 + dy**2)**0.5 < R :
                n_neighbors_dir.append(directions[-1][j])
        new_dir = np.mean(n_neighbors_dir) + rd.uniform(-etta/2, etta/2)
        new_dirs.append(new_dir)
    directions.append(new_dirs)
    #order parameter
    v_xs = np.cos(directions[-1]) 
    v_ys = np.sin(directions[-1]) 
    order_parameter = ( np.mean(v_xs)**2 + np.mean(v_ys)**2 )**0.5
    order_parameters.append(order_parameter)
           
# =============================================================================
# running
# =============================================================================
density = 4
Ns = [30, 100, 200, 500]
# L = (N/density)**0.5 
v = 0.03
R = 1
etta_list = np.arange(0, 6, 0.3)
T = 60

def run() :
    initialize()
    for t in range(1, T) :
        update()

# =============================================================================
# order parameter vs noise
# =============================================================================
colors = ['blue', 'red', 'black', 'green']
for i in range(len(Ns)) :
    N = int(Ns[i])
    L = int((N/density)**0.5)
    order_parameter_list = []
    for etta in etta_list :
        run()
        order_parameter_list.append(np.mean(order_parameters[-10:]))
        print(etta)
    plt.scatter(etta_list, order_parameter_list, color = colors[i], label = f'N={N}')
    print(N, '*****************************')
plt.xlabel('etta')
plt.ylabel('order parameter')
plt.title(f'density=4   R=1   v=0.03   T={T}')
plt.legend()
plt.show()

  
    
  
    
  
    
  
    