from scipy import *
from qutip import *
import numpy as np
import sys
from matplotlib import *
from matplotlib import colors

# http://qutip.org/docs/4.1/guide/guide-bloch.html


class convert():
    def r_to_rho(r):
        # conversion bloch vector to density matrix
        rho = [[0, 0], [0, 0]]
        if np.linalg.norm(r) <= 1.:
            rho = (qeye(2) + r[0] * sigmax() + r[1] * sigmay() + r[2] * sigmaz()) / 2
        else:
            print("ERROR: norm of r is more than 1")
            sys.exit()
        return rho

    def rho_to_r(rho):
        # conversion density matrix to bloch vector
        r = np.array([0, 0, 0])
        if ((rho[0, 0] + rho[1, 1]) == 1):
            r[2] = (rho[0, 0] - rho[1, 1]).real
            r[1] = 2 * (rho[1, 0]).imag
            r[0] = 2 * (rho[1, 0]).real
        else:
            print("Trace <> 1")
            sys.exit()
        return r

    def pure_state(rho):
        # checking if the state is pure
        if ((rho * rho) == rho):
            print("Pure state")
        else:
            print("Mixed state")

class sphere():
    def axes():
        b = Bloch()
        up = basis(2, 0)
        x = (basis(2, 0) + (1 + 0j) * basis(2, 1)).unit()
        y = (basis(2, 0) + (0 + 1j) * basis(2, 1)).unit()
        z = (basis(2, 0) + (0 + 0j) * basis(2, 1)).unit()
        b.add_states([x, y, z])
        return b


