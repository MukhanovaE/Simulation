from Lib.LinearAlgebraFunctions import *
from Lib.Parametrs import  *
from scipy import *
import qutip as qt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import optimize
from scipy.optimize import curve_fit
from scipy.optimize import least_squares

state = qt.Qobj(1/2*np.array([np.sqrt(3),-1]))
b = qt.Bloch()
b.add_vectors(state)
b.show()