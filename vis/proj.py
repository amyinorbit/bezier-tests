#!/usr/bin/env python3
from bdyn import bezier, accelerators
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits import mplot3d

DIM = 2
h = 0.5
num_steps = 5
sub_steps = 10

r = np.empty((num_steps, DIM))
v = np.empty((num_steps, DIM))
r[0,:] = [0, 0]
v[0,:] = [5, 9]

t, b, a = bezier.verlet(r, v, h, accelerators.const_gravity([0, -9.81]))
tb, rb, vb = bezier.refine(r, b, v, a, h, sub_steps)


title(r'Projectile motion, $\vec{v}_0 = (%d, %d)$' % (v[0,0], v[0,1]))
plot(r[:,0], r[:,1], '+', label='verlet solution')
plot(rb[:,0], rb[:,1], '-', label='bezier-refined solution')

xlabel('x')
ylabel('y')
legend()

savefig('projectile.pdf')
