#!/usr/bin/env python3
from bdyn import bezier, accelerators
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits import mplot3d

DIM = 3

h = 0.5
num_steps = 5

r = np.empty((num_steps, DIM))
v = np.empty((num_steps, DIM))
r[0,:] = [0, 0, 0]
v[0,:] = [7, 5, 10]

t, b, a = bezier.verlet(r, v, h, accelerators.const_gravity([0, 0, -9.81]))
tb, rb, vb = bezier.refine(r, b, v, a, h, 10)

fig = figure()
ax = axes(projection='3d')
ax.plot3D(r[:,0], r[:,1], r[:,2])
ax.plot3D(rb[:,0], rb[:,1], rb[:,2])
show()
