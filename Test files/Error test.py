from sympy import *
init_printing()

from sympsi import *
from sympsi.pauli import *
from sympsi.boson import *
from sympsi.operatorordering import *

Hsym = symbols("H")
omega_r = symbols("ω_r", positive=True)
Hsym = symbols("H")
a = BosonOp("a")

H0 = omega_r * Dagger(a) * a

print(H0)