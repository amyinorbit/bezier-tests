from typing import Callable, NewType, Tuple
from dataclasses import dataclass
import numpy as np
from .types  import *

def verlet(
    r: np.ndarray,
    v: np.ndarray,
    step_size: float,
    accelerate: Accelerator) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Advance a physics simulation using the Verlet method
    """

    step_count = r.shape[0]
    h = step_size
    a = np.ndarray(r.shape)
    b = np.ndarray(r.shape)
    t = np.arange(0.0, step_count) * step_size

    a[0,:] = accelerate(r[0])

    h = step_size
    for n in range(0, step_count-1):
        r[n+1,:] = r[n,:] + v[n,:]*h + 0.5*a[n,:]*(h**2)
        a[n+1,:] = accelerate(r[n+1])
        v[n+1,:] = v[n,:] + 0.5*h*(a[n,:] + a[n+1,:])
        b[n,:] = r[n,:] + 0.5 * v[n,:]*h
    b[-1,:] = r[-1,:] + 0.5 * v[-1,:]*h

    return t, b, a

def refine(
    r: np.ndarray,
    b: np.ndarray,
    v: np.ndarray,
    a: np.ndarray,
    step_size: float,
    sub_count: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Interpolate between points of a physics simulation using bezier curves
    """

    h = step_size
    step_count = r.shape[0]

    new_shape = (step_count * sub_count, r.shape[1])

    t_bezier = np.arange(0, step_count * sub_count) * (h/sub_count)
    r_bezier = np.zeros(new_shape)
    v_bezier = np.zeros(new_shape)

    for n in range(0, step_count-1):
        b0 = r[n]
        b1 = b[n]
        b2 = r[n+1]

        offset = n * sub_count

        for m in range(0, sub_count):
            t0 = m / sub_count
            r_bezier[offset + m] = b0*(1-t0)**2 + 2*(1-t0)*t0*b1 + b2 * t0**2
            v_bezier[offset + m] = (1-t0)*v[n] + t0*v[n+1] # basic lerp
        r_bezier[offset + sub_count] = r[n+1]
        v_bezier[offset + sub_count] = v[n+1]

    IGNORE = - (sub_count - 1)
    return t_bezier[:IGNORE], r_bezier[:IGNORE,:], v_bezier[:IGNORE,:]
