#!/usr/bin/env python3
from bdyn import bezier, accelerators, vector
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits import mplot3d

DIM = 3

h = 400
num_steps = 15
mu = 3.98e14

r0 = 400 + 6371e3
v0 = np.sqrt(mu / r0)

period = 2 * np.pi * np.sqrt(r0**3 / mu)

r = np.empty((num_steps, DIM))
v = np.empty((num_steps, DIM))
ang = np.pi / 4

r[0,:] = [r0, 0, 0]
v[0,:] = [0, np.sin(ang)*v0, np.cos(ang)*v0]

t, b, a = bezier.verlet(r, v, h, accelerators.gravity(mu, [0, 0, 0]))
tb, rb, vb = bezier.refine(r, b, v, a, h, 10)

fig = figure()
ax = axes(projection='3d')

ax.plot3D(r[:,0], r[:,1], r[:,2])
ax.plot3D(rb[:,0], rb[:,1], rb[:,2])

fig = figure()
vv = np.array([vector.norm(vi) for vi in v])
rr = np.array([vector.norm(ri) for ri in r])
E0 = (vv[0]**2 / 2) - (mu / rr[0])
E = (vv**2 / 2) - (mu / rr)
plot(t/ period, (E-E0)/E0)
show()
