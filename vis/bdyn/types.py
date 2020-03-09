from typing import Callable, NewType, Tuple
import numpy as np

Vec = np.array
Accelerator = Callable[[Vec], Vec]
