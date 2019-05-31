import PythonGaussSolver as solver
import numpy as np
from time import time
import subprocess as sbp


def aFunction(x):
    xN = 0.5 * x + 0.5
    return (xN ** 3 / (xN + 1))*np.cos(xN ** 2)


a, b = 0, 1

for i in [_ for _ in range(10)]:
    print("n = " + str(i))
    aSolver = solver.PyGaussSolver(aFunction, a, b, i)
    t0 = time()
    aSolver.exec()
    t1 = time()
    print("Result of Python code: " + str(aSolver.getResult()))
    print("Took : {} ms".format((10 ** 6)*(t1 - t0)))
    t0 = time()
    sbp.call(["gauss.exe", str(i)])
    t1 = time()
    print("Took : {} ms".format((10 ** 3)*(t1 - t0)))
    print("_"*50)

