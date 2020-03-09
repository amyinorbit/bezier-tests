#!/usr/bin/env python3
from bdyn import bezier
from bdyn.types import Vec, Accelerator
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits import mplot3d

DIM = 3

def square_norm(v: Vec) -> float:
    return v[0]*v[0] + v[1]*v[1] + v[2]*v[2]

def norm(v: Vec) -> float:
    return np.sqrt(square_norm(v))

def gravity(mu: float, c: Vec) -> Accelerator:
    def accel(r: Vec) -> Vec:
        r_p = r - c
        r_n = norm(r_p)
        return -mu * r_p / (r_n * r_n * r_n)
    return accel


def sphere(r: float = 1.0):
    u = np.linspace(0, np.pi, 30)
    v = np.linspace(0, 2 * np.pi, 30)

    x = r * np.outer(np.sin(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.cos(v))
    z = r * np.outer(np.cos(u), np.ones_like(v))

    return x, y, z

h = 300
num_steps = 100
mu = 3.98e14

r0 = 400 + 6371e3
v0 = np.sqrt(mu / r0)

period = 2 * np.pi * np.sqrt(r0**3 / mu)

r = np.empty((num_steps, DIM))
v = np.empty((num_steps, DIM))
ang = np.pi / 4


r[0,:] = [r0, 0, 0]
v[0,:] = [0, np.sin(ang)*v0, np.cos(ang)*v0]

t, b, a = bezier.verlet(r, v, h, gravity(mu, [0, 0, 0]))
tb, rb, vb = bezier.refine(r, b, v, a, h, 10)

fig = figure()
ax = axes(projection='3d')
sx, sy, sz = sphere(6371e3)

ax.plot_wireframe(sx, sy, sz, color='0.9')
ax.plot3D(r[:,0], r[:,1], r[:,2])
ax.plot3D(rb[:,0], rb[:,1], rb[:,2])

fig = figure()
vv = np.array([norm(vi) for vi in v])
rr = np.array([norm(ri) for ri in r])
E0 = (vv[0]**2 / 2) - (mu / rr[0])
E = (vv**2 / 2) - (mu / rr)
plot(t/ period, (E-E0)/E0)
show()
