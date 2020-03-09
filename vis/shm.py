#!/usr/bin/env python3
from bdyn import bezier
from bdyn.types import Vec, Accelerator
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits import mplot3d

DIM = 1

def spring_mass(k: float, m: float) -> Accelerator:
    def accel(r: Vec) -> Vec:
        return - r * k / m
    return accel

h = 0.5
k = 1.0
m = 1.0
num_periods = 3
omega = np.sqrt(k/m)
period = 2 * np.pi / omega
num_steps = int(num_periods * period / h) + 1

r = np.empty((num_steps, DIM))
v = np.empty((num_steps, DIM))
r[0,:] = 1
v[0,:] = 0

t, b, a= bezier.verlet(r, v, h, spring_mass(k, m))
tb, rb, vb = bezier.refine(r, b, v, a, h, 10)

plot(tb, rb)
show()
