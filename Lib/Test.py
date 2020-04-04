from sympy import *
init_printing()


from sympsi import *
from sympsi.pauli import *



theta, t = symbols("theta, t", real=True, positive=True)
eps, Delta, Omega = symbols("epsilon, Delta, Omega", real=True, positive=True)
Hsym = symbols("H")

sx, sy, sz = SigmaX(), SigmaY(), SigmaZ()

H = -eps/2 * sz - Delta/2 * sx
U = exp(I * theta/2 * sy)

hamiltonian_transformation(U, sx)