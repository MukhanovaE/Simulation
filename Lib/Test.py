from sympy import *
init_printing()

from sympsi import *
from sympsi.pauli import *

theta, t = symbols("theta, t", real=True, positive=True)
#eps = symbols("epsilon")
#Delta = symbols("Delta")
eps, Delta, Omega = symbols("epsilon, Delta, Omega", real=True, positive=True)
Hsym = symbols("H")

sx, sy, sz = SigmaX(), SigmaY(), SigmaZ()

H = -eps/2 * sz - Delta/2 * sx
U = exp(I * theta/2 * sy)

print(unitary_transformation(U, sx))

hamiltonian_transformation(U, sz)

H1 = hamiltonian_transformation(U, H)
H1