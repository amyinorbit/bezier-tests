import numpy as np
from .types import Vec

def square_norm(v: Vec) -> float:
    return np.sum(v * v)

def norm(v: Vec) -> float:
    return np.sqrt(square_norm(v))
