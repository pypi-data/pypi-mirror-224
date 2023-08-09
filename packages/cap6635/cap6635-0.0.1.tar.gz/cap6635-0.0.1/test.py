from utilities.timer import Timer
from environment.map import Map2D

import numpy as np

with Timer():
    a = Map2D()
    a.buildWall()
    print(a.map)
