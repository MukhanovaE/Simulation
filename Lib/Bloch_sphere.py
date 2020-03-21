from scipy import *
import qutip as qt
import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import optimize
from scipy.optimize import curve_fit
from scipy.optimize import least_squares
from Lib.Parametrs import *


class bloch_sphere():

    def r_to_rho(r):
        rho = [[0, 0],[0,0]]
        if np.linalg.norm(r) <= 1.:
            rho = (qt.qeye(2) + r[0] * qt.sigmax() + r[1] * qt.sigmay() + r[2] * qt.sigmaz())/2
        else:
            print("ERROR: norm of r is more than 1")
            sys.exit()
        return rho


r = np.array([0, 0, 1])
R = bloch_sphere.r_to_rho(r)

print(R)