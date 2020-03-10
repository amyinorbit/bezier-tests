from .types import *
from . import vector
import numpy as np

def spring_mass(k: float, m: float, anchor: Vec) -> Accelerator:
    def accel(r: Vec) -> Vec:
        return (anchor - r) * k / m
    return accel

def const_gravity(vec: Vec) -> Accelerator:
    def accel(r: Vec) -> Vec:
        return vec
    return accel

def gravity(mu: float, c: Vec) -> Accelerator:
    def accel(r: Vec) -> Vec:
        r_p = r - c
        r_n = vector.norm(r_p)
        return -mu * r_p / (r_n * r_n * r_n)
    return accel
