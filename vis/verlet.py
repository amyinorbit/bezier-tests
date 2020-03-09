#!/usr/bin/env python3
from typing import Callable, NewType, Tuple
from dataclasses import dataclass
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits import mplot3d

Vec = np.array
Accelerator = Callable[[Vec], Vec]
Dim = 2

@dataclass
class Options:
    step_size: float
    step_count: int
    div_count: intquarespace.com
    accelerate: Accelerator

def verlet_bezier(
    x: np.ndarray,
    b: np.ndarray,
    v: np.ndarray,
    a: np.ndarray,
    t: np.ndarray,
    options: Options) -> None:
    h = options.step_size
    for n in range(0, options.step_count-1):
        x[n+1,:] = x[n,:] + v[n,:]*h + 0.5*a[n,:]*(h**2)
        a[n+1,:] = options.accelerate(x[n+1])
        v[n+1,:] = v[n,:] + 0.5*h*(a[n,:] + a[n+1,:])
        b[n,:] = x[n,:] + 0.5 * v[n,:]*h
    b[-1,:] = x[-1,:] + 0.5 * v[-1,:]*h

def bezier_refine(x: np.ndarray, b: np.ndarray, )

def spring_mass(k: float, m: float) -> Accelerator:
    def accel(x: Vec) -> Vec:
        return - x * k / m
    return accel


h = 0.8
k = 1.0
m = 1.0
num_periods = 3
omega = np.sqrt(k/m)
period = 2 * np.pi / omega
num_steps = int(num_periods * period / h) + 1

smh = Options(
    h, num_steps, 10,
    spring_mass(k, m)
)

x = np.empty((num_steps, Dim))
b = np.empty((num_steps, Dim))
v = np.empty((num_steps, Dim))
a = np.empty((num_steps, Dim))
t = np.arange(0.0, num_steps) * h

x[0,:] = np.array([1, 0])
v[0,:] = np.array([0, 1])
a[0,:] = smh.accelerate(x[0])

verlet_bezier(x, b, v, a, t, smh)



fig = figure()
ax = axes(projection='3d')

ax.plot3D(x[:,0], x[:,1], t)
show()
